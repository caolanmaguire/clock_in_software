import os
import pwinput

os.system("CLS")


import logo

user_db = open("user_db.txt", "r")

user_accounts = []

for x in user_db:
    parsed_line = x.split(' ')
    try:
        user_accounts.append([parsed_line[0],parsed_line[1].replace('\n', '')])
    except:
        user_accounts.append([parsed_line[0],parsed_line[1]])



while True:
    username = input('Please enter your username below:');

    password = pwinput.pwinput('Please enter your password below:');

    if len(username) >= 5 and len(password) >= 5:
        break;
    else:
        print('Username and pasword has to be at least 5 characters long')



for x in user_accounts:

    if x[0] == username:
        if x[1] == password:
            print('logged in as : ' + username)
            break;
        else:
            print('Password is wrong')


menu_options = open("menu_options.txt", "r")
print(menu_options.read())

dialog_response = input('\n\nPlease choose from the above menu which function you would like to run : ')

while True:
    if dialog_response == '1':
        print('1')

    if dialog_response == '2':
        print('2')

    if dialog_response == '3':
        print('3')

    if dialog_response == '4':
        print('4')

    if dialog_response == '5':
        from program_functions import add_user

    if dialog_response == '6':
        from program_functions import email

    
    if dialog_response == '0':
        break;
    
    os.system("CLS")
    menu_options = open("menu_options.txt", "r")
    print(menu_options.read())
    dialog_response = input('\n\nPlease choose from the above menu which function you would like to run : ')


print('Thank you for using Smart Clocker')