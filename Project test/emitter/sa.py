import random
import cv2
import base64
import json

from iottalkpy.dan import NoData

api_url = 'http://140.116.58.163:31480/csm'

device_name = 'emitter_image'
device_model = 'ScratchX'

idf_list = ['ScratchX-I']
push_interval = 1  # global interval
interval = {
    'Scratch_X': 3,
}


def on_register(dan):
    print('register successfully')


def ScratchX_I():
    image = cv2.imread("test.png")
    # Convert the image to a byte string
    _, img_bytes = cv2.imencode('.png', image)
    # Encode the image as base64
    png_as_text = base64.b64encode(img_bytes)
    print("successful")
    # Create a JSON object with the base64-encoded image data
    json_data = json.dumps({"data": str(png_as_text, 'utf-8')})

    return json_data


def DummyControl_O(data: list):
    print(str(data[0]))
