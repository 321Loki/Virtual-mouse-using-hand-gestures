# Virtual Mouse Using Hand Gesture

A Python application that lets you control your mouse cursor using hand gestures
detected via webcam, using OpenCV, MediaPipe, and PyAutoGUI.

## Project Files
- `main.py` – Main application (camera capture, gesture detection, mouse control)
- `util.py` – Helper functions (angle and distance calculations)
- `requirements.txt` – Python dependencies

## Gestures
| Gesture | Action |
|---|---|
| Index finger up, thumb close to palm | Move cursor |
| Index finger bent down, middle finger up | Left click |
| Middle finger bent down, index finger up | Right click |
| Both index and middle fingers bent down (thumb away) | Double click |
| Both index and middle fingers bent down (thumb close) | Take screenshot |

## Setup in VS Code (Step by Step)

### 1. Install Prerequisites
- Install **Python 3.9, 3.10, or 3.11** (MediaPipe does not yet support every
  newer Python version, so avoid 3.12+ if you hit install errors).
  Download from https://www.python.org/downloads/ and tick
  "Add Python to PATH" during install.
- Install **VS Code** from https://code.visualstudio.com/
- In VS Code, install the **Python extension** (by Microsoft) from the
  Extensions tab (Ctrl+Shift+X).

### 2. Open the Project Folder
- Extract/copy the project folder (containing `main.py`, `util.py`,
  `requirements.txt`) somewhere on your computer.
- In VS Code: File → Open Folder → select that folder.

### 3. Create a Virtual Environment
Open a terminal in VS Code (Terminal → New Terminal) and run:

```bash
python -m venv venv
```

Activate it:

- **Windows (PowerShell):**
  ```bash
  venv\Scripts\activate
  ```
- **macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```

VS Code may prompt "Select Interpreter" — choose the one inside
`venv` (e.g. `./venv/Scripts/python.exe` or `./venv/bin/python`).

### 4. Install Dependencies
With the virtual environment activated, run:

```bash
pip install -r requirements.txt
```

This installs `opencv-python`, `mediapipe`, `pyautogui`, `pynput`, and `numpy`.

### 5. Run the Project
```bash
python main.py
```

- A window titled **"Frame"** will open showing your webcam feed with hand
  landmarks drawn on your hand.
- Move your hand in front of the camera to control the cursor.
- Press **`q`** in the Frame window to quit the program.

## Troubleshooting
- **"No module named mediapipe"** – Make sure your virtual environment is
  activated, then re-run `pip install -r requirements.txt`.
- **MediaPipe install fails** – Try a Python version between 3.9 and 3.11
  (MediaPipe wheels lag behind the very latest Python releases).
- **Webcam doesn't open** – Make sure no other app is using the camera, and
  that you've granted camera permission to your terminal/VS Code (especially
  on macOS).
- **Cursor moves erratically / clicks misfire** – Ensure good, even lighting
  and keep your hand fully inside the camera frame. You can tweak the angle
  and distance thresholds in `main.py` to better match your hand size and
  camera distance.
- **`pyautogui` fail-safe triggers** – If your finger moves to a screen
  corner, PyAutoGUI's fail-safe may raise an exception and stop the script.
  This is intentional safety behavior; just move your hand back to center.

## Notes
- Only one hand is detected at a time (`max_num_hands=1`).
- Screenshots taken via the screenshot gesture are saved in the project
  folder as `my_screenshot_<random_number>.png`.
