import * as tf from '@tensorflow/tfjs'

const model = await tf.loadLayersModel('D:\coding\python\captcha\model.json')

const example = tf.fromPixels('D:\coding\python\captcha\testcases\bin\symbol-Upper-y\id-3mvYL613.png')

const prediction = model.predict(example);

print(prediction)