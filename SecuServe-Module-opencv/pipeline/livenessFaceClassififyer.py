"""
this class is for handling liveness of faces and then passes this data to the rest of the facial rec pipeline
"""

from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import AveragePooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator

import cv2
import face_recognition
from util import consoleLog
IMG_SIZE = 24



# trains the live model
def train(train_generator, val_generator):
	STEP_SIZE_TRAIN=train_generator.n//train_generator.batch_size
	STEP_SIZE_VALID=val_generator.n//val_generator.batch_size
	
	model = Sequential()

	model.add(Conv2D(filters=6, kernel_size=(3, 3), activation='relu', input_shape=(IMG_SIZE,IMG_SIZE,1)))
	model.add(AveragePooling2D())

	model.add(Conv2D(filters=16, kernel_size=(3, 3), activation='relu'))
	model.add(AveragePooling2D())

	model.add(Flatten())

	model.add(Dense(units=120, activation='relu'))

	model.add(Dense(units=84, activation='relu'))

	model.add(Dense(units=1, activation = 'sigmoid'))


	model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
  
  	consoleLog.Debug('Training Liveness Model CNN.....')
  
	model.fit_generator(generator=train_generator,
	                    steps_per_epoch=STEP_SIZE_TRAIN,
	                    validation_data=val_generator,
	                    validation_steps=STEP_SIZE_VALID,
	                    epochs=20
	)
  	return model


def process_and_encode(images):
    known_encodings = []
    known_names = []
    consoleLog.Debug("Encoding Liveness dataset ...")

    for image_path in tqdm(images):
        # Load image
        image = cv2.imread(image_path)
        # Convert it from BGR to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
     
        # detect face in the image and get its location (square boxes coordinates)
        boxes = face_recognition.face_locations(image, model='hog')

        # Encode the face into a 128-d embeddings vector
        encoding = face_recognition.face_encodings(image, boxes)

        # the person's name is the name of the folder where the image comes from
        name = image_path.split(os.path.sep)[-2]

        if len(encoding) > 0 : 
            known_encodings.append(encoding[0])
            known_names.append(name)

    return {"encodings": known_encodings, "names": known_names}


def isBlinking(history, maxFrames):
    """ @history: A string containing the history of eyes status 
         where a '1' means that the eyes were closed and '0' open.
        @maxFrames: The maximal number of successive frames where an eye is closed """
    for i in range(maxFrames):
        pattern = '1' + '0'*(i+1) + '1'
        if pattern in history:
            return True
    return False