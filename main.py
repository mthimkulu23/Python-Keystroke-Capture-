import sys
import os


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from keylogger import KeyLogger
from config import LOG_FILE, LLM_TRIGGER_KEY

def main():
    """
    Main function to initialize and run the intelligent keylogger.
    """
    print(f"Starting intelligent keystroke capture. All keystrokes will be logged to '{LOG_FILE}'.")
    print(f"Press '{LLM_TRIGGER_KEY.name.replace('f', 'F')}' to send captured text for LLM analysis.")
    print("Press 'Esc' to stop the capture.")

    # Create an instance of the KeyLogger
    keylogger = KeyLogger()

    # Start the keylogger listener
    keylogger.start_listener()

    print("Keystroke capture stopped.")

if __name__ == "__main__":
    main()
