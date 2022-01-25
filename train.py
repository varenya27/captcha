import cv2
import pickle
import os.path
import numpy as np
from imutils import paths
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.core import Flatten, Dense
from helpers import resize_to_fit


# folder = ''.join([os.getcwd(),r"\tescases\bin"])
folder=r'D:\coding\python\captcha\testcases\bin'
# print(folder)
MODEL_FILENAME = "D:\coding\python\captcha\captcha_model.hdf5"
MODEL_LABELS_FILENAME = "D:\coding\python\captcha\model_labels.dat"


# initialize the data and labels
data = []
labels = []
# loop over the input images
os.chdir(folder)
for imgfolder in os.listdir(folder):
    # print('******')
    # print(imgfolder)
    # print('******')
    flag=1
    for imgpath in (os.listdir(''.join([os.getcwd(),r'\s',imgfolder[1:]]))):
        image = cv2.imread(''.join([os.getcwd(),r'\s',imgfolder[1:],r'\i',imgpath[1:]]))
        try:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        except:
            print('ded')
            quit()
        # Resize the letter so it fits in a 20x20 pixel box
        image = resize_to_fit(image, 20, 20)

        # Add a third channel dimension to the image to make Keras happy
        image = np.expand_dims(image, axis=2)

        # Grab the name of the letter based on the folder it was in
        p=imgfolder.split(os.path.sep)
        if p[7:12]=='Lower':
            label = p[-1]
        else:
            label = p[-1].upper()

        data.append(image)
        labels.append(label)
    os.chdir(folder)


data = np.array(data, dtype="float") / 255.0
labels = np.array(labels)

(X_train, X_test, Y_train, Y_test) = train_test_split(data, labels, test_size=0.25, random_state=0)

lb = LabelBinarizer().fit(Y_train)
Y_train = lb.transform(Y_train)
Y_test = lb.transform(Y_test)

with open(MODEL_LABELS_FILENAME, "wb") as f:
    pickle.dump(lb, f)

# Build the neural network!
model = Sequential()

model.add(Conv2D(20, (5, 5), padding="same", input_shape=(20, 20, 1), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

model.add(Conv2D(50, (5, 5), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

model.add(Flatten())
model.add(Dense(500, activation="relu"))

model.add(Dense(51, activation="sigmoid"))

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(X_train, Y_train, validation_data=(X_test, Y_test), batch_size=32, epochs=4, verbose=1)

model.save(MODEL_FILENAME)
