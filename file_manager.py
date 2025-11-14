import os
import sys
from datetime import datetime
from logger import log_activity

# --- TASK 1: Project Initialization  ---
print("--- Task 1: Initializing Project ---")
folder_name = "StudentFiles"
folder_path = ""  # Initialize to be used in Task 2

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

except OSError as e:
    # d) Handle exceptions and terminate
    print(f"Error: Failed to create folder '{folder_name}'. Reason: {e}")
    sys.exit("Program terminated due to folder creation failure.")  #


# --- TASK 2: File Creation and Writing  ---
print("\n--- Task 2: Creating and Writing to File ---")
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
        f"\nSuccess: File '{file_name}' created in '{folder_name}' at {creation_time}."
    )

    # Log the activity
    log_activity(folder_path, file_name)

except IOError as e:
    print(f"Error: Failed to write to file '{file_name}'. Reason: {e}")
    # Note: Person 3 will be responsible for logging this error
    sys.exit("Program terminated due to file writing failure.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit("Program terminated.")

print("\n--- Tasks 1 & 2 Completed ---")

# --- Tasks 3, 4, 5, 6 will be added below by other team members ---
# They will need the 'file_path' and 'folder_path' variables.
