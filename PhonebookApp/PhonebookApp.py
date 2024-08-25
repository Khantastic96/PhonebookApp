# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 20:49:44 2024

@author: Sharek Khan
"""

# Import modules
from asyncio.windows_events import NULL
from Entities.Phonebook import Phonebook
from Entities.Record import Record
from Entities.User import User
from DAO.PhonebookDAO import PhonebookDAO
from DAO.RecordDAO import RecordDAO
from DAO.UserDAO import UserDAO

# Define global constants
CLEAR_SCREEN = "\033[H\033[J"

# Define the main function
def main():
    # Define local CONSTANTS
    ADD = 1
    LIST = 2
    EXIT = 3
    MODIFY = 4
    SEARCH = 5
    DELETE = 6
    
    # Initialize variables
    username = ""
    password = ""
    is_authenticated = False
    input_choice = 0

    # Authenticate user
    while is_authenticated != True:
        # Login logic
        login_menu()
        username = input("USERNAME: ")
        password = input("PASSWORD: ")
        
        # Authenticate
        is_authenticated = True
        
        # Check login credentials
        if is_authenticated != True:
            print("ERROR: Login credentials invalid!")
            input("Press ENTER to continue...")
        else:
            # Run through application
            phonebook = Phonebook()
            while input_choice != EXIT:
                # Application logic
                main_menu()
                input_choice = int(input("INPUT (1-6): "))
                # Check input selection
                if input_choice == ADD:
                    # Add record logic
                    add_menu()
                    # Start code here
                    name = input("Enter NAME: ")
                    phone_number = input("Enter PHONENUMBER: ")
                    email = input("Enter EMAIL: ")
                    address = input("Enter ADDRESS: ")
                    city = input("Enter CITY: ")
                    province = input("Enter PROVINCE: ")
                    postal_code = input("Enter POSTAL CODE: ")
                    date_of_birth = input("Enter D.O.B (dd/mm/yyy): ")
                    
                    record = Record()
                    record.set_name(name)                    
                    record.set_phone_number(phone_number)
                    record.set_email(email)
                    record.set_address(address)
                    record.set_city(city)
                    record.set_province(province)
                    record.set_postal_code(postal_code)
                    record.set_date_of_birth(date_of_birth)
                    
                    phonebook.add_record(record)
                    print("... Record added!")
                    # End code here
                    input("Press ENTER to continue...")
                elif input_choice == LIST:
                    # List records logic
                    list_menu()
                    # Start code here
                    phonebook.list_records()
                    # End code here
                    input("Press ENTER to continue...")
                elif input_choice == EXIT:
                    # Exit logic
                    # Start code here
                    is_authenticated = False
                    # End code here
                    print("Saving your changes and logging out.")
                    input("Press ENTER to continue...")
                elif input_choice == MODIFY:
                    # Modify record logic
                    modify_menu()
                    # Start code here
                    name = input("Enter NAME: ")
                    record = phonebook.search_records(name)
                    
                    if record != None:
                        name = input("Enter NEW NAME: ")
                        phone_number = input("Enter NEW PHONENUMBER: ")
                        email = input("Enter NEW EMAIL: ")
                        address = input("Enter NEW ADDRESS: ")
                        city = input("Enter NEW CITY: ")
                        province = input("Enter NEW PROVINCE: ")
                        postal_code = input("Enter NEW POSTAL CODE: ")
                        date_of_birth = input("Enter NEW D.O.B (dd/mm/yyyy): ")
                        
                        record.set_name(name)
                        record.set_phone_number(phone_number)
                        record.set_email(email)
                        record.set_address(address)
                        record.set_city(city)
                        record.set_province(province)
                        record.set_postal_code(postal_code)
                        record.set_date_of_birth(date_of_birth)
                        
                        phonebook.modify_record(record)
                        print("... Record updated!")
                    else :
                        print("... Record not found!")
                    # End code here
                    input("Press ENTER to continue...")
                elif input_choice == SEARCH:
                    # Search records logic
                    search_menu()
                    # Start code here
                    name = input("Enter NAME: ")
                    record = phonebook.search_records(name)
                    
                    if record != None:
                        print(record)
                    else:
                        print("... Record not found!")
                    # End code here
                    input("Press ENTER to continue...")
                elif input_choice == DELETE:
                    # Delete record logic
                    delete_menu()
                    # Start code here
                    name = input("Enter NAME: ")
                    record = phonebook.search_records(name)
                    
                    if record != None:
                        phonebook.delete_record(record)
                        print("... Record deleted!")
                    else:
                        print("... Record not found!")
                    # End code here
                    input("Press ENTER to continue...")
                else:
                    # Invalid entry
                    print("ERROR: Invalid entry!")
                    print("Please enter a number from the range specified.")
                    input("Press ENTER to continue...")
                
# Define the menu header function
def menu_header():
    print(CLEAR_SCREEN, end="")
    print("**********WELCOME TO PHONEBOOK**********")
    
# Define the menu footer function
def menu_footer():
    print("")
    print("****************************************")
    
# Define the login menu function
def login_menu():
    menu_header()
    print("                 LOGIN")
    menu_footer()
    
# Define the main menu function
def main_menu():
    menu_header()
    print("                 MENU")
    print("    1.Add         2.List      3.Exit")
    print("    4.Modify      5.Search    6.Delete")
    menu_footer()    

# Define the add record menu function
def add_menu():
    menu_header()
    print("                ADD NEW")
    menu_footer()
    
# Define the list records menu function
def list_menu():
    menu_header()
    print("                 LIST")
    menu_footer()
    
# Define the modify record menu function
def modify_menu():
    menu_header()
    print("                MODIFY")
    menu_footer()
    
# Define the search records menu function
def search_menu():
    menu_header()
    print("                SEARCH")
    menu_footer()
    
# Define the delete record menu function
def delete_menu():
    menu_header()
    print("                DELETE")
    menu_footer()

# Invoke the main function
main()
