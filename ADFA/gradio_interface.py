import gradio


def predict(image):
    return image


inputs = ["image", gradio.Audio(source="microphone")]
outputs = ["video"]

GradioInterface = gradio.Interface(predict, inputs, outputs)
