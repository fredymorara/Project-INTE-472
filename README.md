# Python File Management and Data Processing Utility

 A group project for **Kabarak University**, Department of Computer Science/Information Technology.
 **Course:** INTE 472: Scripting Languages 

---

## 📋 Project Overview

 This utility is designed to assist users in automatically creating, backing up, organizing, logging, and analyzing data files using Python.  The project demonstrates file handling integrated with system utilities   and is submitted as part of the coursework (30 marks).

## ✨ Features

This project is divided into two main scripts:

### 1. `file_manager.py` (Main Utility)
*  **Project Initialization:** Automatically checks for and creates a `StudentFiles` directory on startup.
*  **File Creation:** Generates a text file named with the current date (e.g., `records_2025-10-31.txt`)   and populates it with 5 student names provided by the user.
*  **File Information:** Reads a file's contents   and displays its metadata, including file size (bytes)   and last modified date.
*  **Backup & Archiving:** Creates backup copies using `shutil.copy()`   and moves them to a dedicated `Archive` subfolder.
*  **Activity Logging:** Maintains a central log file (`activity_log.txt`)   with timestamps for all successful operations   and any errors encountered.
*  **File Management:** Provides a user-prompted option to delete files from the `StudentFiles` directory   and logs the deletion.

### 2. `students_report.py` (Data Processing)
*  **Data Ingestion:** Reads student data from a `students.json` file.
*  **Data Processing:** Computes the average score for each student, rounded to two decimal places.
*  **Report Generation:** Writes the results (`id`, `name`, `average`)   into a `report.csv` file.
*  **Sorting:** Sorts the data in the CSV file by average score in descending order.
*  **Error Handling:** Includes error handling to display an informative message if `students.json` is missing, preventing a crash.

---

## ️ Technologies Used

This project utilizes the following standard Python modules as required:
*  `os` 
*  `sys` 
*  `shutil` 
*  `datetime` 
*  `json` 
*  `csv` 

---

## 📂 Repository Structure

 As required for submission, this repository contains:
. ├── file_manager.py # The main utility script ├── students_report.py # The data processing script ├── students.json # Sample JSON data for testing └── README.md # This project description file 





---

## 🚀 How to Run

### Main Utility
1.  Ensure you are in the project's root directory.
2.  Run the script:
    ```bash
    python file_manager.py
    ```
3.  Follow the on-screen prompts to create files and enter names.

### Data Processing Script
1.  Ensure the `students.json` file is in the same directory.
2.  Run the script:
    ```bash
    python students_report.py
    ```
3.  A `report.csv` file will be generated with the processed data.

---

## 👥 Team Members

This project was a collaborative effort by the following team members.

| Name | Registration Number | GitHub Profile |
| :--- | :--- | :--- |
| Cleophas Kiama | INTE/MG/2834/09/22 | [@CleoKiama](https://github.com/CleoKiama) |
| Morris Mwangi | INTE/MG/----/09/22 | [Link to GitHub 3] |
| David Koroso | INTE/MG/----/09/22 | [Link to GitHub 3] |
| Fredrick M. Morara | INTE/MG/2814/09/22 | [@fredymorara](https://github.com/fredymorara) |