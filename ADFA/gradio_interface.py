import gradio


def predict(image):
    return image


inputs = ["image", "microphone"]
outputs = ["video"]

GradioInterface = gradio.Interface(predict, inputs, outputs)
