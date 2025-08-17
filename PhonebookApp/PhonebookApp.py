# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 20:49:44 2024

@author: Sharek Khan
"""

# Import modules
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
    LOGIN = 1
    REGISTER = 2
    QUIT = 3

    ADD = 1
    LIST = 2
    EXIT = 3
    MODIFY = 4
    SEARCH = 5
    DELETE = 6

    # Initialize variables
    is_authenticated = False
    pre_input_choice = 0
    post_input_choice = 0

    # Intialize application
    while pre_input_choice != QUIT:
        pre_main_menu()
        try:
            pre_input_choice = int(input("INPUT (1-3): "))
        except ValueError:
            print("")
            print("Expected an integer value, got non-integer entry")
            input("Press ENTER to continue...")
            continue

        # Check input selection
        if pre_input_choice == LOGIN:
            # Login user
            login_menu()
            username = input("USERNAME: ")
            password = input("PASSWORD: ")

            # Authenticate with MongoDB cluster
            user_dao = UserDAO()
            is_authenticated = user_dao.authenticate_user(username, password)

            # Check login credentials
            if not is_authenticated:
                print("")
                print("ERROR: Login credentials invalid!")
                input("Press ENTER to continue...")
            else:
                # Cache user session
                try:
                    user = User()
                    user.set_user_id(user_dao.find_user(username)["_id"])
                    user.set_username(user_dao.find_user(username)["username"])
                    user.set_password(user_dao.find_user(username)["password"])
                except ValueError as ve:
                    print(ve)

                # Request for existing phonebook with MongoDB cluster
                phonebook_dao = PhonebookDAO()
                has_phonebook = phonebook_dao.has_phonebook(user.get_user_id())

                # Check for existing phonebook
                if not has_phonebook:
                    try:
                        phonebook = Phonebook()
                        phonebook.set_user(user)
                        phonebook.generate_phonebook_id()
                        phonebook_dao.insert_phonebook(user, phonebook)
                    except ValueError as ve:
                        print(ve)

                # Cache phonebook
                try:
                    phonebook = Phonebook()
                    phonebook.set_phonebook_id(phonebook_dao.find_phonebook(user.get_user_id())["_id"])
                    phonebook.set_user(user)
                except ValueError as ve:
                    print(ve)

                # Request for exisiting record(s) with MongoDB cluster
                record_dao = RecordDAO()
                has_records = record_dao.has_records(phonebook.get_phonebook_id())

                # Check for existing records
                if has_records:
                    # Cache records
                    collection = record_dao.find_records(phonebook.get_phonebook_id())

                    # Iterates through each document in MongoDB collection
                    for document in collection:
                        # Initialize a new record
                        try:
                            record = Record()
                            record.set_record_id(document["_id"])
                            record.set_phonebook_id(document["phonebook_id"])
                            record.set_name(document["name"])
                            record.set_phone_number(document["phone_number"])
                            record.set_email(document["email"])
                            record.set_address(document["address"])
                            record.set_city(document["city"])
                            record.set_province(document["province"])
                            record.set_postal_code(document["postal_code"])
                            record.set_date_of_birth(document["date_of_birth"])
                        except ValueError as ve:
                            print(ve)

                        # Adds record to current phonebook registry
                        phonebook.add_record(record)

                # Reset post_input_choice
                post_input_choice = 0

                # Run Phonebook application
                while post_input_choice != EXIT:
                    # Application logic
                    post_main_menu()
                    try:
                        post_input_choice = int(input("INPUT (1-6): "))
                    except ValueError:
                        print("")
                        print("Expected an integer value, got non-integer entry")
                        input("Press ENTER to continue...")
                        continue

                    # Check input selection
                    if post_input_choice == ADD:
                        # Add record logic and initialize a new record
                        add_menu()
                        record = Record()
                        record.generate_record_id(phonebook.get_phonebook_id(), len(phonebook.get_records()) + 1)
                        record.set_phonebook_id(phonebook.get_phonebook_id())
                        validate_input("Enter NAME: ", record.set_name)
                        validate_input("Enter PHONE NUMBER: ", record.set_phone_number)
                        validate_input("Enter EMAIL: ", record.set_email)
                        validate_input("Enter ADDRESS: ", record.set_address)
                        validate_input("Enter CITY: ", record.set_city)
                        validate_input("Enter PROVINCE: ", record.set_province)
                        validate_input("Enter POSTAL CODE: ", record.set_postal_code)
                        validate_input("Enter D.O.B (dd/mm/yyyy): ", record.set_date_of_birth)

                        # Check if new record is a duplicate of existing record
                        if (phonebook.is_duplicate(record)):
                            print("")
                            print("...Duplicate entry not allowed!")
                        else:
                            # Save locally on cached list
                            phonebook.add_record(record)
                            # Save remotely on the MongoDB cluster
                            record_dao.insert_record(record)
                            print("")
                            print("...Record added!")
                        input("Press ENTER to continue...")
                    elif post_input_choice == LIST:
                        # List records logic
                        list_menu()
                        phonebook.list_records()
                        print("")
                        input("Press ENTER to continue...")
                    elif post_input_choice == EXIT:
                        # Exit and clear session fields
                        print("")
                        print("...Saving your changes and logging out.")
                        is_authenticated = False
                        user = None
                        phonebook = None
                        input("Press ENTER to continue...")
                    elif post_input_choice == MODIFY:
                        # Modify record logic
                        modify_menu()
                        name = input("Enter NAME: ")
                        records = phonebook.search_records_by_name(name)
                        
                        # Check if records exist
                        if len(records) > 0:
                            index = 0
                            # Multiple records returned
                            if len(records) > 1:
                                # Determine which specific record to modify
                                for i in range(0, len(records)):
                                    print("%d. %s" % (i+1, records[i].get_name()))
                                try:
                                    print("")
                                    index = int(input("Which record do you want to modify (1-%d): " % (len(records)))) - 1
                                except ValueError:
                                    print("")
                                    print("Expected an integer value, got non-integer entry")
                                    input("Press enter to continue...")
                                    continue
                            
                            # Check input selection
                            if index >= 0 and index < len(records):
                                # Reinitialize existing record
                                validate_input("Enter NEW NAME: ", records[index].set_name)
                                validate_input("Enter NEW PHONE NUMBER: ", records[index].set_phone_number)
                                validate_input("Enter NEW EMAIL: ", records[index].set_email)
                                validate_input("Enter NEW ADDRESS: ", records[index].set_address)
                                validate_input("Enter NEW CITY: ", records[index].set_city)
                                validate_input("Enter NEW PROVINCE: ", records[index].set_province)
                                validate_input("Enter NEW POSTAL CODE: ", records[index].set_postal_code)
                                validate_input("Enter NEW D.O.B (dd/mm/yyyy): ", records[index].set_date_of_birth)
                                                            
                                # Update locally on cached list
                                phonebook.modify_record(records[index])
                                # Update remotely on the MondoDB cluster
                                record_dao.update_record(records[index])
                                print("")
                                print("...Record modified!")
                            else:
                                # Invalid entry
                                print("")
                                print("Expected an integer from the options provided, got invalid entry")
                        else:
                            print("")
                            print("...Record not found")
                        input("Press ENTER to continue...")
                    elif post_input_choice == SEARCH:
                        # Search records logic
                        search_menu()
                        name = input("Enter NAME: ")
                        records = phonebook.search_records_by_name(name)

                        # Check if record(s) exists
                        if len(records) > 0:
                            for record in records:
                                print(record)
                                print("")
                        else:
                            print("")
                            print("...Record not found!")
                        input("Press ENTER to continue...")
                    elif post_input_choice == DELETE:
                        # Delete record logic
                        delete_menu()
                        name = input("Enter NAME: ")
                        records = phonebook.search_records_by_name(name)
                        
                        # Check if records exist
                        if len(records) > 0:
                            index = 0
                            # Multiple records returned
                            if len(records) > 1:
                                # Determine which specific record to delete
                                for i in range(0, len(records)):
                                    print("%d. %s" % (i+1, records[i].get_name()))
                                try:
                                    print("")
                                    index = int(input("Which record do you want to delete (1-%d): " % (len(records)))) - 1
                                except ValueError:
                                    print("")
                                    print("Expected an integer value, got non-integer entry")
                                    input("Press enter to continue...")
                                    continue
                            
                            # Check input selection
                            if index >= 0 and index < len(records):
                                # Confirm deletion
                                confirm = input("CONFIRM DELETION? (Y/N): ")
                                if confirm.upper() == "Y":
                                    # Delete locally on cached list
                                    phonebook.delete_record(records[index])
                                    # Delete remotely on the MondoDB cluster
                                    record_dao.delete_record(records[index])
                                    print("")
                                    print("...Record deleted!")
                                else:
                                    print("")
                                    print("...Deletion aborted!")
                            else:
                                # Invalid entry
                                print("")
                                print("Expected an integer from the options provided, got invalid entry")
                        else:
                            print("")
                            print("...Record not found")
                        input("Press ENTER to continue...")
                    else:
                        # Invalid entry
                        print("")
                        print("Expected an integer from the options provided, got invalid entry")
                        input("Press ENTER to continue...")
        elif pre_input_choice == REGISTER:
            # Register new user
            register_menu()
            user = User()
            user_dao = UserDAO()
            
            # Get validated input for User fields
            validate_input("Enter FIRST NAME: ", user.set_first_name)
            validate_input("Enter LAST NAME: ", user.set_last_name)
            validate_input("Enter PHONE NUMBER: ", user.set_phone_number)
            # Iterate until input is validated and meets conditions
            while True:
                validate_input("Enter USERNAME: ", user.set_username)
                if user_dao.find_user(user.get_username()) is not None:
                    print("...Username already exists!!")
                else:
                    break
            # Continue getting validated input for User fields
            validate_input("Enter PASSWORD: ", user.set_password)
            user.generate_user_id()

            # Register with MongoDB cluster
            if user_dao.insert_user(user) == 1:
                print("")
                print("...User registered!")
            else:
                print("")
                print("...User not registered!")
            input("Press ENTER to continue...")
        elif pre_input_choice == QUIT:
            # Quit the application
            print("")
            print("...Quitting application!")
        else:
            # Invalid entry
            print("")
            print("Expected an integer from the options provided, got invalid entry")
            input("Press ENTER to continue...")

# Define the input validation function
def validate_input(str_prompt, mutator_method):
    while True:
        try:
            input_value = input(str_prompt)
            mutator_method(input_value)
            return input_value
        except ValueError as ve:
            print(ve)

# Define the menu header function
def menu_header():
    print(CLEAR_SCREEN, end="")
    print("**********WELCOME TO PHONEBOOK**********")

# Define the menu footer function
def menu_footer():
    print("")
    print("****************************************")

# Define the pre-authentication main menu function
def pre_main_menu():
    menu_header()
    print("                 MENU")
    print("")
    print("    1.Login    2.Register    3.Quit")
    menu_footer()

# Define the login menu function
def login_menu():
    menu_header()
    print("                 LOGIN")
    menu_footer()

# Define the register menu function
def register_menu():
    menu_header()
    print("                REGISTER")
    print("")
    print("*NOTE: Name + Phone Number will NOT be")
    print("stored or housed on the server, only")
    print("used for processing server data!")
    menu_footer()

# Define the post-autentication main menu function
def post_main_menu():
    menu_header()
    print("                 MENU")
    print("")
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
