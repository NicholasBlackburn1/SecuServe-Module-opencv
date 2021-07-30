"""
this is the file holds the Pipeline FSM wide enums 
"""


class PipeLineFSM:
    curState = None
    
    IDLE = 0,
    SETUP_PIPELINE = 1,
    TRAIN_MODEL = 2,
    INIT_RECONITION =3, 
    RUN_RECONITION = 4,
    ERROR = 5
    
    # sets current state of pipeline
    def setCurrentState(self,state):
        self.curState = state
        
        
    
  