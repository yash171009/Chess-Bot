#!/usr/bin/env python3
"""
Auto-install Stockfish chess engine for Mac, Windows, or Linux.
This script downloads the appropriate Stockfish binary and places it in Backend/bin/
"""
import os
import sys
import platform
import urllib.request
import zipfile
import tarfile
import shutil
from pathlib import Path

# Stockfish download URLs (using official GitHub releases)
STOCKFISH_RELEASES = {
    'Windows': {
        'x86_64': 'https://github.com/official-stockfish/Stockfish/releases/download/sf_16/stockfish_16_win_x64_avx2.zip',
        'x86': 'https://github.com/official-stockfish/Stockfish/releases/download/sf_16/stockfish_16_win_x64_avx2.zip'
    },
    'Darwin': {  # macOS
        'x86_64': 'https://github.com/official-stockfish/Stockfish/releases/download/sf_16/stockfish_16_src.zip',
        'arm64': 'https://github.com/official-stockfish/Stockfish/releases/download/sf_16/stockfish_16_src.zip'
    },
    'Linux': {
        'x86_64': 'https://github.com/official-stockfish/Stockfish/releases/download/sf_16/stockfish_16_src.zip',
        'aarch64': 'https://github.com/official-stockfish/Stockfish/releases/download/sf_16/stockfish_16_src.zip'
    }
}

# Alternative: Use pre-built binaries from stockfishchess.org
STOCKFISH_BINARIES = {
    'Windows': {
        'x86_64': 'https://stockfishchess.org/files/stockfish_16_win_x64_avx2.zip',
    },
    'Darwin': {
        'x86_64': 'https://stockfishchess.org/files/stockfish_16_src.zip',
        'arm64': 'https://stockfishchess.org/files/stockfish_16_src.zip'
    },
    'Linux': {
        'x86_64': 'https://stockfishchess.org/files/stockfish_16_src.zip',
        'aarch64': 'https://stockfishchess.org/files/stockfish_16_src.zip'
    }
}


def get_system_info():
    """Get system OS and architecture."""
    system = platform.system()
    machine = platform.machine().lower()
    
    # Normalize architecture names
    if machine in ['x86_64', 'amd64']:
        arch = 'x86_64'
    elif machine in ['arm64', 'aarch64']:
        arch = 'arm64' if system == 'Darwin' else 'aarch64'
    elif machine in ['i386', 'i686', 'x86']:
        arch = 'x86'
    else:
        arch = machine
    
    return system, arch


def download_file(url, dest_path):
    """Download a file from URL to destination path."""
    print(f"Downloading Stockfish from {url}...")
    try:
        urllib.request.urlretrieve(url, dest_path)
        print(f"Downloaded to {dest_path}")
        return True
    except Exception as e:
        print(f"Error downloading: {e}")
        return False


def extract_zip(zip_path, extract_to):
    """Extract ZIP file to directory."""
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        return True
    except Exception as e:
        print(f"Error extracting ZIP: {e}")
        return False


def extract_tar(tar_path, extract_to):
    """Extract TAR file to directory."""
    try:
        with tarfile.open(tar_path, 'r:*') as tar_ref:
            tar_ref.extractall(extract_to)
        return True
    except Exception as e:
        print(f"Error extracting TAR: {e}")
        return False


def find_stockfish_binary(extract_dir):
    """Find the Stockfish executable in extracted directory."""
    stockfish_names = ['stockfish', 'stockfish.exe', 'Stockfish', 'Stockfish.exe']
    
    for root, dirs, files in os.walk(extract_dir):
        for file in files:
            if file in stockfish_names:
                return os.path.join(root, file)
    
    return None


def install_stockfish():
    """Main installation function."""
    system, arch = get_system_info()
    print(f"Detected system: {system}, architecture: {arch}")
    
    # Get script directory and create bin directory
    script_dir = Path(__file__).parent
    bin_dir = script_dir / 'bin'
    bin_dir.mkdir(exist_ok=True)
    
    stockfish_path = bin_dir / ('stockfish.exe' if system == 'Windows' else 'stockfish')
    
    # Check if already installed
    if stockfish_path.exists():
        print(f"Stockfish already installed at {stockfish_path}")
        return str(stockfish_path)
    
    # Try to get download URL
    download_url = None
    
    # For Windows, use pre-built binary
    if system == 'Windows':
        if arch == 'x86_64':
            download_url = STOCKFISH_BINARIES.get('Windows', {}).get('x86_64')
        elif arch == 'x86':
            # Stockfish doesn't provide 32-bit Windows binaries
            print("32-bit Windows is not supported by Stockfish.")
            print("Please install the 64-bit version of Windows or download Stockfish manually from:")
            print("  https://stockfishchess.org/download/")
            return None
        else:
            print(f"Unsupported Windows architecture: {arch}")
            print("Please download Stockfish manually from: https://stockfishchess.org/download/")
            return None
    # For macOS and Linux, try package managers first, then download pre-built binaries
    elif system == 'Darwin':
        # Try Homebrew first
        brew_path = shutil.which('brew')
        if brew_path:
            print("Found Homebrew. Attempting to install Stockfish via Homebrew...")
            result = os.system(f'{brew_path} install stockfish 2>&1')
            if result == 0:
                stockfish_system = shutil.which('stockfish')
                if stockfish_system:
                    print(f"✓ Stockfish installed via Homebrew at {stockfish_system}")
                    return stockfish_system
        
        # Stockfish doesn't provide pre-built binaries for macOS
        # Source code downloads won't contain executable binaries
        print("Homebrew installation failed or not available.")
        if arch == 'arm64':
            # For Apple Silicon, try to download or use Homebrew
            print("For Apple Silicon Macs, please install via Homebrew:")
            print("  brew install stockfish")
            print("Or download from: https://stockfishchess.org/download/")
        else:
            # For Intel Mac, no pre-built binaries available
            print("For Intel macOS, Stockfish doesn't provide pre-built binaries.")
            print("Please install via Homebrew: brew install stockfish")
            print("Or download and compile from source: https://stockfishchess.org/download/")
        return None
        
    elif system == 'Linux':
        # Try apt (Debian/Ubuntu) first
        apt_path = shutil.which('apt')
        if apt_path:
            print("Found apt. Attempting to install Stockfish...")
            print("(This may require sudo password)")
            result = os.system('sudo apt-get update -qq && sudo apt-get install -y stockfish 2>&1')
            if result == 0:
                stockfish_system = shutil.which('stockfish')
                if stockfish_system:
                    print(f"✓ Stockfish installed via apt at {stockfish_system}")
                    return stockfish_system
        
        # Try yum/dnf (RedHat/Fedora)
        yum_path = shutil.which('yum') or shutil.which('dnf')
        if yum_path:
            print(f"Found {yum_path}. Attempting to install Stockfish...")
            print("(This may require sudo password)")
            result = os.system(f'sudo {yum_path} install -y stockfish 2>&1')
            if result == 0:
                stockfish_system = shutil.which('stockfish')
                if stockfish_system:
                    print(f"✓ Stockfish installed at {stockfish_system}")
                    return stockfish_system
        
        # Stockfish doesn't provide pre-built binaries for Linux
        # Source code downloads won't contain executable binaries
        print("Package manager installation failed.")
        print("Stockfish doesn't provide pre-built binaries for Linux.")
        print("Please install via package manager:")
        print("  sudo apt-get install stockfish  # Debian/Ubuntu")
        print("  sudo yum install stockfish      # RedHat/Fedora")
        print("  sudo pacman -S stockfish        # Arch Linux")
        print("Or download and compile from source: https://stockfishchess.org/download/")
        return None
    
    # If we have a download URL (Windows), download and extract
    if download_url:
        temp_dir = script_dir / 'temp_stockfish'
        temp_dir.mkdir(exist_ok=True)
        zip_path = temp_dir / 'stockfish.zip'
        
        if not download_file(download_url, zip_path):
            return None
        
        if not extract_zip(zip_path, temp_dir):
            return None
        
        # Find the binary
        found_binary = find_stockfish_binary(temp_dir)
        if found_binary:
            shutil.copy2(found_binary, stockfish_path)
            # Make executable on Unix systems
            if system != 'Windows':
                os.chmod(stockfish_path, 0o755)
            
            # Cleanup
            shutil.rmtree(temp_dir)
            
            print(f"Stockfish installed successfully at {stockfish_path}")
            return str(stockfish_path)
        else:
            print("Could not find Stockfish binary in downloaded archive")
            shutil.rmtree(temp_dir)
            return None
    
    return None


if __name__ == '__main__':
    result = install_stockfish()
    if result:
        print(f"\n✓ Stockfish installation complete!")
        print(f"  Location: {result}")
        sys.exit(0)
    else:
        print("\n✗ Stockfish installation failed or not supported for this system.")
        print("  Please install Stockfish manually from: https://stockfishchess.org/download/")
        sys.exit(1)

