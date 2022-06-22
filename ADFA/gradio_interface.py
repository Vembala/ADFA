import gradio


def predict(image):
    return image


inputs = [gradio.Image(type="filepath"), gradio.Audio(source="microphone")]
outputs = ["video"]

GradioInterface = gradio.Interface(predict, inputs, outputs)
