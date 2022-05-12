from keras.models import load_model
from matplotlib.pyplot import isinteractive
from helpers import resize_to_fit
from imutils import paths
import numpy as np
import cv2
import pickle
# from crop import crop 
from threshold import threshold
from contour import isolate

# def main():

CAPTCHA_IMAGE_FOLDER = r"D:\coding\python\captcha\testcases\del"
MODEL_FILENAME = "D:\coding\python\captcha\captcha_model.hdf5"
MODEL_LABELS_FILENAME = "D:\coding\python\captcha\model_labels.dat"

# Load up the model labels 
with open(MODEL_LABELS_FILENAME, "rb") as f:
    lb = pickle.load(f)

# Load the trained neural network
model = load_model(MODEL_FILENAME)


captcha_image_files = list(paths.list_images(CAPTCHA_IMAGE_FOLDER))
captcha_image_files = np.random.choice(captcha_image_files, size=(10,), replace=False)


def solvecaptcha(image_file):

    image = cv2.imread(image_file)

    # cropim= crop(image)
    threshim= threshold(image)
    letter_image_regions= isolate(threshim)
    if isinstance(letter_image_regions, int):
        print('Bad Captcha')
        return(0)

    # output = cv2.merge([image] * 3)
    predictions = []

    # loop over the letters
    for letter_bounding_box in letter_image_regions:


        letter_image = letter_bounding_box

        letter_image = resize_to_fit(letter_image, 20, 20)


        letter_image = np.expand_dims(letter_image, axis=2)
        letter_image = np.expand_dims(letter_image, axis=0)


        prediction = model.predict(letter_image)


        letter = lb.inverse_transform(prediction)[0]
        if 'LOWER' in letter:
            predictions.append(letter[-1].lower())
        else:
            predictions.append(letter[-1])

        # draw the prediction on the output image
        # cv2.rectangle(output, (x - 2, y - 2), (x + w + 4, y + h + 4), (0, 255, 0), 1)
        # cv2.putText(output, letter, (x - 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)

    # Print the captcha's text
    captcha_text = "".join(predictions)
    print("CAPTCHA text is: {}".format(captcha_text))
    return captcha_text
image_file=r'D:\coding\python\captcha\testcases\plswork\cap.png'

if __name__=='__main__':
    solvecaptcha()