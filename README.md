# Python File Management and Data Processing Utility

 A group project for **Kabarak University**, Department of Computer Science/Information Technology[cite: 1, 2].
 **Course:** INTE 472: Scripting Languages [cite: 3]

---

## 📋 Project Overview

 This utility is designed to assist users in automatically creating, backing up, organizing, logging, and analyzing data files using Python[cite: 6].  The project demonstrates file handling integrated with system utilities [cite: 7]  and is submitted as part of the coursework (30 marks)[cite: 4].

## ✨ Features

This project is divided into two main scripts:

### 1. `file_manager.py` (Main Utility)
*  **Project Initialization:** Automatically checks for and creates a `StudentFiles` directory on startup[cite: 20, 21].
*  **File Creation:** Generates a text file named with the current date (e.g., `records_2025-10-31.txt`) [cite: 27]  and populates it with 5 student names provided by the user[cite: 28].
*  **File Information:** Reads a file's contents [cite: 33]  and displays its metadata, including file size (bytes) [cite: 34]  and last modified date[cite: 35].
*  **Backup & Archiving:** Creates backup copies using `shutil.copy()` [cite: 37]  and moves them to a dedicated `Archive` subfolder[cite: 39, 40].
*  **Activity Logging:** Maintains a central log file (`activity_log.txt`) [cite: 43]  with timestamps for all successful operations [cite: 45]  and any errors encountered[cite: 49].
*  **File Management:** Provides a user-prompted option to delete files from the `StudentFiles` directory [cite: 51, 52]  and logs the deletion[cite: 53].

### 2. `students_report.py` (Data Processing)
*  **Data Ingestion:** Reads student data from a `students.json` file[cite: 57].
*  **Data Processing:** Computes the average score for each student, rounded to two decimal places[cite: 61].
*  **Report Generation:** Writes the results (`id`, `name`, `average`) [cite: 63]  into a `report.csv` file[cite: 62].
*  **Sorting:** Sorts the data in the CSV file by average score in descending order[cite: 64].
*  **Error Handling:** Includes error handling to display an informative message if `students.json` is missing, preventing a crash[cite: 65, 66].

---

## ️ Technologies Used

This project utilizes the following standard Python modules as required:
*  `os` [cite: 8]
*  `sys` [cite: 9]
*  `shutil` [cite: 10]
*  `datetime` [cite: 11]
*  `json` [cite: 12]
*  `csv` [cite: 13]

---

## 📂 Repository Structure

 As required for submission[cite: 68], this repository contains:
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
*(As required for Moodle submission [cite: 16, 74])*

| Name | Registration Number | GitHub Profile |
| :--- | :--- | :--- |
| Cleophas Kiama | INTE/MG/2834/09/22 | [@CleoKiama](https://github.com/CleoKiama) |
| Morris Mwangi | INTE/MG/----/09/22 | [Link to GitHub 3] |
| David Koroso | INTE/MG/----/09/22 | [Link to GitHub 3] |
| Fredrick M. Morara | INTE/MG/2814/09/22 | [@fredymorara](https://github.com/fredymorara) |