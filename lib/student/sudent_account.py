from models import Student, session


def create_new_student():
    # Prompts student to enter required information
    print("Please add your details:")
    first_name = input("First Name: ")
    second_name = input("Second name: ")
    surname = input("Surname:  ")
    school_code = input("School code shared by principal: ")

    # Adds new student to the database
    new_student = Student(
        student_first_name=first_name,
        student_second_name=second_name,
        student_surname=surname,
        school_code=school_code
    )
    session.add(new_student)
    session.commit()

    # Finds new student to assign them a new unique key
    student_code = session.query(Student).all()
    for student in student_code:
        if (student.student_first_name == first_name
                and student.student_second_name == second_name
                and student.student_surname == surname
                and student.school_code == school_code):
            # add the student unique code.

            add_unique_code = session.query(Student).filter(Student.student_id == student.student_id).first()
            # Gives criteria of assigning the new student identification code

            new_student_code = (f"s{student.student_first_name[0]}{student.student_first_name[2]}{student.student_id}"
                                f"{student.student_surname[-1]}{school_code}")
            add_unique_code.unique_code = new_student_code
            session.commit()

            # message to confirm registration
            print(f"Thank you for registering with us you log in code is {new_student_code}")
