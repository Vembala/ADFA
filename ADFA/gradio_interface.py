import gradio
import sda

MODEL_PATH = "ADFA/models/grid.dat"

animator = sda.VideoAnimator(model_path=MODEL_PATH)


def predict(image):
    return image


inputs = [
    gradio.Image(type="filepath"),
    gradio.Audio(source="microphone", type="filepath"),
]
outputs = ["video"]

GradioInterface = gradio.Interface(predict, inputs, outputs)
