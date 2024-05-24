from parent.student_info import parent_get_student_behaviour, parent_get_student_result
from .student_info import student_rating
from models import Student, session
from utils import recursion_of_menu
import os



def student_menu(user_id):
    # get student details to be used within
    the_details = session.query(Student).filter(Student.unique_code == user_id).first()
    os.system('clear')
    print(f"Welcome back {the_details.student_second_name} {the_details.student_surname},")
    print("What details do tou want to see today ")

    # tuple of options
    option_for = ('Results', 'Behaviour', 'Rating', 'quit')

    # counting the options
    the = 0

    # printing the options  available
    for option in option_for:
        the += 1
        print(f'{the}. {option}')
    one_option = input("choose one: ")
    if one_option == '1':
        os.system('clear')
        print(f'Here are your results {the_details.student_first_name} ')
        parent_get_student_result(user_id)
        recursion_of_menu(user_id, student_menu)
        
    elif one_option == '2':
        os.system('clear')
        print(f'Here are your indiscipline case {the_details.student_first_name} ')
        parent_get_student_behaviour(user_id)
        recursion_of_menu(user_id, student_menu)

    elif one_option == '3':
        os.system('clear')
        student_rating(user_id)
        recursion_of_menu(user_id, student_menu)

    elif one_option == '4':
        os.system('clear')
        print(f'You have successfully quited the programme.We hope to see you again {the_details.student_first_name}')
        recursion_of_menu(user_id, student_menu)

    else:
        print('Invalid input')
