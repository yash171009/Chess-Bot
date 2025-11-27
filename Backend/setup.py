#!/usr/bin/env python3
"""
Setup script that installs Python requirements and Stockfish.
Run this after creating your virtual environment.

Usage:
    python3 setup.py
    # or if python3 is aliased to python:
    python setup.py
"""
import subprocess
import sys
import os
import shutil
from pathlib import Path

def find_python():
    """Find the best Python executable to use."""
    # Try sys.executable first (the one running this script)
    if sys.executable:
        return sys.executable
    
    # Try python3
    python3 = shutil.which('python3')
    if python3:
        return python3
    
    # Try python
    python = shutil.which('python')
    if python:
        return python
    
    # Fallback
    return 'python3'

def main():
    script_dir = Path(__file__).parent
    python_exe = find_python()
    
    print("=" * 60)
    print("Chess Bot Setup")
    print("=" * 60)
    print(f"Using Python: {python_exe}")
    print("=" * 60)
    
    # Install Python requirements
    print("\n[1/2] Installing Python requirements...")
    try:
        subprocess.check_call([
            python_exe, "-m", "pip", "install", "-r", "requirements.txt"
        ], cwd=script_dir)
        print("✓ Python requirements installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"✗ Error installing Python requirements: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"✗ Python executable not found: {python_exe}")
        print("  Please ensure Python 3 is installed and in your PATH")
        sys.exit(1)
    
    # Install Stockfish
    print("\n[2/2] Installing Stockfish engine...")
    try:
        install_script = script_dir / "install_stockfish.py"
        result = subprocess.run([
            python_exe, str(install_script)
        ], cwd=script_dir, capture_output=True, text=True)
        
        print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        
        if result.returncode == 0:
            print("✓ Stockfish installation completed")
        else:
            print("⚠ Stockfish installation had issues, but continuing...")
            print("  You may need to install Stockfish manually.")
    except Exception as e:
        print(f"⚠ Error running Stockfish installer: {e}")
        print("  You may need to install Stockfish manually.")
    
    print("\n" + "=" * 60)
    print("Setup complete!")
    print("=" * 60)
    print("\nTo start the server, run:")
    print(f"  {python_exe} app.py")
    print("\nOr with uvicorn:")
    print(f"  {python_exe} -m uvicorn app:app --reload")

if __name__ == '__main__':
    main()

