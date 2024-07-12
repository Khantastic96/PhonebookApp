# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:02:55 2024

@author: Sharek Khan
"""

class User:
    # Define the init method/class constructor
    def __init__(self, username, password):
        self.set_username(username)
        self.set_password(password)

    # Define the accessor to the username field
    def get_username(self):
        return self.__username

    # Define the accessor to the password field
    def get_password(self):
        return self.__password

    # Define the mutator to the username field
    def set_username(self, new_username):
        self.__username = new_username

    # Define the mutator to the password field
    def set_password(self, new_password):
        self.__password = new_password
