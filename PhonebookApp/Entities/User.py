# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:02:55 2024

@author: Sharek Khan
"""


class User:
    # Define the init method/class constructor
    def __init__(self, username, password):
        self._username = username
        self._password = password

    # Define the accessor to the username field
    def getUsername(self):
        return self._username

    # Define the accessor to the password field
    def getPassword(self):
        return self._password

    # Define the mutator to the username field
    def setUsername(self, newUsername):
        self._username = newUsername

    # Define the mutator to the password field
    def setPassword(self, newPassword):
        self._password = newPassword
