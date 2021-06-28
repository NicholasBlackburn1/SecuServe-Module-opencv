""" 
this file is for testing the datasturue for handing faces
#author Nicholas 
To make tests think about black box reverse enginnering only what inputs and what out puts are required/ expected
"""
import unittest
from videoprocessingsrc import knnClasifiyer
import __init__
class TestKnnClass(unittest.TestCase):
    
    """
    This is for only testing if kkn clasifiyer is not none as it is done training
    """
    def test_training_knn_clasifiyer(self):
        data= knnClasifiyer.train(train_dir=__init__.TEST_TRAIN_DIR,model_save_path=__init__.TEST_TRAIN_DIR+"test.model",n_neighbors=2)
        self.assertIsNotNone(data)
        
        
    """
    this will test trained test knn classifiyer aginst a known image UwU
    """
    def test_read_knn_classifiyer(self):
        
        predict = knnClasifiyer.predict(__init__.READIMAGE, model_path=__init__.TEST_TRAIN_DIR+"test.model", distance_threshold=0.65)
        self.assertEqual(predict,[('me', (145, 312, 287, 170))])