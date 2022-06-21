import gradio


def predict(image):
    return image


inputs = ["image"]
outputs = ["video"]

GradioInterface = gradio.Interface(predict, inputs, outputs)
