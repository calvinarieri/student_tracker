from models import Other_user, session
from utils import recursion_of_menu

from student.student_info import student_rating

def company_menu(user_id):
     # gets the company password
        password = user_id[1:6]
        print(password)

        # get the company details to be used within
        the_company = session.query(Other_user).filter(Other_user.user_password == password).first()
        print(f'Welcome back {the_company.company_name}')

        # use the user code to gwt the records
        the_code = input("The student code: ")
        student_rating(the_code)
        recursion_of_menu(user_id, company_menu)