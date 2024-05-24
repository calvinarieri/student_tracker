from models import Parent, session, Student
from sqlalchemy import exists
from .menu import parent_menu

# add new parent
def create_new_parent():
    print("Welcome to our system we are happy to work with you to make you son works hard and is disciplined in school")

    # gets the required input to  create a parent
    the_one = input("Your child code: ")
    student = session.query(exists().where(Student.unique_code == the_one))
        
    if student.scalar():
        print("Please enter the required details below")
        pa_id= None
        pa_name = input("Your full names: " )
        pa_ph = input("Your phone number: ")

        # enter values to be fed to the table
        new_parent = Parent(parent_id = pa_id, parent_name = pa_name, parent_phone=pa_ph, student_code = the_one)

        # pushes ths values to a database
        session.add(new_parent)
        session.commit() 

        # generates the loging code of the new parent
        give_code = session.query(Parent).filter(Parent.parent_name == pa_name, Parent.parent_phone ==pa_ph).first()
        the_code = f"p{give_code.parent_id*21}s{give_code.parent_name[0:2]}"
        give_code.parent_log_in = the_code     # updates the database
        session.commit()

        # output the loging/user  code for the parent.
        
        print('Do you want to proceed to log in?')
        print('1. Log in')
        print('2. Exit')
        option = input('Choose one:')
        if option == '1':
            GREEN = "\033[32m"
            print(GREEN+ f"\nWelcome {pa_name} your log/user in code is {the_code}" +RESET)
            parent_menu(the_code)
        elif option == '2':
            print(f"Welcome {pa_name} your log/user in code is {the_code}")
        else:
            print('Wrong choice')
            print(f"Welcome {pa_name} your log/user in code is {the_code}")

    else:
        RED = "\033[31m"
        RESET = "\033[0m"
        

        print(RED+"\n Oops! student does not exist! "+RESET)
        print("Do you want to try again?")
        print('1. Try again ')
        print('2. Exit ')
        option = input(' Choose one: ')
        if option == "1":
            print("Make sure you've added every character correctly.")
            create_new_parent()
        elif option == "2":
            print('Thank you for trying our application. Hope you will be back soon.')
        
        else:
            print(RED+ 'Wrong choice.\n Programme exited' +RESET)