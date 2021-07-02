"""
This class is for running my video pipeline 
"""
import __init__




def main():
    #send_data = socketsend.send_json(None)
    print("in Main program")
    
    __init__.console_Log.Debug("Starting the Pipe Line via Controller")

    while True: 
        __init__.console_Log.PipeLine_Ok("data from zmq TODO")
        #if(__init__.NetworkManager.recvContronMessage() == {"controller": "Start"} ):
        if(True):
            __init__.videoRequired.RequiredCode.setupPipeline(__init__.videoRequired.RequiredCode())
            
            
if __name__ == "__main__":
    main()
