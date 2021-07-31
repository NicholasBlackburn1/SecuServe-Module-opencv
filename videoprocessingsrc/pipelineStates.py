"""
this is the file holds the Pipeline and controls Pipline
"""
import videoRequired

class States():
    IDLE = 0
    SETUP_PIPELINE = 1
    TRAIN_MODEL = 2
    RUN_RECONITION = 4
    ERROR = 5

class Pipeline:
    current : int
    
      
    # returns the current state of the piplien
    def current_state(self):
        return self.current
    
    def set_state(self,state):
        self.current = state
        
    def runPipeLine(self, start_state, sender):
       
        self.current = start_state
        if(self.current == States.SETUP_PIPELINE):
            print(self.current_state())
            videoRequired.RequiredCode.setupPipeline(videoRequired.RequiredCode(),sender)
            self.current = States.TRAIN_MODEL
            
        if(self.current == States.TRAIN_MODEL):
            print(self.current_state())
            videoRequired.RequiredCode.trainPipeLine(videoRequired.RequiredCode(),sender)
            self.current = States.RUN_RECONITION
            
        if(self.current == States.RUN_RECONITION):
            watchdog+=1
            print("in Reconitoon")
            videoRequired.RequiredCode.reconitionPipeline(videoRequired.RequiredCode(),sender)
            
            
        if(self.current == States.IDLE):
            print("in idle")
            self.current = States.ERROR
            
        if(self.current == States.ERROR):
            print("in ERROR")
            
  
                

            
                