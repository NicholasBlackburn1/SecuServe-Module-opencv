"""
This class is for running my video pipeline 
TODO: add code to launc from zmq
"""

import imports
import pipelineStates

            

def main():
    imports.consoleLog.Warning("Initing zmq")
    context = imports.zmq.Context()
    sender = context.socket(imports.zmq.PUB)
    
    controller = context.socket(imports.zmq.SUB)
    controller.setsockopt(imports.zmq.SUBSCRIBE, b'')
    
    sender.bind("tcp://"+"127.0.0.1:5001")
    controller.connect("tcp://"+"127.0.0.1:5000")
    
    imports.consoleLog.PipeLine_Ok("running zmq")
    imports.consoleLog.Debug("Waiting for Zmq to recv Control Message...")
    watchdog = 0
    
    pipeline = pipelineStates.PipeLine()
    
    # loops to recv json message

    #if(controller.recv_json() == {"controller":"start"}):
    imports.consoleLog.Warning("running VideoProcessing Pipeline...")

    pipeline.on_event(pipelineStates.States.SETUP_PIPELINE)
    pipeline.on_event(pipelineStates.States.TRAIN_MODEL)
    pipeline.on_event(pipelineStates.States.RUN_RECONITION)

   


        
    
    
                
            
if __name__ == "__main__":
    main()
