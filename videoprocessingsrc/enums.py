"""
this is the file holds module wide enums 
"""

import enum

class UserStatus(enum.Enum):
    ADMIN = 'Admin',
    USER = 'User',
    UNWANTED = 'Unwanted',
    UNKNOWN  ='unknown'
    