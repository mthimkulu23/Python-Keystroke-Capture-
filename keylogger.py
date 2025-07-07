

from pynput import keyboard
import logging
import requests
import json
from config import LOG_FILE, LLM_API_URL, LLM_TRIGGER_KEY

class KeyLogger:
    """
    A class to handle keyboard event logging and LLM integration.
    It sets up a listener, logs key presses and releases, and can send
    captured text for LLM analysis.
    """
    def __init__(self):
        """
        Initializes the KeyLogger, setting up the logging configuration
        and the buffer for captured text.
        """
        # Set up logging to write to the specified file
        logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                            format='%(asctime)s: %(message)s')
        self.logger = logging.getLogger()
        self.captured_text_buffer = [] 

    def _send_to_llm_for_analysis(self, text_to_analyze):
        """
        Sends the accumulated text to the Gemini API for analysis.
        Logs the original text and the LLM's response.
        """
        if not text_to_analyze.strip():
            self.logger.info("LLM analysis skipped: No text in buffer.")
            return

        self.logger.info(f"\n--- Sending text for LLM analysis ---")
        self.logger.info(f"Original Text: {text_to_analyze}")

        try:
            # Prepare the chat history for the LLM request
            chat_history = []
            prompt = f"Analyze the following text and provide a concise summary or key insights:\n\n{text_to_analyze}"
            chat_history.push({"role": "user", "parts": [{"text": prompt}]})

            payload = {"contents": chat_history}
           
            api_key = ""
            api_url = f"{LLM_API_URL}?key={api_key}"

            response = requests.post(
                api_url,
                headers={'Content-Type': 'application/json'},
                data=json.dumps(payload)
            )
            response.raise_for_status() 

            result = response.json()

            if result.get("candidates") and len(result["candidates"]) > 0 and \
               result["candidates"][0].get("content") and \
               result["candidates"][0]["content"].get("parts") and \
               len(result["candidates"][0]["content"]["parts"]) > 0:
                llm_response_text = result["candidates"][0]["content"]["parts"][0]["text"]
                self.logger.info(f"LLM Analysis: {llm_response_text}")
            else:
                self.logger.error(f"LLM Analysis failed: Unexpected response structure or no content. Response: {result}")

        except requests.exceptions.RequestException as e:
            self.logger.error(f"LLM Analysis failed: Network or API error: {e}")
        except json.JSONDecodeError as e:
            self.logger.error(f"LLM Analysis failed: JSON decoding error: {e}")
        except Exception as e:
            self.logger.error(f"LLM Analysis failed: An unexpected error occurred: {e}")
        finally:
            self.logger.info(f"--- LLM analysis complete ---\n")
            # Clear the buffer after sending for analysis
            self.captured_text_buffer = []

    def _on_press(self, key):
        """
        This function is called when a key is pressed.
        It logs the key press event and adds the character to the buffer.
        """
        try:
            char = key.char
            self.logger.info(f"Key pressed: {char}")
            if char is not None:
                self.captured_text_buffer.append(char)
        except AttributeError:
            # Handle special keys
            special_key_str = str(key)
            self.logger.info(f"Special key pressed: {special_key_str}")
            # Add a space for common delimiters or newlines for Enter
            if key == keyboard.Key.space:
                self.captured_text_buffer.append(" ")
            elif key == keyboard.Key.enter:
                self.captured_text_buffer.append("\n")
           

    def _on_release(self, key):
        """
        This function is called when a key is released.
        It logs the key release event and handles special actions like stopping
        the listener or triggering LLM analysis.
        """
        self.logger.info(f"Key released: {str(key)}")

        # Stop the listener if 'esc' key is released
        if key == keyboard.Key.esc:
            print("\nExiting keystroke capture. Check the log file for output.")
            return False 

  
        if key == LLM_TRIGGER_KEY:
            text_to_analyze = "".join(self.captured_text_buffer)
            print(f"\nTriggering LLM analysis for: '{text_to_analyze[:50]}...'")
            self._send_to_llm_for_analysis(text_to_analyze)

    def start_listener(self):
        """
        Starts the keyboard listener.
        """
      
        with keyboard.Listener(on_press=self._on_press, on_release=self._on_release) as listener:
          
            listener.join()
