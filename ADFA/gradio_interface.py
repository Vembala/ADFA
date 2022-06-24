import os

import gradio

def predict(
    image_path: str, audio_path: str,
) -> str:
    
    return None


inputs = [
    gradio.Image(type="filepath"),
    gradio.Audio(source="microphone", type="filepath"),
]
outputs = ["video"]

GradioInterface = gradio.Interface(predict, inputs, outputs)
