"""
this is the file holds the Pipeline and controls Pipline
watch dog count to frozen 
"""
import videoRequired

from state import State


class States():
    IDLE = 0
    SETUP_PIPELINE = 1
    TRAIN_MODEL = 2
    RUN_RECONITION = 4
    ERROR = 5

# Start of our states
class SetupPipeLine(State):
    """
    The state which indicates that there are limited device capabilities.
    """

    def on_event(self, event):
        if event == States.SETUP_PIPELINE:
            videoRequired.RequiredCode.setupPipeline(videoRequired.RequiredCode())
            return TrainPipeline()

        return self


class TrainPipeline(State):
    """
    The state which indicates that there are no limitations on device
    capabilities.
    """

    def on_event(self, event):
        if event == States.TRAIN_MODEL:
            
            return RunReconitionPipeLine()

        return self
    
    
class RunReconitionPipeLine(State):
    """
    The state which indicates that there are limited device capabilities.
    """

    def on_event(self, event):
        if event == States.RUN_RECONITION:
            return 

        return self


class Idle(State):
    """
    The state which indicates that there are no limitations on device
    capabilities.
    """

    def on_event(self, event):
        if event == States.IDLE:
            return #TODO: add pipeline trained models

        return self

class Pipeline:
    current : int
    nextState: int 
      
    # returns the current state of the piplien
    def current_state(self):
        return self.current
    
    def set_state(self,state):
        self.current = state
        
    def runPipeLine(self, start_state, sender):
       pass
   
   
   

            
                