import gradio
import sda

animator = sda.VideoAnimator()


def predict(image):
    return image


inputs = [
    gradio.Image(type="filepath"),
    gradio.Audio(source="microphone", type="filepath"),
]
outputs = ["video"]

GradioInterface = gradio.Interface(predict, inputs, outputs)
