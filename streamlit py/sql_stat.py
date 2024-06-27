# sql_stat.py

import streamlit as st
import mysql.connector
import pymysql

def stat():
    st.subheader("College Management System Statistics")

    # Assuming you have a MySQL connection
    connection = pymysql.connect(
            host="localhost",
            user="root",
            password="idonothaveapassword",
            database="college_management_system"
        )

    cursor = connection.cursor()

    # Count the number of students
    student_count_query = "SELECT COUNT(*) FROM Student"
    cursor.execute(student_count_query)
    student_count = cursor.fetchone()[0]

    # Count the number of faculties
    faculty_count_query = "SELECT COUNT(*) FROM Faculty"
    cursor.execute(faculty_count_query)
    faculty_count = cursor.fetchone()[0]

    # Count the number of students in Vakula
    CSE_count_query = "SELECT COUNT(*) FROM Student s JOIN Enrollment e ON s.Student_ID=e.Student_ID WHERE Mess_name='Vakula'"
    cursor.execute(CSE_count_query)
    CSE_count = cursor.fetchone()[0]

    # Count the number of students in Vakula whose phone number is valid
    Valid_Phone_query = "SELECT COUNT(*) AS StudentCount FROM Enrollment e JOIN Student s ON e.Student_ID = s.Student_ID WHERE s.Phone_Number IS NOT NULL AND s.Phone_Number != '' GROUP BY Mess_name"
    cursor.execute(Valid_Phone_query)
    Valid_Phone = cursor.fetchone()[0]

    # Name of students in Vakula whose phone number is valid
    Valid_Phone_Name_query = "SELECT First_Name, Last_Name FROM Student WHERE Student_ID IN (SELECT Student_ID FROM Enrollment  WHERE Mess_name = 'Vakula') AND Phone_Number IS NOT NULL AND Phone_Number != ''"
    cursor.execute(Valid_Phone_Name_query)
    Valid_Phone_Name = cursor.fetchone()

    # Display the statistics
    st.write(f"Number of Students: {student_count}")

    st.write(f"Number of Faculties: {faculty_count}")

    st.write(f"Number of Students in Vakula: {CSE_count}")

    st.write(f"Number of Students in Vakula with a Valid Phone Number: {Valid_Phone}")


    if Valid_Phone_Name:
        st.write("Name of First Student in Vakula with a Valid Phone Number:")
        first_name, last_name = Valid_Phone_Name
        st.write(f"{first_name} {last_name}")
    else:
        st.write("No students found in Vakula with a valid phone number.")

    

    # Close the database connection
    cursor.close()
    connection.close()
