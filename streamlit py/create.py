
import streamlit as st
import mysql.connector  # Assuming you are using MySQL
import pymysql

def create_student():
    st.subheader("Add a New Student")

    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    date_of_birth = st.date_input("Date of Birth")
    email = st.text_input("Email")
    phone_number = st.text_input("Phone Number")
    address = st.text_area("Address")

    if st.button("Add Student"):
        # Assuming you have a MySQL connection
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="idonothaveapassword",
            database="college_management_system"
        )

        cursor = connection.cursor()

        # Insert the new student into the database
        insert_query = "INSERT INTO Student (First_Name, Last_Name, Date_of_Birth, Email, Phone_Number, Address) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (first_name, last_name, date_of_birth, email, phone_number, address)

        cursor.execute(insert_query, data)
        connection.commit()

        st.success("Student added successfully!")

        # Close the database connection
        cursor.close()
        connection.close()

def create_faculty():
    st.subheader("Add a New Faculty Member")

    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    date_of_birth = st.date_input("Date of Birth")
    email = st.text_input("Email")
    phone_number = st.text_input("Phone Number")
    qualifications = st.text_area("Qualifications")

    if st.button("Add Faculty"):
        # Assuming you have a MySQL connection
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="idonothaveapassword",
            database="college_management_system"
        )

        cursor = connection.cursor()

        # Insert the new faculty member into the database
        insert_query = "INSERT INTO Faculty (First_Name, Last_Name, Date_of_Birth, Email, Phone_Number, Qualifications) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (first_name, last_name, date_of_birth, email, phone_number, qualifications)

        cursor.execute(insert_query, data)
        connection.commit()

        st.success("Faculty member added successfully!")

        # Close the database connection
        cursor.close()
        connection.close()



def add_report():
    st.subheader("Add Report")

    
    report_name = st.text_input("Report Name")
    marks = st.text_input("Marks")
    generation_date = st.date_input("Generation Date")
    faculty_id = st.text_input("Faculty_ID")
    student_id = st.text_input("Student_ID")

    if st.button("Add Report"):
        # Assuming you have a MySQL connection
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="idonothaveapassword",
            database="college_management_system"
        )

        cursor = connection.cursor()

        try:
            # Insert the new report into the database
            insert_query = "INSERT INTO Report (Report_Name, marks, Generation_Date, Faculty_ID, Student_ID) VALUES (%s, %s, %s, %s, %s)"
            data = (report_name, marks, generation_date, faculty_id, student_id)

            cursor.execute(insert_query, data)
            connection.commit()
            st.success("Report added successfully!")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")
            connection.rollback()
        finally:
            # Close the database connection
            cursor.close()
            connection.close()


# Function to enroll the student in a course
def enroll_course():
    st.subheader("Add Student Mess")

    student_id = st.text_input("Enter Student ID")
    mess_name = st.selectbox("Select Mess", ['Vakula', 'Food Court'])
    
    if st.button("Enroll in Mess"):
        # Connect to the database
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="idonothaveapassword",
            database="college_management_system"
        )

        cursor = connection.cursor()

        try:
            # Get mess_id based on the selected Mess_name
            mess_id_mapping = {'Vakula': 1, 'Food Court': 2}
            mess_id = mess_id_mapping.get(mess_name)

            if mess_id is None:
                st.error("Invalid course name selected.")
                return

            # Insert the enrollment record into the Enrollment table
            insert_query = "INSERT INTO Enrollment (Student_ID, mess_id, Mess_name) VALUES (%s, %s, %s)"
            data = (int(student_id), mess_id, mess_name)

            cursor.execute(insert_query, data)
            connection.commit()

            st.success("Enrollment successful!")

        except mysql.connector.Error as err:
            st.error(f"Error: {err}")
            connection.rollback()

        finally:
            # Close the database connection
            cursor.close()
            connection.close()

def fetch_mess_id(mess_name):
    # Connect to the database
    connection = pymysql.connect(
            host="localhost",
            user="root",
            password="idonothaveapassword",
            database="college_management_system"
        )

    cursor = connection.cursor()

    # Query the database to get the mess_id based on mess_name
    query = "SELECT mess_id FROM Courses WHERE Mess_name = %s"
    cursor.execute(query, (mess_name,))
    result = cursor.fetchone()

    # Close the database connection
    cursor.close()
    connection.close()

    # Check if a result was found
    if result:
        return result[0]  # Return the first column (mess_id)
    else:
        return None  # Return None if no result was found
    

