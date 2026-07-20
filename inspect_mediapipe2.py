from mediapipe.tasks.python.vision import hand_landmarker
import inspect
print('hand_landmarker module:', hand_landmarker)
print('attributes:', [name for name in dir(hand_landmarker) if 'HandLandmarker' in name or 'Options' in name])
print('HandLandmarker __init__:', inspect.signature(hand_landmarker.HandLandmarker.__init__))
print('HandLandmarkerOptions __init__:', inspect.signature(hand_landmarker.HandLandmarkerOptions.__init__))
print('HandLandmarker attrs:', [a for a in dir(hand_landmarker.HandLandmarker) if a.startswith('create') or a.startswith('from') or a.endswith('Options')])
print('HandLandmarkerOptions attrs:', [a for a in dir(hand_landmarker.HandLandmarkerOptions) if not a.startswith('_')])
print('HandLandmarkerResult attrs sample:', [a for a in dir(hand_landmarker.HandLandmarkerResult) if not a.startswith('_')][:30])
print(inspect.getsource(hand_landmarker.HandLandmarkerResult)[:500])
