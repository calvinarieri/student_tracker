import os
import time 

from student.sudent_account import create_new_student
from parent.parent_account import create_new_parent
from principal.principal_account import create_new_principal
from company.company_profile import create_new_company


# menu importations
from student.menu import student_menu
from parent.menu import parent_menu
from principal.menu import principal_menu
from company.menu import company_menu              

# the main menu for the users.
def main(user_id):

    # Finds the category of the user eithe company principal student or parent
    find_category = user_id[0]

    # Student options
    if find_category == "s":
        student_menu(user_id)

    elif find_category == 'p':
        parent_menu(user_id)

    elif find_category == 'c':
        company_menu(user_id)
       

    elif find_category == 'a':
        principal_menu(user_id)



WELCOME_MESSAGE = """
Welcome to school management system
We manage students results 
Online school fees payment
behavior
ratings
Happy using!
"""

def print_welcome_message():
    for line in WELCOME_MESSAGE.splitlines():
        print(line)        
        time.sleep(2) # delay print     
        
        os.system('clear')  # macOS/Linux

        # Or print multiple newlines for limited clearing
        for _ in range(4):
            print()

# starts the cli program 
if __name__ == "__main__":
    def start_app():
        # welcomes you to the system 
        print_welcome_message()
        print("Are you an existing member?")
        print("1. Yes")
        print("2. No")

        # Receive options
        get_choice = input("Choose one: ")

        # log if in the system
        if get_choice == "1": 
            os.system('clear')  # macOS/Linux
            user_id = input("Please enter your user number: ")
            main(user_id)

            # register if not in the system
        elif get_choice == "2":
            os.system('clear')  # macOS/Linux
            print("Please register with us to use this system.")  
            print("Do you want to regster as:") 

            # Gives list of people to be registered
            list_of_choices = ("Student", "Parent", "Principal", "Company")

            #  Returns the options availablen
            num = 0
            for choice in list_of_choices:
                num += 1
                print(f"{num}. {choice}")

                # prompts user to chose their choice
            the_chosen = input("Please choose one: ") 

            # The users choice
            if the_chosen == "1":
                os.system('clear') 
                create_new_student()

                        # Application of a new parent.
            elif the_chosen == "2":

                # must have a student code to register as ne parent
                os.system('clear') 
                print("Once you child has identification code you can now proceed to this step.")
                print("Does your child have an Identification code?") 
                print("1. Yes")
                print("2. No")

                # If lacks the student code
                present_code = input("Choose one option: ")
                if present_code == "2":

                    # Output messages
                    os.system('clear') 
                    print("Apply for the code. And one has applied for it please wait for response from the school so that you can register")
                    print("Thank you for showing interest in our system.")

                    # if has student code
                if present_code == "1":
                    os.system('clear') 
                    
                    # calls the creating new parent function
                    create_new_parent()
            elif the_chosen == "3":

                os.system('clear')
                # calls the new principal function
                create_new_principal()
            elif the_chosen == "4":

                os.system('clear')
                # calls the new company function
                create_new_company()

            else:
                print('Wrong choice!')

    start_app()
             

