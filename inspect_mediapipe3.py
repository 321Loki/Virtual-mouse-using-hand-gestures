from mediapipe.tasks.python.vision import hand_landmarker
from mediapipe.tasks.python.vision.core import vision_task_running_mode
from mediapipe.tasks.python.core import base_options
import inspect

print('HandLandmarker attrs:', [a for a in dir(hand_landmarker.HandLandmarker) if a.startswith('create')])
print('HandLandmarkerOptions attrs:', [a for a in dir(hand_landmarker.HandLandmarkerOptions) if not a.startswith('_')])
print('VisionTaskRunningMode attrs:', [a for a in dir(vision_task_running_mode.VisionTaskRunningMode) if not a.startswith('_')])
print('BaseOptions attrs:', [a for a in dir(base_options.BaseOptions) if not a.startswith('_')][:50])
print('HandLandmarkerOptionsC attrs:', [a for a in dir(hand_landmarker.HandLandmarkerOptionsC) if not a.startswith('_')][:50])
