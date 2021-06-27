""" 
this file is for testing the datasturue for handing faces
#author Nicholas 
"""
import unittest
from videoprocessingsrc import faceDataStruture

class TestFaceData(unittest.TestCase):
    
    """
    This is for only testing if data structure is valid
    """
    def test_data_structure(self):
        data = faceDataStruture.UserData("name","unknown","\null\image.jpg","example.com","5555555")
        self.assertEqual(data, faceDataStruture.UserData("name","unknown","\null\image.jpg","example.com","5555555"))
        
    

