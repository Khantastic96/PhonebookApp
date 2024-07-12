# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 20:49:44 2024

@author: Sharek Khan
"""

# Import modules
from Entities import Phonebook
from Entities import User
from Entities import Record
from DAO import PhonebookDAO
from DAO import UserDAO

# Define the main function
def main():
    # Do something here...
    print("Hello World!")
        
# Define the menu header function
def menu_header():
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
    print("    1.Add New     2.List      3.Exit")
    print("    4.Modify      5.Search    6.Delete")
    menu_footer()    

# Invoke the main function
main()