import tensorflowjs as tfjs
from keras.models import load_model

MODEL_FILENAME = "D:\coding\python\captcha\captcha_model.hdf5"

model = load_model(MODEL_FILENAME)

tfjs.converters.save_keras_model(model, 'D:\coding\python\captcha')