"""
Activity Logger Module
This module provides logging functionality for file operations.
"""

import os
from datetime import datetime


def log_activity(folder_path, file_name, action="created and archived"):
    """
    Log an activity to the activity_log.txt file inside the StudentFiles folder.

    Args:
        folder_path (str): The path to the StudentFiles folder
        file_name (str): The name of the file being logged
        action (str): The action performed (default: "created and archived")

    Returns:
        bool: True if logging was successful, False otherwise
    """
    try:
        # Create the log file path inside StudentFiles folder
        log_file_path = os.path.join(folder_path, "activity_log.txt")

        # Get current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Format the log entry
        log_entry = f"[{timestamp}] {file_name} {action} successfully.\n"

        # Append to the log file (creates file if it doesn't exist)
        with open(log_file_path, "a") as log_file:
            log_file.write(log_entry)

        print(f"Activity logged to {log_file_path}")
        return True

    except IOError as e:
        print(f"Error: Failed to write to log file. Reason: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred during logging: {e}")
        return False


def read_log(folder_path):
    """
    Read and display the contents of the activity log file.

    Args:
        folder_path (str): The path to the StudentFiles folder

    Returns:
        str: The contents of the log file, or None if file doesn't exist
    """
    try:
        log_file_path = os.path.join(folder_path, "activity_log.txt")

        if not os.path.exists(log_file_path):
            print("No log file found.")
            return None

        with open(log_file_path, "r") as log_file:
            contents = log_file.read()

        return contents

    except IOError as e:
        # --- ADD THESE LINES (Task 5c) ---
        error_message = f"Failed to read log file. Reason: {e}"
        print(f"Error: {error_message}")
        # Can't log to the file if we can't read it, but we print.
        return None
        
    except Exception as e:
        # --- ADD THESE LINES (Task 5c) ---
        error_message = f"An unexpected error occurred while reading log: {e}"
        print(f"An unexpected error occurred: {e}")
        # Try to log this, though it might fail if it's an IOError
        log_activity(folder_path, "activity_log.txt", action=f"Error - {error_message}")
        return None
