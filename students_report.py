# File: students_report.py

"""
Student Report Generator (Project Task 7)

Reads student data from students.json, calculates average scores,
and writes a sorted report to report.csv.
"""

import json
import csv
import sys

def generate_student_report():
    """
    Reads students.json, computes average scores, and saves to report.csv.
    """
    json_filename = "students.json"
    csv_filename = "report.csv"
    
    # --- Task 7d: Error handling for missing file ---
    try:
        # --- Task 7a: Read a JSON file ---
        with open(json_filename, "r") as f:
            students_data = json.load(f)
            
    except FileNotFoundError:
        print(f"Error: The file '{json_filename}' was not found.")
        print("Please make sure 'students.json' is in the same directory.")
        sys.exit(1) # Exit the script
    except json.JSONDecodeError:
        print(f"Error: Failed to decode '{json_filename}'. Please check file format.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        sys.exit(1)

    processed_data = []

    # --- Task 7b: Compute each student's average score ---
    for student in students_data:
        try:
            student_id = student.get("id")
            name = student.get("name")
            scores = student.get("scores", [])
            
            if not scores:
                average = 0.0
            else:
                average = sum(scores) / len(scores)
                
            # Round to two decimal places
            average = round(average, 2)
                
            processed_data.append({
                "id": student_id,
                "name": name,
                "average": average
            })
        except (TypeError, AttributeError, ValueError) as e:
            # Handle potential bad data inside the json file
            print(f"Warning: Skipping invalid student record: {student}. Reason: {e}")

    # --- Task 7c: Sort the data by average (descending order) ---
    try:
        # Sorts the list of dictionaries by the 'average' key, high to low
        processed_data.sort(key=lambda x: x["average"], reverse=True)
    except TypeError as e:
        print(f"Error: Could not sort data, check for invalid average scores. {e}")
        # Continue without sorting if it fails
    
    # --- Task 7c: Write the results into a CSV file ---
    try:
        # Define the column headers
        fieldnames = ["id", "name", "average"]
        
        with open(csv_filename, "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(processed_data)
            
        print(f"\nSuccessfully generated '{csv_filename}'.")

    except IOError as e:
        print(f"Error: Could not write to '{csv_filename}'. Reason: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred while writing the CSV: {e}")
        sys.exit(1)


# Run the script
if __name__ == "__main__":
    print("--- Student Data Processing Utility (Task 7) ---")
    generate_student_report()
