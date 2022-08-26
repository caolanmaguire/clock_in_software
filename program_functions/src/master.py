import os
import sys
import pwinput
import time
from datetime import datetime

from list_users import list_all_users
# sys.path.insert(1, 'program_functions/facial-recognition/src')

# import faces


now = datetime.now()

program_start_time = now.strftime("%H:%M:%S-%d/%m/%y")

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
            print('logged in as : ' + username + ' at : ' + program_start_time)
            break;
        else:
            print('Password is wrong')
            exit()


menu_options = open("menu_options.txt", "r")
print(menu_options.read())

dialog_response = input('\n\nPlease choose from the above menu which function you would like to run : ')

while True:
    if dialog_response == '1':
        #from program_functions import faces
<<<<<<< HEAD:program_functions/src/master.py
=======
        os.system('cd program_functions/Facial-Detection/src/')
        os.system('faces.py')
        #exec(open('/program_functions/Facial-Detection/src/faces.py').read())
>>>>>>> e40a67da2efcb6c17ebb646d8ca401f25878241b:master.py
        print('1')
        # os.system('cd program_functions/Facial-Detection/src/')
        # os.system('python faces.py')
        #cls
        exec(open('faces.py').read())

    if dialog_response == '2':
        user_db = open("database.csv", "r")
        
        print('\t\t\t* * * DATABASE RESULTS * * * ')
        print('\t\tFIRST NAME | DOB | COMPANY ID | CLOCKED TIME')

        for x in user_db:
            print('\t\t' + x.replace(',',' | '))

    if dialog_response == '3':
        list_all_users()

    if dialog_response == '4':
        import remove_user

    if dialog_response == '5':
        import add_user

    if dialog_response == '6':
        import smtplib
        import imghdr
        from email.message import EmailMessage
        from datetime import date
        import os
        from program_functions import send_email

    if dialog_response == '0':
        break;
    
    # os.system("CLS")
    menu_options = open("menu_options.txt", "r")
    print(menu_options.read())
    dialog_response = input('\n\nPlease choose from the above menu which function you would like to run : ')

print('Thank you for using Smart Clocker')