from models import Other_user, session

# add new company
def create_new_company():
    print("Thank you for choosing our system to get a person information before hiring them.")
    print("Before you continue please register with us")

    # Get details of the new company
    u_id = None
    u_n = input("User Name: ")
    u_p = input("password: ")
    c_n = input("Company Name: ")

    # add the new company to the database
    new_company = Other_user(user_id = u_id, user_name = u_n, user_password = u_p, company_name = c_n) 
    session.add(new_company)
    session.commit()

    # out puts the log in code
    print(f"Welcome {c_n} we are happy to work with your user code is c{u_p}") 