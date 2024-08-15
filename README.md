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
    - macOS: Pending (if at all possible). Figure this out yourself or set up a Windows or Linux VM.
5. Type in `git clone https://github.com/Tech-FZ/Misonic-Project`.
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
5. Try to run the game. If it works, good.