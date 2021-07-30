"""
This class is for running my video pipeline 
TODO: add code to launc from zmq
"""
import imports



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

    # loops to recv json message
    while controller.recv_json() == None:
        if(controller.recv_json() == {"controller":"start"}):
            imports.consoleLog.Warning("running VideoProcessing Pipeline...")

            # this is the setup state in pipeline 
            if(imports.enums.PipeLineStates.getCurrentState(imports.enums.PipeLineStates()) == imports.enums.PipeLineStates.SETUP):
                imports.consoleLog.Warning("in state:"+str(imports.enums.PipeLineStates.getCurrentState(imports.enums.PipeLineStates())))
                imports.pipeline.RequiredCode.setupPipeline(imports.pipeline.RequiredCode(),sender)
                imports.enums.PipeLineStates.set_State(imports.enums.PipeLineStates(),imports.enums.PipeLineStates().TRAIN_MODEL)
            
            # this is the TrainModel State in Pipeline
            if(imports.enums.PipeLineStates.getCurrentState(imports.enums.PipeLineStates()) == imports.enums.PipeLineStates.TRAIN_MODEL):
                imports.consoleLog.Warning("in state:"+str(imports.enums.PipeLineStates.getCurrentState(imports.enums.PipeLineStates())))
                imports.pipeline.RequiredCode.trainPipeLine(imports.pipeline.RequiredCode(),sender)
                imports.enums.PipeLineStates.set_State(imports.enums.PipeLineStates(),imports.enums.PipeLineStates().RECOGNIZE_FACES)
                
                
                        # this is the TrainModel State in Pipeline
            if(imports.enums.PipeLineStates.getCurrentState(imports.enums.PipeLineStates()) == imports.enums.PipeLineStates.RECOGNIZE_FACES):
                imports.consoleLog.Warning("in state:"+str(imports.enums.PipeLineStates.getCurrentState(imports.enums.PipeLineStates())))
                imports.pipeline.RequiredCode.reconitionPipeline(imports.pipeline.RequiredCode(),sender)
                
        
                
                
            
if __name__ == "__main__":
    main()
