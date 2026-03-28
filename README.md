**Car Dodger — Developer Setup**

This project is a small Pygame Community Edition (`pygame-ce`) example (entry point: `src/main.py`). The instructions below show how to set up a development environment on macOS using Python 3.14 and a virtual environment, install dependencies, and run the application.

**Prerequisites**

- **Python:** Install Python 3.14. See the **OS-specific Notes** section below for platform-specific installation guidance.
- **System libraries for Pygame:** Some platforms may require SDL or other system libraries — see **OS-specific Notes** below for details and install commands.

**Create and activate virtual environment**

- From the project root, create a venv named `.venv` and activate it:

```
python3.14 -m venv .venv
source .venv/bin/activate
```

- Upgrade pip (recommended):

```
pip install --upgrade pip
```

**Install Python dependencies**

- If there is a `requirements.txt` in the project root, install from it:

```
pip install -r requirements.txt
```

-- If there is no `requirements.txt`, install `pygame-ce` directly:

```
pip install pygame-ce
```

**Run the application**

- From the project root (where `src/` is located), run the game with the module runner (recommended):

```
python3.14 -m src.main
```

- Notes:
  - Using `-m src.main` runs the package import path correctly. Running `python src/main.py` may fail depending on your environment's `PYTHONPATH`.
  - The game opens a window; press the usual keys shown in the code (`Left` / `Right`) to control the player.

**Quick sanity checks**

- Verify the main module imports without launching the window:

```
python3.14 -c "import importlib; importlib.import_module('src.core.game'); print('import OK')"
```

**Development notes & tips**

- The asset loader expects an `assets/` directory at the repo root with subfolders `img/`, `sfx/`, and `music/`. Ensure those exist and contain the required files.
- If sounds or fonts fail to load, check that the `pygame.mixer` and `pygame.font` subsystems are initialized and that the asset paths resolve correctly.
- If you encounter window freeze when the game ends, the project already uses a non-blocking game-over state; ensure you are running the latest code.

**Packaging**

- To build a standalone binary you can use `PyInstaller`. When using PyInstaller, the `asset_loader` handles `sys._MEIPASS` for bundled assets.

```
pyinstaller --onefile --add-data "assets:assets" src/main.py
```

Replace or adapt the `--add-data` paths for macOS if necessary.

**Troubleshooting**

-- If `pygame-ce` installation fails with compilation errors on macOS, ensure Xcode command-line tools are installed and the SDL libraries (via Homebrew) are present.
-- If audio does not play, check your system mixer and that `pygame.mixer` initialized without errors.

**Contact / Next steps**

- For code improvements, consider adding `requirements.txt` (if missing), a small `README` entry describing controls, and simple smoke tests for asset path resolution.

---

**OS-specific Notes**

- **macOS**:
  - Install Python 3.14 (Homebrew or official installer). Using `pyenv` is also convenient for managing multiple Python versions.
  - Install SDL/system deps via Homebrew if you see build or runtime errors:

  ```bash
  brew install sdl2 sdl2_image sdl2_mixer sdl2_ttf
  ```

  - Create and activate the virtualenv as shown earlier:

  ```bash
  python3.14 -m venv .venv
  source .venv/bin/activate
  ```

  - On newer macOS versions you may need to grant microphone/screen recording permission for apps that use audio or Pygame's window features.

- **Windows**:
  - Install Python 3.14 from the official installer and check "Add Python to PATH" if you want `python3.14` on the command line.
  - Create the virtualenv and activate it (cmd.exe):

  ```cmd
  python -m venv .venv
  .venv\Scripts\activate
  ```

  - Or in PowerShell:

  ```powershell
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  ```

  - Install `pygame-ce` inside the activated venv:

  ```powershell
  pip install pygame-ce
  ```

  - If you see compilation errors when installing dependencies, install the latest Visual C++ Build Tools (required for some wheels/source builds). In many cases `pygame-ce` provides Windows wheels and `pip install pygame-ce` should work without build tools.

- **Linux (Debian/Ubuntu)**:
  - Install Python 3.14 packages and development headers plus SDL libs before installing `pygame-ce`:

  ```bash
  sudo apt update
  sudo apt install -y python3.14 python3.14-venv python3.14-dev \
      libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libfreetype6-dev
  ```

  - Create and activate the venv as usual:

  ```bash
  python3.14 -m venv .venv
  source .venv/bin/activate
  pip install --upgrade pip
  pip install pygame-ce
  ```

  - On other distros, use the equivalent package manager and package names (e.g., `dnf`, `pacman`). Ensure ALSA/PulseAudio/pipewire are configured for sound.

**Virtualenv activation quick reference**

- macOS / Linux:

```bash
source .venv/bin/activate
```

- Windows (cmd.exe):

```cmd
.venv\Scripts\activate
```

- Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```
