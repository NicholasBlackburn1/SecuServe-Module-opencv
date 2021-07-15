"""
Tests The Pipeline Using Mocks
TODO: what does set up correctly mean? -> me anseer

TODO: TEST DRIVEN DEV For Setup of pipe line 

 read config file 
 read config file if none create one
  
 check config file for requrid entrys 
 check config file has no entrys create some 
 
 check to see if basic file strucure is set up 
 check to see if basic file strucure is not setup set it up
 
 Connects to database and see if the data is not null and returns the userData
 Connects to database and see if the data is null reread data
 Checks to see if data was added to database
 
 loads up all trained models
 loads up all trained models if correpet retrain it
 
 
 
 
 Create and fill the UserDataList 
"""
import unittest
from unittest.mock import Mock


class TestCVPipeline(unittest.TestCase):
    
    mock = Mock()
     
    """
    Mocks and tests  Setup of pipe line
    """
    def Test_Pipeline_Setup(self):
        pass