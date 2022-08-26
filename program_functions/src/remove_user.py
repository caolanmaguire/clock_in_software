import pwinput
import time

print('\nAdd New User Below\n')
new_username = input("Enter the new user's username : ")
new_password = pwinput.pwinput("Enter the new user's password : ")

with open("user_db.txt", "a") as file_object:
    file_object.write("\n" + new_username + " " + new_password)

print('user has been added!\nReturning you to home page\n')
time.sleep(3)