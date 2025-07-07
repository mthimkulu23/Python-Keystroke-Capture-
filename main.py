# main.py

# This is the main entry point for the keystroke capture application.
# It initializes the keylogger and starts listening for events.

import sys
import os

# Add the parent directory to the Python path to allow importing modules
# from the current project structure. This is important when running
# the script from a different directory or when the modules are not
# directly in the Python path.
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from keylogger import KeyLogger
from config import LOG_FILE

def main():
    """
    Main function to initialize and run the keylogger.
    """
    print(f"Starting keystroke capture. All keystrokes will be logged to '{LOG_FILE}'.")
    print("Press 'Esc' to stop the capture.")

    # Create an instance of the KeyLogger
    keylogger = KeyLogger()

    # Start the keylogger listener
    keylogger.start_listener()

    print("Keystroke capture stopped.")

if __name__ == "__main__":
    main()
