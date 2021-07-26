"""
this is the file holds module wide enums 
"""

import enum

# allows to easyly share user staus without need of a string 

class UserStatus(enum.Enum):
    ADMIN = 'Admin',
    USER = 'User',
    UNWANTED = 'Unwanted',
    UNKNOWN  ='unknown'
    
    
class PipeLineStates(enum.Enum):
    SETUP = 'SETUP',
    TRAIN_MODEL = 'TRAIN_PIPELINE',
    RECOGNIZE_FACES = 'RECOGNIZING_FACES',
    IDLE = 'IDLE',
    ERROR = 'ERROR'
    