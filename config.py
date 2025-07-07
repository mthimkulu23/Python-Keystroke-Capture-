
from pynput import keyboard

# Define the log file name
LOG_FILE = "keystrokes.log"

# --- LLM Integration Configuration ---
LLM_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"


# keyboard.Key.ctrl_l for Left Control
LLM_TRIGGER_KEY = keyboard.Key.f12
