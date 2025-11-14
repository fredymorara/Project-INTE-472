import os
import sys
from datetime import datetime
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
        # (e.g., backup_and_archive(folder_path, file_path, file_name))
        # --------------------------------------------------------


        # Log the activity (Task 5)
        # This log message assumes Person 2 has added the backup/archive code above.
        # This correctly logs "created and archived" as required[cite: 46].
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
            file_size = os.path.getsize(file_path)
            print(f"{idx}. {file} ({file_size} bytes)")


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
    print("5. Exit")
    print("=" * 60)


def main():
    """Main program loop."""
    # Initialize the project folder
    folder_path = initialize_project()
    folder_name = "StudentFiles"

    # Main menu loop
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            create_records_file(folder_path)

        elif choice == "2":
            delete_file_prompt(folder_path)

        elif choice == "3":
            view_files(folder_path)

        elif choice == "4":
            view_activity_log(folder_path)

        elif choice == "5":
            # extra
            print("\nThank you for using Student Files Management System!")
            print("Goodbye!")
            sys.exit(0)

        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.")


# Run the main program
if __name__ == "__main__":
    main()

# --- Tasks 4, 5, 6 will be added below by other team members ---
# They will need the 'file_path' and 'folder_path' variables.
