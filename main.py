from CommonPasswords import common

def instructions():
    print("Please follow the following instructions - ")
    print("Password length has to be between 12 and 20 characters!")
    print("Password must consist of Characters in Upper Case (A-Z)!")
    print("Password must consist of Characters in Lower Case (a-z)!")
    print("Passowrd should consist of Numbers - (0-9)!")
    print("Passowrd should consist of atleast 3 Special Characters (!, @, #, $, %, ^, &, *, (, ), _, -, ~)!")
    print("Password should start with either any special character or 2 digit number!")
    print("Password should have at least 3 Upper Case and 3 Lower Case characters!")
    print("Password cannot contain  5 same characters or numbers consecutively!")
    print("Password cannot have 3 same special charaters consecutively!")
    print("Password cannot have the UserName into it at any position!")

def UserName():
    user = input("ENTER USERNAME: ")
    print("WELCOME!", user)
    return user

def Password():
    return input("ENTER YOUR PASSWORD: ")

def Length(passw):
    if 12 <= len(passw) <= 20:
        return True
    else:
        print("Password length must be between 12 and 20 characters!!")
        return False
        
def Start(passw):
    if passw.startswith(('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '~')) or passw[:2].isdigit():
        return True
    else:
        print("Password should start with a special character or a 2-digit number!!")
        return False
    
def Special(passw):
    count = sum(1 for i in passw if i in '!@#$%^&*()_-~')
    if count >= 3:
        return True
    else:
        print("Password must have at least 3 special characters!!")
        return False

def Case(passw):
    countupper = sum(1 for i in passw if i.isupper())
    countlower = sum(1 for i in passw if i.islower())
    if countupper >= 3 and countlower >= 3:
        return True
    else:
        print("Password must have at least 3 uppercase and 3 lowercase characters!!")
        return False

def User(name, passw):
    if name not in passw:
        return True
    else:
        print("Password cannot contain the username!")
        return False

def Digit(passw):
    count = sum(1 for i in passw if i.isdigit())
    if count >= 2:
        return True
    else:
        print("Password must contain at least 2 digits!!")
        return False

def ConsecutiveNum(passw):
    count = 1
    for i in range(1,len(passw)):
        if passw[i] == passw[i-1]:
            count += 1
    if count >= 5:
        print("Password cannot contain 5 same characters or numbers consecutively!!")
        return False
    else:
        return True

def ConsecutiveChar(passw):
    count = 1
    for i in range(1, len(passw)):
        if passw[i] in '!@#$%^&*()_-~' and passw[i] == passw[i-1]:
            count += 1
    if count >= 3:
        print("Password cannot have 3 same special characters consecutively!!")
        return False
    else:
        return True

def CommonPass(passw):
    if passw not in common:
        return True
    else:
        print("This password is too common, please try another!!")
        return False

def main():
    attempts = 3
    name = UserName()
    instructions()
    while attempts>0:
        passw = Password()
        if Helper(name, passw):
            print("Password is valid!!")
            break
        else:
            attempts -= 1
            print(f"{attempts} attempts are left!!")

    if attempts == 0 :
        user_input = input("PRESS Y -- To Continue --  OR PRESS N to End: ")

        if user_input.lower() == "y":
            main()
        else:
            print("Thank you! for your response")

def Helper(name, passw):
    return Length(passw) and Case(passw) and Special(passw) and Digit(passw) and User(name, passw) and ConsecutiveChar(passw) and ConsecutiveNum(passw) and Start(passw) and CommonPass(passw)
           
main()
