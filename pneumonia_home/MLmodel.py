import numpy as np
import tensorflow as tf
from matplotlib import image
from PIL import Image


# inp = image.imread('person1946_bacteria_4874.jpeg')
def model_call(data):
    # pimg = Image.open(data)
    dic = {0 : 'Positive', 1:'Negative'}
    pimg = data
    # print(len(pimg))
    inp1 = pimg.resize((150,150))
    inparr = np.array(inp1)

    inparr.resize((1,150,150,1), refcheck=False)
    inparr.shape

    # Load TFLite model and allocate tensors.
    interpreter = tf.lite.Interpreter(model_path="./trained_model.tflite")
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    # Test model on random input data.
    input_shape = input_details[0]['shape']
    input_data = np.array(inparr, dtype=np.float32)
    interpreter.set_tensor(input_details[0]['index'], input_data)

    interpreter.invoke()
    # The function `get_tensor()` returns a copy of the tensor data.
    # Use `tensor()` in order to get a pointer to the tensor.
    output_data = interpreter.get_tensor(output_details[0]['index'])



    return dic[int(output_data[0][0])]


