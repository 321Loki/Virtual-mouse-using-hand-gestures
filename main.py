import argparse
import time

import cv2
import numpy as np
import pyautogui
from util import clamp, scale_point

pyautogui.FAILSAFE = False
screen_width, screen_height = pyautogui.size()

try:
    import mediapipe as mp
    mp_hands = mp.solutions.hands
    Hands = mp_hands.Hands
    drawing_utils = mp.solutions.drawing_utils
except Exception:
    print("MediaPipe 'solutions.hands' not available in this environment.")
    print("To enable hand tracking, install a MediaPipe version that provides the legacy 'solutions' API inside your venv:")
    print("    pip install 'mediapipe==0.10.5'")
    raise


def parse_args():
    parser = argparse.ArgumentParser(description="Hand tracking mouse controller")
    parser.add_argument("--camera", type=int, default=0, help="Webcam index")
    parser.add_argument("--smoothing", type=float, default=0.65, help="Cursor smoothing factor (0-1)")
    parser.add_argument("--click-threshold", type=float, default=0.06, help="Thumb-index pinch distance threshold for left click")
    parser.add_argument("--right-threshold", type=float, default=0.08, help="Thumb-middle pinch distance threshold for right click")
    parser.add_argument("--double-threshold", type=float, default=0.10, help="Thumb-ring pinch distance threshold for double click")
    parser.add_argument("--mirror", action="store_true", help="Mirror video feed horizontally")
    parser.add_argument("--test", action="store_true", help="Test mode (checks dependencies, exits gracefully)")
    return parser.parse_args()


def draw_status(frame, status, left_active, right_active, fps):
    label = f"Status: {status}"
    cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    cv2.putText(frame, f"FPS: {fps:.1f}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 200, 0), 2)
    cv2.putText(frame, f"Left: {'ON' if left_active else 'OFF'}  Right: {'ON' if right_active else 'OFF'}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)


def main():
    args = parse_args()
    
    # Test mode: verify dependencies without needing a webcam
    if args.test:
        print("Testing dependencies...")
        print("✓ mediapipe", mp.__version__)
        print("✓ cv2 version", cv2.__version__)
        print("✓ numpy version", np.__version__)
        print("✓ pyautogui available")
        print("✓ All dependencies OK")
        print("\nScreen resolution:", screen_width, "x", screen_height)
        return
    
    cap = cv2.VideoCapture(args.camera)
    if not cap.isOpened():
        print(f"Error: Could not open webcam at index {args.camera}.")
        return

    prev_cursor = np.array([screen_width * 0.5, screen_height * 0.5], dtype=np.float32)
    left_click_active = False
    right_click_active = False
    double_click_active = False
    last_time = time.time()

    with Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.55, min_tracking_confidence=0.55) as hands:
        while True:
            try:
                success, frame = cap.read()
                if not success:
                    print("Error: Failed to read frame from webcam.")
                    break

                if args.mirror:
                    frame = cv2.flip(frame, 1)

                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = hands.process(frame_rgb)
                status = "No hand detected"
                h, w, _ = frame.shape
                current_time = time.time()
                fps = 1.0 / (current_time - last_time) if current_time != last_time else 0.0
                last_time = current_time

                if results.multi_hand_landmarks:
                    hand = results.multi_hand_landmarks[0]
                    index_tip = hand.landmark[8]
                    thumb_tip = hand.landmark[4]
                    middle_tip = hand.landmark[12]

                    ix = int(index_tip.x * w)
                    iy = int(index_tip.y * h)
                    tx = int(thumb_tip.x * w)
                    ty = int(thumb_tip.y * h)
                    mx = int(middle_tip.x * w)
                    my = int(middle_tip.y * h)

                    drawing_utils.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
                    cv2.circle(frame, (ix, iy), 10, (0, 255, 0), -1)
                    cv2.circle(frame, (tx, ty), 8, (255, 180, 0), -1)
                    cv2.circle(frame, (mx, my), 8, (0, 150, 255), -1)

                    screen_x = scale_point(index_tip.x, 0, 1, 0, screen_width)
                    screen_y = scale_point(index_tip.y, 0, 1, 0, screen_height)
                    screen_x = clamp(screen_x, 0, screen_width - 1)
                    screen_y = clamp(screen_y, 0, screen_height - 1)

                    prev_cursor = prev_cursor * (1.0 - args.smoothing) + np.array([screen_x, screen_y]) * args.smoothing
                    cursor_x = int(prev_cursor[0])
                    cursor_y = int(prev_cursor[1])
                    pyautogui.moveTo(cursor_x, cursor_y, duration=0.01)
                    status = "Tracking hand"

                    ring_tip = hand.landmark[16]
                    rx = int(ring_tip.x * w)
                    ry = int(ring_tip.y * h)
                    cv2.circle(frame, (rx, ry), 8, (255, 0, 255), -1)

                    pinch_dist = np.hypot(index_tip.x - thumb_tip.x, index_tip.y - thumb_tip.y)
                    right_dist = np.hypot(middle_tip.x - thumb_tip.x, middle_tip.y - thumb_tip.y)
                    double_dist = np.hypot(ring_tip.x - thumb_tip.x, ring_tip.y - thumb_tip.y)

                    if double_dist < args.double_threshold and not double_click_active and not left_click_active and not right_click_active:
                        pyautogui.click(clicks=2)
                        double_click_active = True
                        status = "Double click"
                    elif double_click_active and double_dist > args.double_threshold + 0.03:
                        double_click_active = False

                    if right_dist < args.right_threshold and not right_click_active and not left_click_active and not double_click_active:
                        pyautogui.mouseDown(button="right")
                        right_click_active = True
                        status = "Right click"
                    elif right_click_active and right_dist > args.right_threshold + 0.03:
                        pyautogui.mouseUp(button="right")
                        right_click_active = False
                        status = "Right released"

                    if pinch_dist < args.click_threshold and not left_click_active and not right_click_active and not double_click_active:
                        pyautogui.mouseDown()
                        left_click_active = True
                        status = "Left click"
                    elif left_click_active and pinch_dist > args.click_threshold + 0.03:
                        pyautogui.mouseUp()
                        left_click_active = False
                        status = "Released"

                draw_status(frame, status, left_click_active, right_click_active, fps)
                cv2.imshow("Hand Tracker", frame)

                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    break
                if key == ord('m'):
                    args.mirror = not args.mirror
            except KeyboardInterrupt:
                print("\nInterrupted by user")
                break
            except Exception as e:
                print(f"Error in main loop: {e}")
                import traceback
                traceback.print_exc()
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
