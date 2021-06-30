"""
this is where data will be sent from and recieved 
"""

import __init__

class NetworkManager(object):
    
    """
    sends stats of opencv module over the network
    """
    def sendProgramStatus(self,prgstatus):
        __init__.consoleLog.Debug("sending prg status to rest of prgram") 
        __init__.send_data({"prgstats": str(prgstatus)})
    
    """
    sends Dectected face name over the network
    """
    def sendDetectedFaceName(self,detectedNames):
        __init__.consoleLog.Debug("sending Faces  to rest of prgram") 
        __init__.send_data({"dectected": str(detectedNames)})
        
    
    
    """
    this is where the other modules
    """    
    def recvContronMessage(self):
        return __init__.recv_command