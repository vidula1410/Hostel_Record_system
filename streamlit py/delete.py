# delete.py

import streamlit as st
import mysql.connector
import pymysql

def delete_student():
    st.subheader("Delete Student")

    student_id = st.text_input("Enter Student ID to delete:")

    if st.button("Delete Student"):
        # Assuming you have a MySQL connection
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="idonothaveapassword",
            database="college_management_system"
        )

        cursor = connection.cursor()

        # Delete the student from the database
        delete_query = "DELETE FROM Student WHERE Student_ID = %s"
        data = (student_id,)

        cursor.execute(delete_query, data)
        connection.commit()

        if cursor.rowcount > 0:
            st.success("Student deleted successfully!")
        else:
            st.warning("No student found with the given ID.")

        # Close the database connection
        cursor.close()
        connection.close()

def delete_faculty():
    st.subheader("Delete Faculty")

    faculty_id = st.text_input("Enter Faculty ID to delete:")

    if st.button("Delete Faculty"):
        # Assuming you have a MySQL connection
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="idonothaveapassword",
            database="college_management_system"
        )

        cursor = connection.cursor()

        # Delete the faculty from the database
        delete_query = "DELETE FROM Faculty WHERE Faculty_ID = %s"
        data = (faculty_id,)

        cursor.execute(delete_query, data)
        connection.commit()

        if cursor.rowcount > 0:
            st.success("Faculty deleted successfully!")
        else:
            st.warning("No faculty found with the given ID.")

        # Close the database connection
        cursor.close()
        connection.close()
