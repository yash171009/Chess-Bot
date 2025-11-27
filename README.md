# Chess Bot - Stockfish Chess Engine

A web-based chess game where you can play against the Stockfish chess engine.

## Features

- Play chess against Stockfish engine
- Choose to play as White or Black
- Board automatically flips when playing as Black
- Move history and captured pieces display
- Chess clock with customizable time controls
- Automatic pawn promotion

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Navigate to the Backend directory:**
   ```bash
   cd Backend
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Run the setup script:**
   ```bash
   python3 setup.py
   ```
   
   **Note:** On macOS/Linux, use `python3` instead of `python`. If `python3` is not found, you may need to install Python 3 first.
   
   This will:
   - Install all Python requirements (FastAPI, uvicorn, python-chess)
   - Attempt to install Stockfish automatically
   
   **Note:** Stockfish installation varies by OS:
   - **Windows**: Automatically downloads and installs
   - **macOS**: Attempts Homebrew installation (recommended: `brew install stockfish`)
   - **Linux**: Attempts apt/yum installation (may require sudo)

5. **If Stockfish installation fails**, install it manually:
   - **macOS**: `brew install stockfish`
   - **Linux (Debian/Ubuntu)**: `sudo apt-get install stockfish`
   - **Linux (RedHat/Fedora)**: `sudo yum install stockfish`
   - **Windows**: Download from [stockfishchess.org](https://stockfishchess.org/download/)

### Running the Application

1. **Start the server:**
   ```bash
   python3 app.py
   ```
   
   Or with uvicorn directly:
   ```bash
   python3 -m uvicorn app:app --reload
   ```
   
   **Note:** On macOS/Linux, use `python3` instead of `python`.

2. **Open your browser:**
   Navigate to `http://localhost:8000`

## Usage

1. **Choose your color**: Select White or Black from the dropdown and click "Apply"
2. **Make moves**: Click on a piece, then click on a legal destination square
3. **Pawn promotion**: When a pawn reaches the end, a promotion dialog will appear
4. **Clock controls**: Set time limits, pause/resume, or start a new game

## Project Structure

```
Chess-bot/
├── Backend/
│   ├── app.py                 # FastAPI application
│   ├── engine_player.py       # Stockfish engine interface
│   ├── install_stockfish.py   # Stockfish auto-installer
│   ├── setup.py               # Setup script
│   ├── requirements.txt       # Python dependencies
│   └── bin/                   # Local Stockfish binary (created during setup)
└── Frontend/
    ├── index.html            # Main HTML
    ├── script.js             # Frontend logic
    └── style.css             # Styling
```

## Troubleshooting

### Stockfish not found

If you see "Stockfish not found" warnings:

1. **Check if Stockfish is installed:**
   ```bash
   which stockfish  # macOS/Linux
   where stockfish  # Windows
   ```

2. **Set the STOCKFISH_EXECUTABLE environment variable:**
   ```bash
   export STOCKFISH_EXECUTABLE=/path/to/stockfish  # macOS/Linux
   set STOCKFISH_EXECUTABLE=C:\path\to\stockfish.exe  # Windows
   ```

3. **The app will use a fallback move generator** if Stockfish is not available, but moves will be less optimal.

### Board not flipping

If the board doesn't flip when switching to Black:
- Make sure you're using a modern browser
- Check the browser console for JavaScript errors

## License

This project uses:
- [python-chess](https://github.com/niklasf/python-chess) - Chess library
- [Stockfish](https://stockfishchess.org/) - Chess engine
- [FastAPI](https://fastapi.tiangolo.com/) - Web framework

