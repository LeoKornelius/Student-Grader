'''
Teachers will be allowed to modify or add student grades as long as their passwords are correct
To register class and password a teacher must know the school code which will be "school code"
'''

database = {}

def name_check(teacher_name):
    unique = True
    for subject in database:
        if database[subject][0] == teacher_name:
            unique = False
            break
    return unique


def teacher_information(): # returns tuple with subject name, teacher name, and password
    # Unique name check
    name_cond = True
    print("Alright, let's register your class!")
    while name_cond:
        teacher_name = input("Please type your name: ")
        if name_check(teacher_name):
            name_cond = False
        else:
            print("Please type in your full name since another teacher has already registered the typed name...")

    # Confirm password check
    password_cond = True
    print(f'Great, {teacher_name}!')
    while password_cond:
        teacher_password = input("Please register a password: ")
        confirm_password = input("Confirm the password typed above: ")
        if teacher_password == confirm_password:
            password_cond = False
        else:
            print("The passwords aren't the same, please try again...")

    # Unique subject name check
    subject_cond = True
    print("Perfect! Let's finish the class setup!")
    while subject_cond:
        subject_name = input("Finally type in the class name: ")
        if subject_name not in database.keys():
            subject_cond = False
        else:
            print("Another teacher is alreadying using the class name typed. Try another...")

    return subject_name, [teacher_name, teacher_password, {}]


def teacher_info(teacher_name):
    for subject in database:
        if database[subject][0] == teacher_name:
            return subject, database[subject]


def teacher_login():
    print("Please type the login information below...")
    login_cond = True
    while login_cond:
        teacher_name = input("Please type your name: ")
        teacher_password = input("Please register a password: ")
        if not name_check(teacher_name): # checks if name is in database
            teacher_subject, teacher_subject_info = teacher_info(teacher_name)
            if teacher_password == teacher_subject_info[1]:
                login_cond = False
            else: # incorrect password
                print("Incorrect password. Try again...")
        else:
            print("It seems you haven't registred a class...")
            ans = input("Would you like to register a class? ")
            if ans.lower() == "yes":
                teacher_signup()
            else:
                 print("Perhaps you mispelled your name. Try again...")
    return teacher_subject, teacher_subject_info


def teacher_signup():
    database_key, database_value = teacher_information()
    database[database_key] = database_value
    print(f'All done!\nYour class has been registred, {database_value[0]}.')
    teacher_login()


def main():
    cond = True
    print("Welcome to the school grading system!")
    while cond:
        persona = input("Are you a student or teacher?")
        if persona == "teacher":
            cond = False
        elif persona == "student":
            cond = False
        else:
            print("Please type student or teacher")