"""
this is the file holds the Pipeline FSM wide enums 
"""
from typing import Counter

import imports

class States:
    IDLE = 0
    SETUP_PIPELINE = 1
    TRAIN_MODEL = 2
    INIT_RECONITION =3 
    RUN_RECONITION = 4
    ERROR = 5


class State(object):
    """
    We define a state object which provides some utility functions for the
    individual states within the state machine.
    """

    def __init__(self):
        print ('Processing current state:', str(self))

    def on_event(self, event,sender):
        """
        Handle events that are delegated to this State.
        """
        pass

    def __repr__(self):
        """
        Leverages the __str__ method to describe the State.
        """
        return self.__str__()

    def __str__(self):
        """
        Returns the name of the State.
        """
        return self.__class__.__name__
    
# this is for seting up the pipeline
class SetupState(State):
    def on_event(self, event,sender):
        if event == States.SETUP_PIPELINE:
            imports.pipeline.RequiredCode.setupPipeline(imports.pipeline.RequiredCode(),sender)
            return UnlockedState()

        return self
        

  