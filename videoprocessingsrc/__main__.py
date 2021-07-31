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
    
    
    # loops to recv json message
    while True:
        #if(controller.recv_json() == {"controller":"start"}):
        imports.consoleLog.Warning("running VideoProcessing Pipeline...")

        # this is the setup state in pipeline 
        pipelineStates.PipeLine.on_event( pipelineStates.PipeLine(),pipelineStates.States.SETUP_PIPELINE)
    
        
        
    
    
                
            
if __name__ == "__main__":
    main()
