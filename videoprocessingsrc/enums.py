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
    CURRENT_STATE = None,
    SETUP_PIPELINE= 'SETUP_PIPELINE',
    TRAIN_MODEL = 'TRAIN_PIPELINE',
    RECOGNIZE_FACES = 'RECOGNIZING_FACES',
    RECOGNIZE_FACES_RUNNING ='RUNNING',
    IDLE = 'IDLE',
    ERROR = 'ERROR',
    STAGE_COMPLETE = 'STAGE COMPLETE'
  
    
    
    # sets current state of state macheene
    def set_State(self,state):
        self.CURRENT_STATE = state
        
        
    def getCurrentState(self):
        return self.CURRENT_STATE