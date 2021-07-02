"""
This class is for running my video pipeline 
"""
import __init__




def main():

    __init__.consoleLog.Debug("Starting the Pipe Line via Controller")
    
    while True:
        
        if(__init__.NetworkManager.recvContronMessage == {"controller": "Start"} ):
            __init__.videoRequired.RequiredCode.setupPipeline(__init__.videoRequired.RequiredCode())