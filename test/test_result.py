import os
from ADFA.gradio_interface import predict

IMAGE_PATH = "test/image.jpeg"
AUDIO_PATH = "test/example_audio.wav"
WRITE_PATH = "test/result.mp4"

os.remove(WRITE_PATH)

def test_predict(image_path: str, audio_path: str):
    ret_path = predict(image_path=image_path, audio_path=audio_path)
    assert os.path.exists(result.mp4)