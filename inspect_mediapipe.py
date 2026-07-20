import mediapipe as mp
import pathlib
import pkgutil

p = pathlib.Path(mp.__file__).parent
print('mediapipe file:', mp.__file__)
print('has solutions:', hasattr(mp, 'solutions'))
print('package path:', p)
print('top-level:', sorted([m.name for m in pkgutil.iter_modules([str(p)])]))

for sub in ['tasks', 'tasks/python', 'tasks/python/vision', 'tasks/python/vision/hand_landmarker']:
    q = p.joinpath(*sub.split('/'))
    if q.exists():
        print('\nContents of', q)
        for child in sorted(q.iterdir()):
            print('  ', child.name)
