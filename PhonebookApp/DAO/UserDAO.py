# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 16:05:44 2024

@author: Sharek Khan
"""

# Import modules
from Entities import User

class UserDAO:
    # Define the init method/class constructor
    def __init__(self):
        self.__user = User()
        
    # Define the method to insert a new user entry to the database
    def insert_user(self):
        # Insertion logic
        return 1
    
    # Define the method to find an existing user entry in the database
    def find_user(self):
        # Querying logic
        return 1
    
    # Define the method to update an existing user entry in the database
    def update_user(self):
        # Updating logic
        return 1
    
    # Define the method to delete an existing user entry from the database
    def delete_user(self):
        # Deleting logic
        return 1