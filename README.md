# Student Data Management System (LOC)

A command-line interface (CLI) application built with Python and MySQL to manage Student List of Candidates (LOC) data. This system allows administrators to perform CRUD (Create, Read, Update, Delete) operations on student records securely.

##  Features

* *User Authentication:* Secure login system to access the dashboard.
* *Insert Record (I):* Add detailed student information (Personal details, Marks, Subjects, etc.).
* *Update Record (U):* Modify existing student details (Name, Parent's Name).
* *Remove Record (R):* Delete a student's record permanently.
* *Search Record (S):* Find specific student details using their Registration Number.
* *Display All (D):* View a summarized list of all students in the database.
* *Database Automation:* Automatically creates the LOC database and required tables if they do not exist.

##  Prerequisites

Before running the script, ensure you have the following installed:

1.  *Python 3.x*
2.  *MySQL Server*
3.  *MySQL Connector for Python*

##  Installation

1.  *Install the MySQL connector library:*
    Open your terminal or command prompt and run:
    bash
    pip install mysql-connector-python
    

2.  *Database Setup:*
    * Ensure your MySQL server is running.
    * Open the Python script and check the connection line at the top:
        python
        con = mcon.connect(host="localhost", port="3306", user="root", passwd="root")
        
    * *Important:* Update user and passwd to match your local MySQL credentials.

##  How to Run

1.  Navigate to the folder containing the script.
2.  Run the file using Python:
    bash
    python your_script_name.py
    
3.  *First Time Login:*
    * The system requires a user in the user table to log in.
    * By default, the script checks for a user with active status ('A').
    * Note: You may need to manually insert a user into the database or uncomment the user insertion lines in the code for the first run.

##  Usage Guide

Once logged in, follow the on-screen menu:

* **Enter I**: To register a new student (You will be prompted for registration number, names, marks, etc.).
* **Enter U**: To fix typos in names or update parent details.
* **Enter R**: To delete a student who has left.
* **Enter S**: To see full details of a specific student.
* **Enter D**: To see a tabular view of all students.
* **Enter E**: To exit the program.

##  Database Schema

The system uses a database named LOC with two main tables:
1.  **user**: Stores login credentials (uname, upwd, utype, ustatus).
2.  **students**: Stores comprehensive student data (reg_num, cand_name, marks, etc.).

---
