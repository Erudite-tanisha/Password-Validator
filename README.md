# Password Validator
This repository contains the source code for a password validator built in Python.

## Python Installation Guide
To run this code, you need Python 3 installed on your machine.

1. Visit the [official Python website](https://www.python.org/downloads/) and install a stable version of Python 3.
2. After installation, confirm the version using:
   ```bash
   python3 --version
   ```
3. Clone this repository:
  ```bash
  git clone https://github.com/Erudite-tanisha/Password-Validator.git
  ```
4. Change to the Password Validator directory:
```bash
python3 main.py
```

## Password Acceptance Criteria
1: PASSWORD LENGTH SHOULD BE OF MINIMUM 12 CHARACTER

2: PASSWORD LENGTH SHOULD NOT BE GREATER THAN 20 CHARACTER

3: PASSWORD MUST CONSIST OF UPPER-CASE CHARACTER [A-Z]

4: PASSWORD MUST CONSIST OF LOWER-CASE CHARACTER [a-z]

5: PASSWORD MUST CONSIST OF NUMBER [0-9]

6: PASSWORD MUST CONSIST OF SPECIALCHARACTER - !, @, #, $, %, ^, &, *, (, ), _, -, ~

7: PASSWORD SHOULD START WITH EITHER ANY SPECIALCHARACTER OR WITH 2 DIGIT'S NUMBER

8: PASSWORD SHOULD CONTAIN ATLEAST3 UPPER-CASE CHARACTER AND 3 LOWER-CASE CHARACTER

9: PASSWORD SHOULD CONTAIN ATLEAST3 SPECIAL CHARACTER

10: PASSWORD SHOULD NOT CONTAIN 5 SAMECHARACTER\ OR NUMBER CONSECUTIVELY

11: PASSWORD SHOULD NOT HAVE USERNAMEINTO IT AT ANY POSITION

12: PASSWORD SHOULD NOT CONTAIN 3 SAME SPECIAL CHARACTER'S CONSECUTIVELY

## Functions
### instructions(): 
Displays instructions for password requirements.

### UserName(): 
Prompts the user to enter their username.

### Password(): 
Prompts the user to enter their password.

### Length(passw): 
Checks if password length is between 12 and 20 characters.

### Start(passw): 
Verifies the password starts with a special character or two-digit number.

### Special(passw): 
Ensures password includes at least 3 special characters.

### Case(passw): 
Confirms password has at least 3 uppercase and 3 lowercase characters.

### User(name, passw): 
Ensures the password does not contain the username.

### Digit(passw): 
Checks if the password has at least 2 digits.

### ConsecutiveNum(passw): 
Prevents 5 identical consecutive characters or numbers.

### ConsecutiveChar(passw): 
Prevents 3 identical special characters consecutively.

### CommonPass(passw): 
Ensures the password is not among common passwords (using the CommonPasswords module).

### main(): 
Manages user attempts and provides options to retry or exit after 3 failed attempts.

### Helper(name, passw): 
A helper function to run all checks in sequence.

## CommonPasswords.py
The script uses an imported common list from the CommonPasswords module, which contains a predefined list of common passwords.

## How to use
1.Run the script.      
2.Enter the desired username when prompted.     
3.Follow the instructions to input a password.     
4.The script will validate the password based on the defined criteria.     
5.It validate the username and proceed to ask password.        
6.If the password is valid, a confirmation message will be displayed. Otherwise, the user will be prompted to enter a new password that meets the requirements.           
7.Ask User whether he wants to continue making password in 3 times wrong password input. If the user says "y" ask for the username again.




