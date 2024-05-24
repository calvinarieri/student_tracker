from parent.student_info import parent_get_student_behaviour, parent_get_student_result
from student.student_info import student_rating
from .payment import pay_school_fees
from models import Parent, session
import os
from utils import recursion_of_menu

def parent_menu(user_id):
        
            # get parent details to be used within
        the_details = session.query(Parent).filter(Parent.parent_log_in == user_id).first()
        print(f'welcome back {the_details.parent_name}')

        # list of options
        option_for = ('Results', 'Behaviour', 'Rating', 'Pay school fees','quit', )

        # counts number of options
        the = 0

        # prints the options available
        for option in option_for:
            the += 1
            print(f'{the}. {option}')

            # choosing one user option
        the_option = input('choose one option: ') 
        if the_option == "1":
            os.system('clear')
            parent_get_student_result(the_details.student_code)
            recursion_of_menu(user_id, parent_menu)
        elif the_option == '2':
            os.system('clear')
            parent_get_student_behaviour(the_details.student_code)
            recursion_of_menu(user_id, parent_menu)
        elif the_option == '3':
            os.system('clear')
            student_rating(the_details.student_code)
            recursion_of_menu(user_id, parent_menu)
        elif the_option == '4':
             os.system('clear')
             print('Add the following information to initiate fee payment')
             pay_school_fees(the_details.student_code,)
             recursion_of_menu(user_id, parent_menu)
        elif the_option == '5':
            os.system('clear')
            print('You have successfuly exited the program')
        else:            
            recursion_of_menu(user_id, parent_menu, 'invalid output')