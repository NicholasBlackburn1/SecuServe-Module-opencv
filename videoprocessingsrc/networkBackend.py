"""
this is where data will be sent from and recieved 
"""

import __init__ as init
import const
class NetworkManager(object):
    context = init.zmq.Context()
    controller = context.socket(init.zmq.SUB)
    def initnetwrok(self):
     
        self.controller.connect("tcp://"+const.zmqconfig['ip']+":"+const.zmqconfig['port'])
       
    
    """
    sends stats of opencv module over the network
    """
    def sendProgramStatus(self,prgstatus):
        init.consoleLog.Debug("sending prg status to rest of prgram") 
      
    
    """
    sends Dectected face name over the network
    """
    def sendDetectedFaceName(self,detectedNames):
        init.consoleLog.Debug("sending Faces  to rest of prgram") 
        
        
    
    """
    this is where the other modules
    """    
    def recvContronMessage(self):
        print(self.controller.recv_json())
    
    