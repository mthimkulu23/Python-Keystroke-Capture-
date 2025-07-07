# Intelligent Keystroke Capture Project

This project provides a Python-based keystroke capture utility with an added "intelligence" feature. It logs all keystrokes to a local file and can, upon a user-defined trigger, send the accumulated text to a Large Language Model (LLM) for analysis and summarization.

# Features

Keystroke Logging: Captures and logs all pressed and released keys to a keystrokes.log file.

Intelligent Analysis: Integrates with the Google Gemini API to provide summaries or insights on captured text.

Configurable Trigger: Allows you to define a specific key (e.g., F12) to trigger the LLM analysis.

Standalone Executable: Can be packaged into a single executable file using PyInstaller for easy distribution.


# Setup and Installation

Follow these steps to set up and run the project:

Clone the Repository (or create the files):

If you're getting this project as files, ensure you have the main.py, keylogger.py, config.py, and requirements.txt files in a 
directory named keystroke_project.

Create a Virtual Environment (Recommended):

It's best practice to use a virtual environment to manage project dependencies.


cd keystroke_project

python3 -m venv .venv

Activate the Virtual Environment:

# macOS/Linux:

source .venv/bin/activate

# Windows (Command Prompt):

.venv\Scripts\activate.bat

# Windows (PowerShell):

.venv\Scripts\Activate.ps1

Install Dependencies:

With your virtual environment activated, install the required Python libraries:

pip install -r requirements.txt

# Running the Application
Development Mode (from source code)

To run the application directly from the Python scripts:

Activate your virtual environment (if not already active).

Navigate to the keystroke_project directory.

Run the main script:

python main.py


