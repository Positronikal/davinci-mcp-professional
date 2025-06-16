#!/usr/bin/env python3
"""
Test script to verify encoding fixes.
"""

import os
import sys

# Set UTF-8 encoding for Windows console
if os.name == 'nt':  # Windows
    os.environ['PYTHONIOENCODING'] = 'utf-8'
    # Try to set console to UTF-8 mode
    try:
        import codecs
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
        sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')
    except (AttributeError, OSError):
        pass  # Fallback to default behavior

from colorama import init as init_colorama, Fore, Style
init_colorama()

def print_status(message: str, status: str = "INFO") -> None:
    """Print a colored status message."""
    if status == "OK":
        print(f"{Fore.GREEN}[OK]{Style.RESET_ALL} {message}")
    elif status == "ERROR":
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} {message}")
    elif status == "WARNING":
        print(f"{Fore.YELLOW}[WARNING]{Style.RESET_ALL} {message}")
    else:
        print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} {message}")

if __name__ == "__main__":
    print("Testing encoding fixes...")
    print_status("This should work without Unicode errors", "OK")
    print_status("This is an error test", "ERROR") 
    print_status("This is a warning test", "WARNING")
    print_status("This is an info test", "INFO")
    print("Test completed successfully!")
