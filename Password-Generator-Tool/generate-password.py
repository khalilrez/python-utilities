#!/usr/bin/env python3
import random
import pyperclip
import os

def showPasswords():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nPASSWORDS---------------------------------\n")
    with open("passwords.txt", "r") as f:
        passwords = f.readlines()
    for password in passwords:
        print(password)
    print("------------------------------------------\n ")
    input("Press Any key to return to main menu")


def searchPassword():
    os.system('cls' if os.name == 'nt' else 'clear')
    with open("passwords.txt", "r") as f:
        passwords = f.readlines()
    search = input("Which password would you like to search for? ")
    print("\nPASSWORD(S) MATCHING : "+search+"  ---------------------------------\n")
    for password in passwords:
       if password.startswith(search):
            print(password)
    print("------------------------------------------\n ")

def deletePassword():
    os.system('cls' if os.name == 'nt' else 'clear')
    with open("passwords.txt", "r") as f:
        passwords = f.readlines()
        for password in passwords:
            print(password)
        delete = input("Which password would you like to delete? ")
        with open("passwords.txt", "w") as f:
            for password in passwords:
                if not password.startswith(delete):
                    f.write(password)
                    print("Done!")
                    
                
def store_password(password):
    with open("passwords.txt", "a") as f:
        f.write(password+"\n")

def passwordGenerator():
    os.system('cls' if os.name == 'nt' else 'clear')
    id = input("Which account is this password for? ")
    if id == "":
        id = "------ unspecified ------"
    length = int(input("How many characters would you like your password to be? "))
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print("\n\nYOUR GENERATED PASSWORD ----------------- \n")
    print("Your password is: \033[0;32m"+password)
    print("\033[0;38m")    
    print("\nIdentified by: \033[0;32m"+id)
    print("\033[0;38m")
    pyperclip.copy(password)
    print("-----------------HAS BEEN COPIED TO YOUR CLIPBOARD\n\n")
    store = input("Would you like to store this password? (y/n) ")
    if store == "y":
        store_password(id+":"+password)
        print("Password stored!")
    else:
        print("Password not stored!")
    



chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
os.system('cls' if os.name == 'nt' else 'clear')
welcome = input("Welcome to my Password Generator! Press enter to continue.")

exit = False
passwords = []
while not exit:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
        ************** MAIN MENU ***********
        *   1. Generate Password           *
        *   2. View All Passwords          * 
        *   3. Delete Password             *
        *   4. Search Password             *
        *   0. Exit                        *
        ************************************
    ''''')
    choice = input("What would you like to do? ")
    if choice == "1":
        passwordGenerator()
    elif choice == "2":
        showPasswords()
    elif choice == "3":
        deletePassword()
    elif choice == "4":
        searchPassword()
    elif choice == "0":
        exit = True
