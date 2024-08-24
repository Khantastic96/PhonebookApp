# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 20:49:44 2024

@author: Sharek Khan
"""

# Import modules
from asyncio.windows_events import NULL
from Entities import Phonebook, Record, User
from DAO import PhonebookDAO, RecordDAO, UserDAO

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
    record = Record()
    phonebook = Phonebook()

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
            while input_choice != EXIT:
                # Application logic
                main_menu()
                input_choice = int(input("INPUT (1-6): "))
                # Check input selection
                if input_choice == ADD:
                    # Add record logic
                    add_menu()
                    # Start code here
                    name = input("Enter name: ")
                    record.set_name(name)
                    
                    phone_number = input("Enter Phone Number: ")
                    record.set_phone_number(phone_number)
                    
                    email = input("Enter email: ")
                    record.set_email(email)
                    
                    address = input("Enter Address: ")
                    record.set_address(address)
                    
                    city = input("Enter city: ")
                    record.set_city(city)

                    province = input("Enter province/state: ")
                    record.set_province(province)

                    postal_code = input("Enter Postal Code/ZipCode: ")
                    record.set_postal_code(postal_code)
                    
                    dateofbirth = input("Enter Date of Birth: ")
                    record.set_date_of_birth(dateofbirth)
                    
                    phonebook.add_record(record)
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
                    
                    # End code here
                    print("Saving your changes and logging out.")
                    input("Press ENTER to continue...")
                elif input_choice == MODIFY:
                    # Modify record logic
                    modify_menu()
                    # Start code here
                    name = input("Search for the name of the person you want to fetch: ")
                    mod_record = phonebook.search_records(name)
                    
                    if mod_record != None :
                   
                        name = input("Enter name: ")
                        mod_record.set_name(name)
                    
                        phone_number = input("Enter Phone Number: ")
                        mod_record.set_phone_number(phone_number)
                    
                        email = input("Enter email: ")
                        mod_record.set_email(email)
                    
                        address = input("Enter Address: ")
                        mod_record.set_address(address)
                    
                        city = input("Enter city: ")
                        mod_record.set_city(city)

                        province = input("Enter province/state: ")
                        mod_record.set_province(province)

                        postal_code = input("Enter Postal Code/ZipCode: ")
                        mod_record.set_postal_code(postal_code)
                    
                        dateofbirth = input("Enter Date of Birth: ")
                        mod_record.set_date_of_birth(dateofbirth)
                        
                        phonebook.modify_record(mod_record)
                        
                    else :
                        input_choice == EXIT

                    # End code here
                    input("Press ENTER to continue...")
                elif input_choice == SEARCH:
                    # Search records logic
                    search_menu()
                    # Start code here
                    
                    # End code here
                    input("Press ENTER to continue...")
                elif input_choice == DELETE:
                    # Delete record logic
                    delete_menu()
                    # Start code here
                    
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
