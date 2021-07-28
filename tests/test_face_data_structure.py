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

       face.UserData.setUserName(face.UserData().__init__('nick',None,None,None,None))
     
       self.assertEquals(str('nick'),str(face.UserData.getUserName(face.UserData())),"should Return name ")
    


    """
    This is for only testing if data structure is valid
    """
    def test_data_structure_is_emtpy(self):
        data = face.UserData(None,None,None,None,None)
        self.assertEqual(data, face.UserData(None,None,None,None,None))

    
