from models import Principal, session

# add new principal
def create_new_principal():
    print("Thank you for choosing our system.Provide the following info to add you to the system.")

    # getting details of the new principal
    p_id = None
    p_reg =int(input("T.S.C number: "))
    p_s = input("School code: ")
    p_n = input("Your full name: ")
    p_n_p = int(input("Your phone number: "))
    # creating the new principal 

    new_principal = Principal(principal_id=p_id ,principal_reg = p_reg,  principal_school = p_s, principal_name = p_n, principal_phone_number = p_n_p)

    # Adding the principal to the database
    session.add(new_principal)
    session.commit()

    # generating the principal user/log  code
    print(f"Welcome {p_n} your usercode is a{p_reg}") 