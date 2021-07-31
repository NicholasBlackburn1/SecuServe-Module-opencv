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
    The state which Sets Up Whole opencv pipeline
    """

    def on_event(self, event):
        if event == States.SETUP_PIPELINE:
            videoRequired.RequiredCode.setupPipeline(videoRequired.RequiredCode())
            return TrainPipeline()

        return self


class TrainPipeline(State):
    """
    The state which Trains the Reconized face Models
    """

    def on_event(self, event):
        if event == States.TRAIN_MODEL:
            videoRequired.RequiredCode.trainPipeLine(videoRequired.RequiredCode())
            return RunReconitionPipeLine()

        return self
    
    
class RunReconitionPipeLine(State):
    """
    The state which Reconizes Faces
    """

    def on_event(self, event):
        if event == States.RUN_RECONITION:
            videoRequired.RequiredCode.reconitionPipeline(videoRequired.RequiredCode())
            return 

        return self


class Idle(State):
    """
    The state which The program waits for a face to be spotted 
    """

    def on_event(self, event):
        if event == States.IDLE:
            return #TODO: add pipeline trained models

        return self
    

class PipeLine(object):
    """ 
    A simple state machine that mimics the functionality of a device from a 
    high level.
    """

    def __init__(self):
        """ Initialize the components. """

        # Start with a default state.
        self.state =SetupPipeLine()

    def on_event(self, event):
        """
        This is the bread and butter of the state machine. Incoming events are
        delegated to the given states which then handle the event. The result is
        then assigned as the new state.
        """

        # The next state will be the result of the on_event function.
        self.state = self.state.on_event(event)

            
                