import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
from keras.preprocessing import image
from tensorflow.keras.utils import load_img, img_to_array
import os



def model_call(data):
    img = data
    # img = os.path.join('.', img)
    # img = load_img(img, target_size=(331, 331))
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img/255
    # inp = Image.open('normal.jpeg')
    inp = img
    # print(inp.size)
    # print(inp.mode)
    # inp1 = inp.resize((331,331))
    inp1 = inp
    # inparr = np.array(inp1)
    inparr = inp1
    # print(inparr.shape, 'inparr.shape')


    inparr.resize((1,331,331,3), refcheck=False)
    # print(inparr.shape, 'inparr.shape resized')

    #  load the tflite model and allocate tensors.
    interpreter = tf.lite.Interpreter(model_path="covid_model.tflite")
    interpreter.allocate_tensors()

    # Get input and output tensors.
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Test the model on random input data.
    input_shape = input_details[0]['shape']
    # print(input_shape, 'input_details')
    # input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
    input_data = np.array(inparr, dtype=np.float32)
    interpreter.set_tensor(input_details[0]['index'], input_data)

    interpreter.invoke()

    # The function `get_tensor()` returns a copy of the tensor data.
    # Use `tensor()` in order to get a pointer to the tensor.
    # print(output_details)
    output_data = interpreter.get_tensor(output_details[0]['index'])
    # print(interpreter.get_tensor(23))
    # print(output_data)
    return output_data[0][0]

# model_call('person1_virus_9.jpeg')