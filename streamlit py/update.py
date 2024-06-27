# update.py

import streamlit as st
import mysql.connector
import pymysql

def update_student():
    st.subheader("Update Student Information")

    student_id = st.text_input("Enter Student ID to update:")
    new_email = st.text_input("Enter New Email:")
    new_phone_number = st.text_input("Enter New Phone Number:")

    if st.button("Update Student"):
        # Assuming you have a MySQL connection
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="idonothaveapassword",
            database="college_management_system"
        )

        cursor = connection.cursor()

        # Update student information in the database
        update_query = "UPDATE Student SET Email = %s, Phone_Number = %s WHERE Student_ID = %s"
        data = (new_email, new_phone_number, student_id)

        cursor.execute(update_query, data)
        connection.commit()

        if cursor.rowcount > 0:
            st.success("Student information updated successfully!")
        else:
            st.warning("No student found with the given ID.")

        # Close the database connection
        cursor.close()
        connection.close()

def update_faculty():
    st.subheader("Update Faculty Information")

    faculty_id = st.text_input("Enter Faculty ID to update:")
    new_email = st.text_input("Enter New Email:")
    new_phone_number = st.text_input("Enter New Phone Number:")

    if st.button("Update Faculty"):
        # Assuming you have a MySQL connection
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="idonothaveapassword",
            database="college_management_system"
        )

        cursor = connection.cursor()

        # Update faculty information in the database
        update_query = "UPDATE Faculty SET Email = %s, Phone_Number = %s WHERE Faculty_ID = %s"
        data = (new_email, new_phone_number, faculty_id)

        cursor.execute(update_query, data)
        connection.commit()

        if cursor.rowcount > 0:
            st.success("Faculty information updated successfully!")
        else:
            st.warning("No faculty found with the given ID.")

        # Close the database connection
        cursor.close()
        connection.close()
