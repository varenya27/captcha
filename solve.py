from keras.models import load_model
from matplotlib.pyplot import isinteractive
from helpers import resize_to_fit
from imutils import paths
import numpy as np
import imutils
import cv2
import pickle
from crop import crop #takes image path as input and crops it
from threshold import threshold #takes image path and thresholds it
from contour import isolate #splits the captcha based on boundaries and stores in bin
from screenshot import takess #takes ss and stores in testcases/more_raw/
# def main():

CAPTCHA_IMAGE_FOLDER = r"D:\coding\python\captcha\testcases\del"
MODEL_FILENAME = "D:\coding\python\captcha\captcha_model.hdf5"
MODEL_LABELS_FILENAME = "D:\coding\python\captcha\model_labels.dat"

# Load up the model labels (so we can translate model predictions to actual letters)
with open(MODEL_LABELS_FILENAME, "rb") as f:
    lb = pickle.load(f)

# Load the trained neural network
model = load_model(MODEL_FILENAME)

# Grab some random CAPTCHA images to test against.
# In the real world, you'd replace this section with code to grab a real
# CAPTCHA image from a live website.
captcha_image_files = list(paths.list_images(CAPTCHA_IMAGE_FOLDER))
captcha_image_files = np.random.choice(captcha_image_files, size=(10,), replace=False)

# loop over the image paths
# for image_file in captcha_image_files:
image_file=r'D:\coding\python\captcha\testcases\plswork\cap.png'
def solve(image_file):
    # image_file= r'D:\coding\python\captcha\testcases\raw\yC2ws.png'
    # Load the image and convert it to grayscale
    image = cv2.imread(image_file)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cropim= crop(image)
    threshim= threshold(cropim)
    letter_image_regions= isolate(threshim)
    if isinstance(letter_image_regions, int):
        print('Bad Captcha')
        return(0)
    # Now we can loop through each of the four contours and extract the letter
    # inside of each one
        # Get the rectangle that contains the contour
    
    # Sort the detected letter images based on the x coordinate to make sure
    # we are processing them from left-to-right so we match the right image
    # with the right letter

    # Create an output image and a list to hold our predicted letters
    output = cv2.merge([image] * 3)
    predictions = []

    # loop over the lektters
    for letter_bounding_box in letter_image_regions:
        # Grab the coordinates of the letter in the image
        # x, y, w, h = letter_bounding_box

        # Extract the letter from the original image with a 2-pixel margin around the edge
        letter_image = letter_bounding_box
        # Re-size the letter image to 20x20 pixels to match training data
        letter_image = resize_to_fit(letter_image, 20, 20)

        # Turn the single image into a 4d list of images to make Keras happy
        letter_image = np.expand_dims(letter_image, axis=2)
        letter_image = np.expand_dims(letter_image, axis=0)

        # Ask the neural network to make a prediction
        prediction = model.predict(letter_image)

        # Convert the one-hot-encoded prediction back to a normal letter
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
    # Show the annotated image
    # cv2.imshow("Output", output)
    # cv2.waitKey()

# if __name__=='__main__':
#     main()