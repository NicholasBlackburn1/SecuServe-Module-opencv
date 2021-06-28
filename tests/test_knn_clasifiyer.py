""" 
this file is for testing the datasturue for handing faces
#author Nicholas 
To make tests think about black box reverse enginnering only what inputs and what out puts are required/ expected
"""
import unittest
from videoprocessingsrc import knnClasifiyer

class TestKnnClass(unittest.TestCase):
    
    """
    This is for only testing if kkn clasifiyer is not none as it is done training
    """
    def test_training_knn_clasifiyer(self):
        data= knnClasifiyer.train(train_dir="data/",model_save_path="test.model",n_neighbors=2)
        self.assertIsNotNone(data)
        
        
    """
    this will test trained test knn classifiyer aginst a known image UwU
    """
    def test_read_knn_classifiyer(self):
        pass