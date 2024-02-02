# Виконано за допомогою ChatGPT


import os
import sys
from pathlib import Path
from colorama import Fore, Style

def display_directory_structure(directory_path):
    directory_path = Path(directory_path)

    if not directory_path.exists() or not directory_path.is_dir():
        print(f"Error: {directory_path} is not a valid directory.")
        return

    print(f"Directory structure for: {directory_path}\n")

    display_contents(directory_path, 0)

def display_contents(path, indent_level):
    for item in path.iterdir():
        if item.is_dir():
            print(Fore.BLUE + "  " * indent_level + f"📁 {item.name}")
            display_contents(item, indent_level + 1)
        else:
            print(Fore.GREEN + "  " * indent_level + f"📄 {item.name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python directory_structure.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        display_directory_structure(directory_path)
