# Dynopoly

Build up a functional monopoly while dealing with dysfunctional events that occur every turn.

## Dev environment setup

### Part for everyone

1. Get [Python 3.12](https://www.python.org/downloads/release/python-3125/) and follow its setup procedures.
    - On Windows and macOS, you will need to install that.
    - On Linux, you may have Python 3 installed already. Open a terminal and type `python3 --version` to check.
2. Get [Git](https://git-scm.com/downloads)
3. Create a folder where you store this code. It's up to you where to store it.
4. For different OSes
    - Linux (GUI, may differ from desktop to desktop): Open the folder, then right-click on the empty space and "Open with Terminal".
    - Windows 10: Open the folder, then click on "File", then on "Open Windows PowerShell".
    - Windows 11: Open the folder, then right-click on the empty space and "Open in Terminal".
    - macOS: If you don't know how to do it, set up a Windows or Linux VM and test the game on there. None of us have a Mac because it's too expensive. Sorry. :(
5. Type in `git clone https://github.com/Tech-FZ/Dynopoly`.
6. Open the project in your desired IDE/code editor. Nicolas is using Visual Studio Code, Mizuki is using Notepad++. Due to the variety, it is too complicated to tell you how to do it. If you need help, ask.
7. Prepare a folder where you store your virtual environment and apply number 4 to open your terminal application again.
8. Type in one of the following, replacing `(your-venv-name)` with the actual venv name you're planning to use:
    - Windows: `python -m venv (your-venv-name)` or `py -3 -m venv (your-venv-name)`
    - Linux: `python3 -m venv (your-venv-name)`
    - macOS: Any of the commands from the others.

### Visual Studio Code/VSCodium

1. When you open VS Code, double-click on `main.py`.
2. Wait for the Python version to show up on the bottom right of VS Code.
3. Click on that version and select "Enter interpreter path", then "Find" and look for the following, replacing `(your-venv-path)` with where your venv is:
    - Windows: `(your-venv-path)\Scripts\python.exe`
    - macOS & Linux: `(your-venv-path)/bin/python`
4. Run your program using the Play button on the top right, below the title bar. A terminal, followed by a failed attempt at running the project will open.
5. On that terminal, type in `pip install --upgrade pygame==2.6.0`.
6. Try to run it again. If it works, good.

### Notepad++ (Windows only)

1. You need to open the files individually with Notepad++. Right-click on the file to edit and then "Edit with Notepad++".
    - Windows 11: You need to click on "More options" first.
2. Open PowerShell/Windows Terminal within the folder where the code is stored. Refer to 4 in the [part for everyone](#part-for-everyone).
3. Type in `"(your-venv-path)\Scripts\Activate.ps1"` to activate the venv.
4. Run `pip install --upgrade pygame==2.6.0`.
5. Try to run the game by running `python main.py`. If it works, good.
    - If that doesn't work, type in the following: `(your-venv-path)\Scripts\python main.py`

### Nano

Attention: A window manager (like Xorg or Wayland) and a desktop (e. g. GNOME, KDE Plasma or Xfce) are still required. If you love the terminal so much, it's your decision.

1. You need to open a terminal in your project directory. Refer to 4 in the [part for everyone](#part-for-everyone)
2. Type in `nano (file-to-edit)`, replacing (file-to-edit) with the actual name of the file you want to edit.
    - If the file is in a subdirectory, change to it with `cd` first. This part should be self-explanatory.
3. Edit the file.
4. Save the file by pressing <kbd>Ctrl</kbd> + <kbd>O</kbd>, then <kbd>Enter</kbd>.
5. Close Nano by pressing <kbd>Ctrl</kbd> + <kbd>X</kbd>.
    - If you are in a subdirectory, navigate back to the root of the project with `cd ..` when you're done.
6. Repeat the process until you edited all of the files you want to edit.
7. Type in the following to activate your venv:
    - Windows: `"(your-venv-path)\Scripts\Activate.ps1"`
    - macOS & Linux: `(your-venv-path)/bin/activate.sh`
8. Run the game with `python main.py`.
    - On Linux, you may have to run `python ./main.py`.
    - If that doesn't work, run the following:
        - Windows: `(your-venv-path)\Scripts\python main.py`
        - Linux: `(your-venv-path)/bin/python main.py` or `(your-venv-path)/bin/python ./main.py`
9. If it works, good.

## Compile the game

1. Do everything in [Dev environment setup](#dev-environment-setup) if you haven't already done so.
2. In the terminal, activate the venv if you deactivated it.
3. Run `pip install pyinstaller pillow` to install PyInstaller, which compiles the program, and Pillow, which converts the icon.
4. Copy and paste all files except the .git folder, the build and dist folders and the main.spec file.
5. Run the following:
    - Windows: `pyinstaller --icon icon.png --onefile main.py`
    - Other platforms: `pyinstaller --onefile main.py`
6. After PyInstaller did its job, double-click on dist and press <kbd>Ctrl</kbd> + <kbd>V</kbd> to paste the files.
7. Test the binaries. If they work, good.
    - On Windows (and probably also macOS), your antivirus may interfere. This is completely normal behaviour from the overprotective software and it is safe to restore the game from quarantine.

## Run the game

1. Download it from the releases.
2. Extract the file.
    - Windows (ZIP files): Right-click, then click on "Extract to" and follow the procedure.
    - Windows (other compressed files): Download [7-Zip](https://www.7-zip.org) and follow the installation procedure, then right-click on the file of the game, then on "Extract to (insert-file-name-here)/".
    - Linux (GUI): Right-click, then click on "Open with Archive Manager" or something, then on "Extract" and save where you want to.
3. Access your extracted files and run the executables as follows:
    - Script: Follow [Dev environment setup](#dev-environment-setup)
    - Executables: Double-click on "main" (Linux) or "main.exe" (Windows)
        - On Windows (and probably also macOS), your antivirus may interfere. This is completely normal behaviour from the overprotective software and it is safe to restore the game from quarantine.
        - On Linux, you may have to right-click, then click on "Properties", then on "Permissions" and check "File may be run as program" before running.
4. If it works, good.
