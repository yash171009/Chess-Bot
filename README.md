# Chess Bot - Stockfish Chess Engine

A web-based chess game where you can play against the Stockfish chess engine.

## Features

- Play chess against Stockfish AI engine
- Choose to play as White or Black
- Board automatically flips based on your color
- Move history in Standard Algebraic Notation (SAN)
- Captured pieces display
- Chess clock with customizable time controls
- Pawn promotion with piece selection (Queen/Rook/Bishop/Knight)

## Installation

### Prerequisites
- Python 3.8 or higher

### Setup (One Command)

1. Navigate to the Backend directory:
```bash
   cd Backend
```

2. Run the setup script:
   
   **Windows:**
```bash
   python setup.py
```
   
   **macOS/Linux:**
```bash
   python3 setup.py
```

   This automatically installs:
   - All Python dependencies (FastAPI, uvicorn, python-chess)
   - Stockfish chess engine

## Running the Application

1. **Start the server:**
   
   **Windows:**
```bash
   python -m uvicorn app:app --reload
```
   
   **macOS/Linux:**
```bash
   python3 -m uvicorn app:app --reload
```

2. **Open your browser:**
   Navigate to `http://127.0.0.1:8000`

## Usage

1. **Choose your color**: Select White or Black from dropdown, click "Apply"
2. **Make moves**: Click a piece, then click destination square
3. **Pawn promotion**: Choose Queen/Rook/Bishop/Knight when pawn reaches end rank
4. **Clock controls**: Set time limits, pause/resume, or start a new game

## Troubleshooting

### "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### "Stockfish not found"
The app works without Stockfish (uses fallback mode), but to install manually:

**macOS:**
```bash
brew install stockfish
```

**Linux:**
```bash
sudo apt install stockfish
```

**Windows:**
Download from [stockfishchess.org](https://stockfishchess.org/download/)

### Port 8000 already in use
```bash
python -m uvicorn app:app --reload --port 8080
```
Then open: `http://127.0.0.1:8080`

## Project Structure
```
Chess Bot/
├── Backend/
│   ├── app.py                 # FastAPI server
│   ├── engine_player.py       # Stockfish interface
│   ├── install_stockfish.py   # Stockfish installer
│   ├── setup.py               # Automated setup
│   ├── requirements.txt       # Dependencies
│   └── bin/                   # Stockfish binary (auto-created)
└── Frontend/
    ├── index.html            # Main page
    ├── script.js             # Game logic
    └── style.css             # Styling
```

## Credits

- [python-chess](https://github.com/niklasf/python-chess) - Chess library
- [Stockfish](https://stockfishchess.org/) - Chess engine
- [FastAPI](https://fastapi.tiangolo.com/) - Web framework