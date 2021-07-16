""" 
this file is for testing the datasturue for handing faces
#author Nicholas 
"""
import unittest
import videoprocessingsrc.faceDataStruture as face
class TestFaceData(unittest.TestCase):
    
    """
    This is for only testing if data structure is valid
    """
    def test_data_structure(self):
        data = face.faceDataStruture.UserData("name","unknown","\null\image.jpg","example.com","5555555")
        self.assertEqual(data, face.faceDataStruture.UserData("name","unknown","\null\image.jpg","example.com","5555555"))
    


