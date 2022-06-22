import os

import gdown
import gradio
import sda

URL = "https://drive.google.com/file/d/1f8bjoQgDgimmuUoNyoD5wOWj3NSK719w/view?usp=sharing"
MODEL_PATH = "ADFA/models/grid.dat"

def download(url=URL, destination=MODEL_PATH):
    gdown.download(url, destination)

def pass_(url=URL, destination=MODEL_PATH):
    pass

choices = {True: pass_, False: download}
model_exist = os.path.exists(MODEL_PATH)
download_function = choices[model_exist]

download_function(url=URL, destination=MODEL_PATH)

animator = sda.VideoAnimator(model_path=MODEL_PATH)


def predict(image):
    return image


inputs = [
    gradio.Image(type="filepath"),
    gradio.Audio(source="microphone", type="filepath"),
]
outputs = ["video"]

GradioInterface = gradio.Interface(predict, inputs, outputs)
