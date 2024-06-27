# read.py

import streamlit as st
import mysql.connector
import pymysql

def read_students(student_id=None):
    st.subheader("View Students")

    # Assuming you have a MySQL connection
    connection = pymysql.connect(
            host="localhost",
            user="root",
            password="idonothaveapassword",
            database="college_management_system"
        )

    cursor = connection.cursor()

    # Retrieve students from the database
    if student_id:
        query = "SELECT * FROM Student WHERE Student_ID = %s"
        cursor.execute(query, (student_id,))
    else:
        query = "SELECT * FROM Student"
        cursor.execute(query)

    students = cursor.fetchall()

    if not students:
        st.warning("No students found.")
    else:
        st.table(students)

    # Close the database connection
    cursor.close()
    connection.close()


def read_faculties(faculty_id=None):
    st.subheader("View Faculties")

    # Assuming you have a MySQL connection
    connection = pymysql.connect(
            host="localhost",
            user="root",
            password="idonothaveapassword",
            database="college_management_system"
        )

    cursor = connection.cursor()

    # Retrieve faculties from the database
    if faculty_id:
        query = "SELECT * FROM Faculty WHERE Faculty_ID = %s"
        cursor.execute(query, (faculty_id,))
    else:
        query = "SELECT * FROM Faculty"
        cursor.execute(query)

    faculties = cursor.fetchall()

    if not faculties:
        st.warning("No faculties found.")
    else:
        st.table(faculties)

    # Close the database connection
    cursor.close()
    connection.close()


def display_reports():
    try:
        # Connect to the database
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="idonothaveapassword",
            database="college_management_system"
        )

        cursor = connection.cursor(dictionary=True)

        # Fetch all reports from the database
        report_query = "SELECT * FROM Report"
        cursor.execute(report_query)
        reports = cursor.fetchall()

        if reports:
            st.subheader("Reports for All Students:")
            for report in reports:
                st.write(f"Report ID: {report['Report_ID']}")
                st.write(f"Student Id: {report['Student_ID']}")
                st.write(f"Report Name: {report['Report_Name']}")
                st.write(f"Marks: {report['marks']}")
                st.write(f"Generation Date: {report['Generation_Date']}")
                st.write("---")

        if not reports:
            st.warning("No reports found for any student.")

    except Exception as e:
        st.error(f"An error occurred: {e}")

    finally:
        # Ensure that the database connection is properly closed
        try:
            cursor.close()
            connection.close()
        except Exception as e:
            st.error(f"An error occurred while closing the connection: {e}")


def display_reports_for_student(student_id):
    try:
        # Connect to the database
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="idonothaveapassword",
            database="college_management_system"
        )

        cursor = connection.cursor(dictionary=True)

        # Fetch reports for the specified student_id from the database
        report_query = "SELECT * FROM Report WHERE Student_ID = %s"
        cursor.execute(report_query, (student_id,))
        reports = cursor.fetchall()

        if reports:
            st.subheader(f"Reports for Student ID {student_id}:")
            for report in reports:
                st.write(f"Report ID: {report['Report_ID']}")
                st.write(f"Student Id: {report['Student_ID']}")
                st.write(f"Report Name: {report['Report_Name']}")
                st.write(f"Marks: {report['marks']}")
                st.write(f"Generation Date: {report['Generation_Date']}")
                st.write("---")

        if not reports:
            st.warning(f"No reports found for Student ID {student_id}.")

    except Exception as e:
        st.error(f"An error occurred: {e}")

    finally:
        # Ensure that the database connection is properly closed
        try:
            cursor.close()
            connection.close()
        except Exception as e:
            st.error(f"An error occurred while closing the connection: {e}")





def get_student_courses(student_id):
    try:
        # Connect to the database
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="idonothaveapassword",
            database="college_management_system",
        )

        cursor = connection.cursor()

        # Query the Enrollment table to get the courses for the student
        query = "SELECT Mess_Name FROM Enrollment WHERE Student_ID = %s ORDER BY Enrollment_ID DESC LIMIT 1"
        cursor.execute(query, (student_id,))
        courses = cursor.fetchone()

        if courses is not None:
            st.subheader(f"Messes Enrolled by Student ID {student_id}:")
            st.write(f"Mess Name: {courses[0]}")
        else:
            st.warning(f"No messes found for Student ID {student_id}.")

    except Exception as e:
        st.error(f"An error occurred: {e}")

    finally:
        # Ensure that the database connection is properly closed
        try:
            cursor.close()
            connection.close()
        except Exception as e:
            st.error(f"An error occurred while closing the connection: {e}")
