"""
this is for test wite vars 
"""
import cv2
from pathlib import Path

TEST_TRAIN_DIR = str(Path().absolute()) + "/data/testTraining/"
TEST_FACE_IMAGE = str(Path().absolute()) + "/data/images/me.jpg"

READIMAGE = cv2.imread(TEST_FACE_IMAGE, cv2.IMREAD_COLOR)
