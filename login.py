users = {}

users['John'] = '123'

def welcome():
    response = int(input("Welcome to Site! To login, press 1, if you forgot password, press 2, and to register, press 3"))
    if response == 1:
        login()
    elif response == 2:
        forgotPass()
    elif response == 3:
        register()
    else:
        print("Invalid Response")
        welcome()

def login():
    username = input('Enter username: ')
    if username in users:
        password = input("Enter password: ")
        if users[username] == password:
            print('Logged In')
        else:
            print('Incorrect password!')
            welcome()
    else:
        print("Sorry! That's not a valid username.")
        welcome()

def forgotPass():
    userName = input('Please enter your name: ')
    print('Your password is: ', users[userName])
    print('-------------')
    print('-------------')
    welcome()

def register():
    username = input("Enter new Username: ")
    password = input('Enter new password: ')
    users[username] = password
    welcome()

welcome()







    
