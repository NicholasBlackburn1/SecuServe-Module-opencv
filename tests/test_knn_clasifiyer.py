""" 
this file is for testing the datasturue for handing faces
#author Nicholas 
"""
import unittest
from videoprocessingsrc import knnClasifiyer

class TestKnnClass(unittest.TestCase):
    
    """
    This is for only testing if kkn clasifiyer is acutally returns json data
    """
    def test_training_knn_clasifiyer(self):
        data = knnClasifiyer.train(train_dir="data/",model_save_path="test.model",n_neighbors=2)
        
        #self.asset_equles(data,knnClasifiyer.train(train_dir="data/",model_save_path="test.model",n_neighbors=2))
