from CommonPasswords import common

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
        return False
        
def Start(passw):
    if passw.startswith(('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '~')) or passw[:2].isdigit():
        return True
    else:
        return False

def Special(passw):
    count = sum(1 for i in passw if i in '!@#$%^&*()_-~')
    return count >= 3

def Case(passw):
    countupper = sum(1 for i in passw if i.isupper())
    countlower = sum(1 for i in passw if i.islower())
    return countupper >= 3 and countlower >= 3

def User(name, passw):
    return name not in passw

def Digit(passw):
    count = sum(1 for i in passw if i.isdigit())
    return count >= 2

def ConsecutiveNum(passw):
    max = 1
    current = 1
    for i in range(1, len(passw)):
        if passw[i] == passw[i-1]:
            current += 1
            max = max(max, current)
        else:
            current = 1
    return max < 5

def ConsecutiveChar(passw):
    max = 1
    current = 1
    for i in range(1, len(passw)):
        if passw[i] in '!@#$%^&*()_-~' and passw[i] == passw[i-1]:
            current += 1
            max = max(max, current)
        else:
            current = 1
    return max < 3

def CommonPass(passw):
    return passw not in common

def Helper():
    name = UserName()
    while True:
        passw = Password()
        if not Length(passw):
            print("Password length must be between 12 and 20 characters!!")
        elif not Case(passw):
            print("Password must have at least 3 uppercase and 3 lowercase characters!!")
        elif not Special(passw):
            print("Password must have at least 3 special characters!!")
        elif not Digit(passw):
            print("Password must contain at least 2 digits!!")
        elif not User(name, passw):
            print("Password cannot contain the username!")
        elif not ConsecutiveNum(passw):
            print("Password cannot contain 5 same characters or numbers consecutively!!")
        elif not ConsecutiveChar(passw):
            print("Password cannot have 3 same special characters consecutively!!")
        elif not Start(passw):
            print("Password should start with a special character or a 2-digit number!!")
        elif not CommonPass(passw):
            print("This password is too common, please try another!!")
        else:
            print("Password is valid!!")
            break

Helper()
