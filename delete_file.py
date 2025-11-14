"""
Delete File Module
This module provides functionality to delete files from the StudentFiles folder.
"""

import os
from logger import log_activity


def delete_file_prompt(folder_path):
    """
    Prompt user to delete a file from the StudentFiles folder.

    Args:
        folder_path (str): The path to the StudentFiles folder

    Returns:
        bool: True if a file was deleted, False otherwise
    """
    print("\n--- File Deletion Module ---")

    # a) Ask the user if they would like to delete a file
    user_response = input(
        "Would you like to delete a file from the StudentFiles folder? (Yes/No): "
    ).strip()

    # b) If the user types "Yes", ask for the file name and delete it
    if user_response.lower() == "yes":
        # Show available files first
        print("\nAvailable files in StudentFiles folder:")
        try:
            files = os.listdir(folder_path)
            if not files:
                print("No files found in the folder.")
                return False

            for idx, file in enumerate(files, 1):
                print(f"{idx}. {file}")
        except OSError as e:
            error_message = f"Unable to list files. Reason: {e}"
            print(f"Error: {error_message}")
            # --- ADD THIS LINE (Task 5c) ---
            log_activity(folder_path, "system", action=f"Error - {error_message}")
            return False

        # Ask for file name
        file_name = input("\nEnter the name of the file to delete: ").strip()
        file_path = os.path.join(folder_path, file_name)

        # Check if file exists
        if not os.path.exists(file_path):
            print(
                f"Error: File '{file_name}' does not exist in the StudentFiles folder."
            )
            return False

        # Confirm deletion
        confirm = input(
            f"Are you sure you want to delete '{file_name}'? (Yes/No): "
        ).strip()
        if confirm.lower() != "yes":
            print("Deletion cancelled.")
            return False

        # Delete the file
        try:
            os.remove(file_path)
            print(f"\nSuccess: File '{file_name}' has been deleted.")

            # c) Log the deletion event [cite: 53]
            log_activity(folder_path, file_name, action="deleted")

            # d) Display all remaining files [cite: 54]
            print("\n--- Remaining Files in StudentFiles Folder ---")
            remaining_files = os.listdir(folder_path)
            if remaining_files:
                for idx, file in enumerate(remaining_files, 1):
                    print(f"{idx}. {file}")
            else:
                print("No files remaining in the folder.")

            return True

        except OSError as e:
            error_message = f"Failed to delete file '{file_name}'. Reason: {e}"
            print(f"Error: {error_message}")
            # --- ADD THIS LINE (Task 5c) ---
            log_activity(folder_path, file_name, action=f"Error - {error_message}")
            return False
        except Exception as e:
            error_message = f"An unexpected error occurred. Reason: {e}"
            print(f"An unexpected error occurred: {e}")
            # --- ADD THIS LINE (Task 5c) ---
            log_activity(folder_path, file_name, action=f"Error - {error_message}")
            return False
    else:
        print("File deletion skipped.")
        return False


def delete_specific_file(folder_path, file_name):
    """
    Delete a specific file without user prompts (for programmatic use).

    Args:
        folder_path (str): The path to the StudentFiles folder
        file_name (str): The name of the file to delete

    Returns:
        bool: True if file was deleted successfully, False otherwise
    """
    file_path = os.path.join(folder_path, file_name)

    if not os.path.exists(file_path):
        print(f"Error: File '{file_name}' does not exist.")
        return False

    try:
        os.remove(file_path)
        print(f"File '{file_name}' deleted successfully.")

        # Log the deletion
        log_activity(folder_path, file_name, action="deleted")

        return True

    except OSError as e:
        # --- ADD THESE LINES (Task 5c) ---
        error_message = f"Failed to delete file '{file_name}'. Reason: {e}"
        print(f"Error: {error_message}")
        log_activity(folder_path, file_name, action=f"Error - {error_message}")
        return False
        
    except Exception as e:
        # --- ADD THESE LINES (Task 5c) ---
        error_message = f"An unexpected error occurred. Reason: {e}"
        print(f"An unexpected error occurred: {e}")
        log_activity(folder_path, file_name, action=f"Error - {error_message}")
        return False


def list_files(folder_path):
    """
    List all files in the StudentFiles folder.
    ...
    """
    try:
        files = os.listdir(folder_path)
        return files
    except OSError as e:
        error_message = f"Unable to list files. Reason: {e}"
        print(f"Error: {error_message}")
        # --- ADD THIS LINE (Task 5c) ---
        # Note: We can't log if the folder_path itself is the problem,
        # but we try anyway.
        log_activity(folder_path, "system", action=f"Error - {error_message}")
        return []