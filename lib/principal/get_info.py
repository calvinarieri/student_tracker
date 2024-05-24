from models import Student_behaviour, session, Student
from tabulate import tabulate

# prints all the students in the school this is only for the principal there
def get_students_school(school_cod):
    print("Here are the number of students in your school")
    student_numbers = 0
    the_students = session.query(Student).filter(Student.school_code == school_cod).all()
    table = []    
    for student in the_students:
        student_numbers += 1
        data = [student_numbers , student.student_first_name , student.student_second_name, student.student_surname , student.unique_code] 
        table.append(data)

        # creates table for the details fetched
    print(tabulate(table, headers=['Number',"First Name", 'Second name', 'Surname', 'Unique code'], tablefmt='github')) 

# Prints the behavior of student according to a certain school only for the principals
def get_students_behaviour(school_id):
    the_mis = session.query(Student_behaviour).filter(Student_behaviour.school_code == school_id).all()
    table = []
    for the_mi in the_mis:
        student_name = session.query(Student).filter(Student.unique_code == the_mi.student_unique_code).first()
        data = [the_mi.misbehaviour_id,f'{student_name.student_first_name} {student_name.student_second_name}', the_mi.student_misbehave]
        table.append(data)
    print(tabulate(table, headers=['misbehaviour id', 'Student name', 'Mistake'], tablefmt='github'))    