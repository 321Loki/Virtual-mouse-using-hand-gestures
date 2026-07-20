# QUICK START GUIDE - Hand Gesture Mouse Controller

## ✅ Setup Complete!

Your Hand Gesture Mouse Controller is ready to use. All files are saved in:
```
D:\Downloads\MINI project code\
```

---

## 🚀 How to Run (Choose One)

### Option 1: Double-Click (Easiest)
1. Open File Explorer and go to `D:\Downloads\MINI project code\`
2. **Double-click `run.bat`**
3. A window will open showing your webcam with hand detection

### Option 2: PowerShell Script
1. Open PowerShell in this directory
2. Run: `.\run.ps1`
3. Application starts with helpful tips displayed

### Option 3: Direct Command
1. Open PowerShell or Command Prompt in this directory
2. Run: `python main.py`

### Option 4: Test Mode (No Webcam Needed)
1. Double-click `test.bat` OR
2. Run: `python main.py --test`

---

## 🎮 Hand Gestures

Once running, use these gestures to control your mouse:

| Gesture | Action |
|---------|--------|
| Index finger pointing up, thumb to palm | Move cursor |
| Pinch thumb + index finger | Left click |
| Pinch thumb + middle finger | Right click |
| Pinch thumb + ring finger | Double click |

---

## ⌨️ Keyboard Controls

| Key | Action |
|-----|--------|
| `q` | Quit application |
| `m` | Toggle mirror (flip video horizontally) |

---

## 🔧 Troubleshooting

### "Could not open webcam"
- Check webcam is connected
- No other app is using the camera (Zoom, Discord, etc.)
- Close the application and try again

### Hand not detected
- Ensure good lighting
- Keep hand fully in camera frame
- Position camera at arm's length
- Adjust `--click-threshold` or `--right-threshold` in code

### Cursor moves erratically
- Improve lighting
- Keep hand steady in frame
- Increase `--smoothing` value (0.0 to 1.0)

---

## 📝 Project Files

```
main.py              ← Main application (hand tracking & mouse control)
util.py              ← Helper functions (math, scaling)
requirements.txt     ← Python dependencies
venv/                ← Virtual environment (dependencies installed here)
run.bat              ← Easy launcher (Windows batch)
run.ps1              ← PowerShell launcher
test.bat             ← Test dependencies
```

---

## 💾 Project Location

**Keep the entire folder at:**
```
D:\Downloads\MINI project code\
```

All scripts and the virtual environment are configured for this path.

---

## 🎯 Tips for Best Results

1. **Lighting**: Use a well-lit room (no dark shadows on hand)
2. **Camera angle**: Position camera slightly above eye level
3. **Distance**: Keep hand 12-24 inches from camera
4. **Gestures**: Use slow, deliberate hand movements
5. **Calibration**: Pinch distances can be adjusted in `main.py` (lines with `--click-threshold`)

---

## 📚 Advanced: Command Line Options

```bash
python main.py --help                    # Show all options
python main.py --camera 0                # Use camera 0 (default)
python main.py --camera 1                # Use camera 1 (if multiple cameras)
python main.py --smoothing 0.8           # Increase cursor smoothing (0-1)
python main.py --click-threshold 0.05    # Adjust left-click sensitivity
python main.py --right-threshold 0.07    # Adjust right-click sensitivity
python main.py --double-threshold 0.09   # Adjust double-click sensitivity
python main.py --mirror                  # Start with mirror mode enabled
python main.py --test                    # Test mode (verify dependencies)
```

---

## ✨ You're All Set!

Simply double-click **`run.bat`** to start controlling your mouse with hand gestures.

Enjoy! 🎉
