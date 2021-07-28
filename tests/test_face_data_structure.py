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
    def test_data_structure_user_name_(self):

       data =face.UserData(name="nick", status='user', image="image",downloadurl="https://example.com", phonenumber=4123891615)
       self.assertEqual(str("nick"),str(face.UserData.getUserName(data)),"should Return name ")
    

    
