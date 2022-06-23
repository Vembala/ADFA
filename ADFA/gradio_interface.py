import os

import gdown
import gradio
import sda

URL = "https://drive.google.com/uc?id=1f8bjoQgDgimmuUoNyoD5wOWj3NSK719w"
MODEL_PATH = "ADFA/models/grid.dat"
OUTPUT_PATH = "result.mp4"


def download(url=URL, destination=MODEL_PATH):
    gdown.download(url, destination)


def pass_(url=URL, destination=MODEL_PATH):
    pass


choices = {True: pass_, False: download}
model_exist = os.path.exists(MODEL_PATH)
download_function = choices[model_exist]

download_function(url=URL, destination=MODEL_PATH)

animator = sda.VideoAnimator(model_path=MODEL_PATH)


def predict(image_path: str, audio_path: str, animator = animator, path: str = OUTPUT_PATH):
    vid, aud = animator(image_path, audio_path)
    animator.save_video(vid, aud, OUTPUT_PATH)

inputs = [
    gradio.Image(type="filepath"),
    gradio.Audio(source="microphone", type="filepath"),
]
outputs = ["video"]

GradioInterface = gradio.Interface(predict, inputs, outputs)
