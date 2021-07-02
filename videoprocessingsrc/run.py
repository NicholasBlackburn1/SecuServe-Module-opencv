"""
This class is for running my video pipeline 
"""
import __init__



#send_data = socketsend.send_json(None)
print("hello")
__init__.consoleLog.Debug("Starting the Pipe Line via Controller")

while True: 
    __init__.consoleLog.PipeLine_Ok(str(__init__.NetworkManager.recvContronMessage()))
    if(__init__.NetworkManager.recvContronMessage() == {"controller": "Start"} ):
        __init__.videoRequired.RequiredCode.setupPipeline(__init__.videoRequired.RequiredCode())
        
        
        