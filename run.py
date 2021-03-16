#!/usr/bin/env python3.6
from user import User
from credential import Credential
def create_users(username,password):
    """
    function to create a new user
    """
    new_user = User (username,password)
    return new_user
def save_users(user):
    """
    Function to save user
    """
    user.save_user()
def display_users(user):
    """
    Function to display saved user
    """
    return user.display_user()
def login_user(username,password):
    """
    Function that checks whether a user exist and then login
    """
    check_user = Credential.verify_user(username,password)
    return check_user
def delete_users(user):
    """
    Function to delete a user
    """
    user.delete_user()
def create_credentials(accountName,username,password):
    """
    Function to create a new credential
    """
    new_credential = Credential(accountName,username,password)
    return new_credential
def save_credentials(credential):
    """
    Function to save credential
    """
    credential.save_credential()
def passwords_generate():
    """
    Generate random password of string letters,digits and ponctuation
    """
    return Credential.password_generate()
def display_credentials():
    """
    Function to display saved credential
    """
    return Credential.display_credentials()
def delete_credentials(credential):
    """
    Function to delete a credential
    """
    credential.delete_credential()
def find_credentials(username):
    """
    function that finds in username and returns a credential that matches that username
    """
    return Credential.find_by_username(username)
def exist_credentials(username):
    """
    Function that checks if a credential exists from the credential list and return true or false.
    """
    return Credential.credential_exist(username)
def copy_passwords(username):
    """
    function that copy password
    """
    return Credential.copy_password(username)
def password_locker():

    print(">" * 80)
    print("\n")
    print("WELCOME TO PASSWORD LOCKER\n ")
    print("<" * 80)
    print("\n")
    print("Please enter your name")
    print("----------------------")
    user_name = input()
    print(f"Hi, {user_name} what would you like to do? \n CNA .... Create new account \n HA .... Have account\n \n ")
    short_code = input("").lower().strip()
    if short_code == "cna":
        print("Sign Up")
        print('--------')
        username = input("User_name: ")
        while True:
            print("TP => Type your Password\nGP => Generate  Password")
            password_choice = input().lower().strip()
            if password_choice == 'tp':
                password = input("Enter Password\n")
                break
            elif password_choice == 'gp':
                password = passwords_generate()
                break
            else:
                print("Invalid password please try again")
        save_users(create_users(username,password))
       
        print(f"Hi {username},Your account has been created ! Your password is : {password}")
        print("=" * 80)
    elif short_code == "ha":
        print("-" * 65)
        print("Enter your User name and your Password to log in:")
        print("-" * 65)
        username = input("User name: ")
        password = input("password: ")
        print("\n")
        # login = login_user(username,password)
        if login_user (username,password) == None:
            print("Invalid username and password\n")
        else:
            print(f"Hi {username}, Welcome To Password Locker Functions")
            print("----------------------------------------------")
            print("\n")
    while True:
        print("Use these short codes:\n CC - Create new Credential \n DC - Display Credential \n FC - Find Credential \n GP - Generate Password \n D - Delete Credential \n EX - Exit application\n")
        print("="* 80)
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create New Credential")
            print("." * 20)
            print("\n")
            print("Account name ")
            accountName = input().lower()
            print("Your Account username")
            username = input()
            while True:
                print("TP => Type your password of the existing an account\nGP => Generate Password")
                password_choice = input().lower().strip()
                if password_choice == "tp":
                    password = input("Enter your Password\n")
                    break
                elif password_choice == 'gp':
                    password = passwords_generate()
                    break
                else:
                    print("Invalid password please try again")
            save_credentials(create_credentials(accountName,username,password))
            print("\n")
            print(":" *50)
            print(f"Account Credential created: {accountName} \nusername: {username} \npassword: {password} ")
            print(":" *50)
            print("\n")
        elif short_code == "dc":
            if display_credentials():
                print(" list of your acounts: ")
                print("\n")
                print("_" * 50)
                for account in display_credentials():
                    print(f"Accountname => {account.accountName} \nUser Name => {username}\nPassword => {password}")
                    print("_" * 50)
                print("\n")
            else:
                print("You don't have a saved credentials ")
                print("\n")
        elif short_code == "d":
            print("Enter the username of the Credentials you want to delete\n")
            search_name = input().lower()
            if find_credentials(search_name):
                search_credential = find_credentials(search_name)
                print("_" * 35)
                search_credential.delete_credential()
                print("\n")
                print(f"Your stored credentials for {search_credential.username} successful deleted!")
                print("\n\n")
            else:
                print(" credential you want to delete does not exist in this app")
        elif short_code == "fc":
            print("Enter the username of the Credential you want to search for")
            search_username = input().lower()
            if exist_credentials(search_username):
                search_credential = find_credentials(search_username)
                print(f"Account Name => {search_credential.accountName}")
                print('\n')
                print('*'* 50)
                print(f"Username => {search_credential.username}")
                print(f"Password => {search_credential.password}")
                print('\n')
                print('*'* 50)
            else:
                print("That Credential does not exist")
                print('/n')       
        elif short_code == "gp":
            password = passwords_generate()
            print(f" password {password} has been generated.\n")
        elif short_code == "ex":
            print("Thanks for using Password-Locker")
            break
        else:
            print("please enter valid input!")
if __name__ == '__main__':
    Password-Locker()