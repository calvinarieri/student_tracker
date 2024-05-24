from models import Student, Parent , Student_results, session, Principal
from tabulate import tabulate
from utils import recursion_of_menu
import os


from .add_student_info import add_misbehave, add_new_result
from .get_info import get_students_school, get_students_behaviour
from student.student_info import student_rating  

def principal_menu(user_id):

        # get the student registration number
        os.system('clear') 
        the_search_code = user_id[1:6]
        the_int = int(the_search_code) #change the number to string

        # fetch information related to the principal for further processing
        get_principal = session.query(Principal).filter(Principal.principal_reg == the_int).first()

        # the principal options
        print(f"Welcome back {get_principal.principal_name},")
        print('Do you want to:')
        print('1. Add details')
        print('2. View details')
        print('3. Delete student')
        print('4. Quit')

        # allows the user to enter the option the want to access
        the_choice = input('Choose one: ')
        if the_choice == '1':
            os.system('clear') 
            print('Choose one: ')

            # tuple of otion
            options = ('Results', 'Behaviour')

            # counts the options
            number_of = 0

            # printing otions
            for option in options:
                number_of += 1
                print(f"{number_of}. {option}")

                # user choosing one option
            receive_option = input("Choose one: ")

            # find the option chosen
            if receive_option == "1":
                os.system('clear') 
                # adds new result
                student_unique_number = input("Please key in student unique number: ")

                # finds out if student principal
                find_out = session.query(Student).filter(Student.unique_code == student_unique_number).first()
                if find_out.school_code == get_principal.principal_school:
                    os.system('clear') 
                    add_new_result(student_unique_number)
                    recursion_of_menu(user_id, principal_menu)

                else:

                    # Refuse to add if not the student pricipal
                    recursion_of_menu(user_id, principal_menu, "You are not allowed to change any detail of the student.")
                    

            elif receive_option == "2":
                os.system('clear') 
                # Takes in student unique key
                student_unique_number = input("Please key in student unique number: ")

                # finds if is the current student principal
                find_out = session.query(Student).filter(Student.unique_code == student_unique_number).first()

                # if yes it adds the misbehave
                if find_out.school_code == get_principal.principal_school:
                    add_misbehave(get_principal.principal_school ,student_unique_number)
                    recursion_of_menu(user_id, principal_menu)
                else:

                    # if false does not add the misbehave
                     recursion_of_menu(user_id, principal_menu, "You are not allowed to change any detail of the student.")                
            else:

                # any input not making sense it will print this
                recursion_of_menu(user_id, principal_menu, "Invalid input")
        elif the_choice == "2":
            os.system('clear') 
            print('Welcome to the view details section')

            # tuple of principal otions
            options = ["Students", 'Misbehaviours', 'student rating', 'students perfomance', 'student parent']

            # counts number of options
            num = 0

            # prints the options for the users
            for option in options:
                num += 1
                print(f'{num}. {option}')

            # user chooses one option
            the_opt = input('Choose one: ')

            # choose operation according to choice
            if the_opt  == '1':
                os.system('clear') 
                get_students_school(get_principal.principal_school) 
                recursion_of_menu(user_id, principal_menu)

            elif the_opt == '2':
                os.system('clear') 
                get_students_behaviour(get_principal.principal_school) 
                recursion_of_menu(user_id, principal_menu)

            elif the_opt == '3':
                os.system('clear') 
                print('To get the student rating please input the student user code.')
                the_code = input("The student code: ")
                student_rating(the_code)
                recursion_of_menu(user_id, principal_menu)

            elif the_opt == '4':
                    os.system('clear') 
                    # gets all students according the school code
                    the_students = session.query(Student).filter(Student.school_code == get_principal.principal_school).all()
                    table = []
                    for student in the_students:

                        # Getting the students names and the results
                        the_result = session.query(Student_results).filter(Student_results.student_unique_code == student.unique_code).all()
                        for result in the_result:

                            # creating table row
                            data = [result.result_id ,f'{student.student_first_name, student.student_second_name, student.student_surname}', result.student_perfomance]
                            table.append(data)

                    # creating table for the data queried
                    print(tabulate(table, headers=['Exam id', 'Student full Names', 'Student perfomance in %']))  
                    recursion_of_menu(user_id, principal_menu)

            elif the_opt == '5':
                os.system('clear') 
                # TODO: FOR STUDENT
                """
                1. Request for the principal to enter student unique code
                2. Query the parents table and filter parents whose student_code is the student code entered by the principal
                3. Check if the exist if there is any parents details isn'tpass message of 'NOT ADDED'  to fuction =>  recursion_of_menu(user_id, principal_menu, {{PASS MESSAGE HERE}}) . 
                4. If exist proceed with tabulating the information then print it. Then import recursion if not imported function from utils and pass required parameters recursion_of_menu(user_id, principal_menu) 
                N/B:
                    Refer to models.py for fields
                    To tabulate refer to: https://pypi.org/project/tabulate/
                    For querying: https://docs.sqlalchemy.org/en/14/orm/query.html
                    For querying use: student = session.query(Parent).filter(Parent.student_code=={{VARIABLE HOLDING THE STUDENT CODE}})).ALL()
                    For conditonal statements: https://www.geeksforgeeks.org/conditional-statements-in-python/
                    
                """
        elif the_choice == '3':

            os.system('clear') 
            # prompt for input
            print("Input student user code to be deleted")
            user_code = input('User code: ')

            # find the student
            find_out = session.query(Student).filter(Student.unique_code == user_code).first()

            # confirm if is students principal
            if find_out.school_code == get_principal.principal_school:
                print(f'You have succesfully deleted {find_out.student_first_name} {find_out.student_second_name} {find_out.student_surname}')
                session.delete(find_out)
                session.commit()

            else:
                os.system('clear') 
                # If not the students principal gives this output message
                print("You cannot delete the student since you are not the school principal")
                principal_menu(user_id)

        elif the_choice == '4':
            os.system('clear') 
            # exiting the programme
            print('You have successfully exited the programme')

        else:
            os.system('clear') 
            print('Invalid output')


