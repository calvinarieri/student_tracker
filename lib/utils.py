import os

# COMMAND LINE COLORS FOR DIFFERENT INSTANCES.

def recursion_of_menu(user_id,  recursive_function, message = ''):
    if len(message) > 4 :
        os.system('clear')
        print(message)
        print('Do you want to try again')
        print('1. Yes')
        print('2. No')
        option = input('Choose one: ')
        if option == '1':
            recursive_function(user_id)
        elif option == '2':
            GREEN = '\033[92m'
            RESET = "\033[0m"
            print(GREEN+ 'Programme exited successfull!'+RESET)
            
        else:
            RED = "\033[31m"
            print(RED+ 'Invalid choice.Programme exite'+RESET)
    else:
        print('Would you like to?')
        print('1. Go back to your account menu')
        print('2. Exit')
        option = input('Choose one: ')
        if option == '1':
            recursive_function(user_id)
        elif option == '2':
            GREEN = '\033[92m'
            RESET = "\033[0m"
            os.system('clear')
            print(GREEN+'Programme exited successfull!'+RESET)
            
        else:
            RED = "\033[31m"
            RESET = "\033[0m"
            os.system('clear')
            print(RED+'Invalid choice.Programme exited'+RESET)

    