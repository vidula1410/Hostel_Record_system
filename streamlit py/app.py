#streamlit run .\app.py
import streamlit as st
from create import create_student, create_faculty, add_report , enroll_course, fetch_mess_id
from database import create_tables
from delete import delete_student, delete_faculty
from read import read_students, read_faculties, display_reports, display_reports_for_student, get_student_courses
from update import update_student, update_faculty
from sql_stat import stat




def main():
    st.title("Hostel Mess Management System")
    create_tables()  # Ensure tables are created

    # Login
    user_type = st.sidebar.radio("Select User Type", ["Warden", "Student", "Faculty"])

    if user_type == "Warden":
        # if Warden_login():
            Warden_menu = ["Add Student", "View Students", "Mess Enrollment", "Edit Students", "Add Faculty","View Faculties", "Edit Faculties", "Statistics", "Remove"]
            Warden_choice = st.sidebar.selectbox("Select Action", Warden_menu)
            
            if Warden_choice == "Add Student":
                create_student()
            elif Warden_choice == "View Students":
                read_students()
            elif Warden_choice == "Mess Enrollment":
                enroll_course()
            elif Warden_choice == "Edit Students":
                update_student()
            elif Warden_choice == "Add Faculty":
                create_faculty()
            elif Warden_choice == "View Faculties":
                read_faculties()
            elif Warden_choice == "Edit Faculties":
                update_faculty()
            elif Warden_choice == "Statistics":
                stat()
            elif Warden_choice == "Remove":
                delete_student()
                delete_faculty()
            else:
                st.subheader("About Hostel Management System")
    elif user_type == "Student":
    # Add code for student functionalities here
       student_id = st.text_input("Enter Student ID")
       if st.button("View Details"):
        read_students(student_id)
        st.subheader("Student Dashboard")
        st.info("Welcome, Student!")
        #display_reports_for_student(student_id)
        
        # Streamlit UI
        st.title("Student Mess Enrollment")
        get_student_courses(student_id)

        
    
    elif user_type == "Faculty":
      faculty_id = st.text_input("Enter Faculty ID")
      if st.button("View Details"):
        read_faculties(faculty_id)
        st.subheader("Faculty Dashboard")
        st.info(f"Welcome, Faculty!")
        st.header("Student Details")
        read_students()
        #display_reports()


if __name__ == "__main__":
    main()




