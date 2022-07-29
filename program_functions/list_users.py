
def list_all_users():
    print('*** List Users ***\n')
        
    user_db = open("user_db.txt", "r")
    for x in user_db:
        print('    ' + x.split(' ')[0])