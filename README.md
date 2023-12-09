# AIMS Captcha Beater
## Description
- The code in this repository can be used to autofill the IITH AIMS captchas (both pages)
- The first captcha is present in the html and can be extracted by simply inspecting the element
- The second captcha can be defeated by running a simple CNN that detects the characters.
- The code in this repository is used to both collect data and train the model, and autofill the captcha in live time using the ``selenium`` module in python to access the browser 
## To extract the data from the website to run the files in the following order:
- ``screenshot.py`` [takes screenshots of the captcha text]
- ``crop.py`` [crops the image to separate letters]
- ``threshold.py`` [applies a threshold to the colors and converts the image to bw]
- ``contour.py`` [detects the letters and makes the contours around them]
## To train the model and put it in action, run the following files:
-``solve.py`` [trains the network]
-``aims.py`` [uses selenium to open the browser and automatically log in to the portal]
