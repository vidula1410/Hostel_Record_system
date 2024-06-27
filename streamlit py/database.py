# database.py

import mysql.connector
import pymysql
import streamlit as st

def create_tables():
    # Assuming you have a MySQL connection
    connection = pymysql.connect(
            host="localhost",
            user="root",
            password="idonothaveapassword",
            database="college_management_system"
        )

    cursor = connection.cursor()

    # Create the Student table
    create_student_table_query = """
    CREATE TABLE IF NOT EXISTS Student (
        Student_ID INT AUTO_INCREMENT PRIMARY KEY,
        First_Name VARCHAR(50) NOT NULL,
        Last_Name VARCHAR(50) NOT NULL,
        Date_of_Birth DATE,
        Email VARCHAR(100) UNIQUE NOT NULL,
        Phone_Number VARCHAR(20),
        Address VARCHAR(255)
    )
    """
    cursor.execute(create_student_table_query)

    # Create the Faculty table
    create_faculty_table_query = """
    CREATE TABLE IF NOT EXISTS Faculty (
        Faculty_ID INT AUTO_INCREMENT PRIMARY KEY,
        First_Name VARCHAR(50) NOT NULL,
        Last_Name VARCHAR(50) NOT NULL,
        Date_of_Birth DATE,
        Email VARCHAR(100) UNIQUE NOT NULL,
        Phone_Number VARCHAR(20),
        Qualifications VARCHAR(255)
    )
    """
    cursor.execute(create_faculty_table_query)

    # Create the Mess table
    create_course_table_query = """
    CREATE TABLE IF NOT EXISTS Enrollment (
        Enrollment_ID INT AUTO_INCREMENT PRIMARY KEY,
        Student_ID INT,
        Mess_ID INT,
        Mess_name ENUM('Vakula','Food Court'),
        FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID),
        CONSTRAINT chk_mess_id CHECK (
        (Mess_name = 'Vakula' AND Mess_ID = 1) OR
        (Mess_name = 'Food Court' AND Mess_ID = 2) )
    )
    """
    cursor.execute(create_course_table_query)

    # Create the Report table
    create_report_table_query = """
    CREATE TABLE IF NOT EXISTS Report (
        Report_ID INT AUTO_INCREMENT PRIMARY KEY,
        Report_Name VARCHAR(100) NOT NULL,
        marks int,
        Generation_Date DATE,
        faculty_id INT,
        student_id INT,
        FOREIGN KEY (faculty_id) REFERENCES Faculty(faculty_id),
        FOREIGN KEY (student_id) REFERENCES Student(student_id)
    )
    """
    cursor.execute(create_report_table_query)

    
    create_enrollment_log_table_query = """
    CREATE TABLE IF NOT EXISTS Enrollment_Log (
        Log_ID INT AUTO_INCREMENT PRIMARY KEY,
        Student_ID INT,
        Enrollment_Date TIMESTAMP,
        Log_Description VARCHAR(255),
        FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID)
    )
    """
    cursor.execute(create_enrollment_log_table_query)

    create_admi_table_query = """
    CREATE TABLE IF NOT EXISTS admi (
     Student_ID int,
     Faculty_ID int,
     FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID),
	 FOREIGN KEY (Faculty_ID) REFERENCES Faculty(Faculty_ID)
    )
    """

    cursor.execute(create_admi_table_query)
     

    connection.commit()

    st.success("Tables created successfully!")

    # Close the database connection
    cursor.close()
    connection.close()
