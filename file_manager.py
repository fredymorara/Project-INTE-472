import os
import sys
from datetime import datetime
import shutil  # <-- ADD THIS LINE
from logger import log_activity, read_log
from delete_file import delete_file_prompt, list_files


def initialize_project():
    """Initialize the StudentFiles folder."""
    print("--- Task 1: Initializing Project ---")
    folder_name = "StudentFiles"

    try:
        # a) Check if the folder exists
        if not os.path.exists(folder_name):
            # b) If not, create it
            os.makedirs(folder_name)
            print(f"Folder '{folder_name}' created.")
        else:
            print(f"Folder '{folder_name}' already exists.")

        # c) Display the absolute path
        folder_path = os.path.abspath(folder_name)
        print(f"Absolute path: {folder_path}")

        return folder_path

    except OSError as e:
        # d) Handle exceptions and terminate
        print(f"Error: Failed to create folder '{folder_name}'. Reason: {e}")
        sys.exit("Program terminated due to folder creation failure.")


def create_records_file(folder_path):
    """Create a new records file with student names."""
    print("\n--- Task 2: Creating and Writing to File ---")
    file_name = "" # Define file_name here to be accessible in except block
    try:
        # a) Generate file name with current date
        current_date = datetime.now().strftime("%Y-%m-%d")
        file_name = f"records_{current_date}.txt"

        # c) Create the full path to save the file inside StudentFiles
        file_path = os.path.join(folder_path, file_name)

        print(f"Creating file: {file_name}. Please enter 5 student names.")

        # b) Prompt user for names and write to file
        with open(file_path, "w") as f:
            for i in range(5):
                name = input(f"Enter name {i+1}/5: ")
                f.write(name + "\n")  # Write one name per line

        # d) Display success message with timestamp
        creation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(
            f"\nSuccess: File '{file_name}' created in 'StudentFiles' at {creation_time}."
        )

        # --- THIS IS WHERE PERSON 2's CODE WILL GO (Task 4) ---
        # --- (e.g., backup_and_archive(folder_path, file_path, file_name)) ---
        
        # --- ADD THIS LINE (Task 4) ---
        backup_and_archive(folder_path, file_path, file_name)
        # ---------------------------------

        # Log the activity (Task 5)
        # This log message is now accurate.
        log_activity(folder_path, file_name, action="created and archived")

    except IOError as e:
        error_message = f"Failed to write to file '{file_name}'. Reason: {e}"
        print(f"Error: {error_message}")
        # --- ADD THIS LINE (Task 5c) ---
        log_activity(folder_path, file_name if file_name else "unknown_file", action=f"Error - {error_message}")
        print("Returning to main menu...")
    except Exception as e:
        error_message = f"An unexpected error occurred. Reason: {e}"
        print(error_message)
        # --- ADD THIS LINE (Task 5c) ---
        log_activity(folder_path, "system", action=f"Error - {error_message}")
        print("Returning to main menu...")


def backup_and_archive(folder_path, file_path, file_name):
    """
    Create a backup and move it to the Archive folder (Task 4).
    
    Args:
        folder_path (str): Path to StudentFiles
        file_path (str): Full path to the original file
        file_name (str): Name of the original file
    """
    print(f"--- Task 4: Backing up '{file_name}' ---")
    try:
        # b) Create Archive subfolder if it doesn't exist
        archive_folder_path = os.path.join(folder_path, "Archive")
        if not os.path.exists(archive_folder_path):
            os.makedirs(archive_folder_path)
            print(f"Subfolder 'Archive' created.")

        # a) Create backup copy name and path
        backup_file_name = f"backup_{file_name}"
        backup_file_path = os.path.join(folder_path, backup_file_name)
        
        # Create the copy
        shutil.copy(file_path, backup_file_path)
        print(f"Backup copy '{backup_file_name}' created.")

        # c) Move backup file into Archive folder
        # shutil.move() can overwrite. We'll move to the full destination path.
        final_backup_path = os.path.join(archive_folder_path, backup_file_name)
        shutil.move(backup_file_path, final_backup_path)
        print(f"Backup moved to 'Archive' folder.")

        # d) List all files in the Archive folder
        print("\nFiles now in Archive folder:")
        archive_files = os.listdir(archive_folder_path)
        if not archive_files:
            print("Archive folder is empty.")
        else:
            for file in archive_files:
                print(f"- {file}")

    except (shutil.Error, OSError) as e:
        error_message = f"Backup/Archive failed for '{file_name}'. Reason: {e}"
        print(f"Error: {error_message}")
        # Log this error (Task 5c)
        log_activity(folder_path, file_name, action=f"Error - {error_message}")


def view_files(folder_path):
    """View all files in the StudentFiles folder."""
    print("\n--- View Files ---")
    files = list_files(folder_path)

    if not files:
        print("No files found in the StudentFiles folder.")
    else:
        print(f"\nFiles in StudentFiles folder ({len(files)} total):")
        for idx, file in enumerate(files, 1):
            file_path = os.path.join(folder_path, file)
            
            # Task 3b: Get file size
            file_size = os.path.getsize(file_path)
            
            # --- START: Added code for Task 3c ---
            mod_time_stamp = os.path.getmtime(file_path)
            mod_time = datetime.fromtimestamp(mod_time_stamp).strftime('%Y-%m-%d %H:%M:%S')
            
            print(f"{idx}. {file} ({file_size} bytes, Last Modified: {mod_time})")
            # --- END: Added code for Task 3c ---


def view_file_contents(folder_path):
    """Read and display the contents of a specific file (Task 3a)."""
    print("\n--- View File Contents ---")
    files = list_files(folder_path)

    if not files:
        print("No files found in the StudentFiles folder.")
        return

    print("Which file would you like to view?")
    for idx, file in enumerate(files, 1):
        print(f"{idx}. {file}")
    
    try:
        # Ask user for a number
        choice_str = input(f"Enter file number (1-{len(files)}): ").strip()
        
        if not choice_str.isdigit():
            print("Invalid input. Please enter a number.")
            return

        choice = int(choice_str)
        if not 1 <= choice <= len(files):
            print("Invalid choice. Number out of range.")
            return
            
        file_name = files[choice - 1]
        file_path = os.path.join(folder_path, file_name)

        print(f"\n--- Contents of {file_name} ---")
        with open(file_path, "r") as f:
            print(f.read())
        print("--- End of File ---")

    except (ValueError, IndexError):
        print("Invalid input. Please enter a number from the list.")
    except IOError as e:
        error_message = f"Failed to read file '{file_name}'. Reason: {e}"
        print(f"Error: {error_message}")
        log_activity(folder_path, file_name, action=f"Error - {error_message}")


def view_activity_log(folder_path):
    """View the activity log."""
    print("\n--- Activity Log ---")
    log_contents = read_log(folder_path)

    if log_contents:
        print(log_contents)
    else:
        print("No activity log found or log is empty.")


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 60)
    print("         STUDENT FILES MANAGEMENT SYSTEM")
    print("=" * 60)
    print("1. Create new records file")
    print("2. Delete a file")
    print("3. View all files")
    print("4. View activity log")
    print("5. View file contents") # <-- ADDED THIS OPTION
    print("6. Exit")               # <-- CHANGED 5 to 6
    print("=" * 60)


def main():
    """Main program loop."""
    # Initialize the project folder
    folder_path = initialize_project()
    folder_name = "StudentFiles"

    # Main menu loop
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ").strip() # <-- CHANGED 1-5 to 1-6

        if choice == "1":
            create_records_file(folder_path)

        elif choice == "2":
            delete_file_prompt(folder_path)

        elif choice == "3":
            view_files(folder_path)

        elif choice == "4":
            view_activity_log(folder_path)

        # --- ADD THIS ELIF BLOCK ---
        elif choice == "5":
            view_file_contents(folder_path)
        # ---------------------------

        elif choice == "6": # <-- CHANGED 5 to 6
            # extra
            print("\nThank you for using Student Files Management System!")
            print("Goodbye!")
            sys.exit(0)

        else:
            print("\nInvalid choice! Please enter a number between 1 and 6.") # <-- CHANGED 1-5 to 1-6


# Run the main program
if __name__ == "__main__":
    main()

# --- Tasks 4, 5, 6 will be added below by other team members ---
# They will need the 'file_path' and 'folder_path' variables.
