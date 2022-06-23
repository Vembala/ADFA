import os
import typing

from ADFA.gradio_interface import predict

IMAGE_PATH = "test/image.jpeg"
AUDIO_PATH = "test/example_audio.wav"
WRITE_PATH = "test/result.mp4"


def remove_(path: str) -> None:
    return None


choices = {True: os.remove, False: remove_}
remove = choices[os.path.exists(WRITE_PATH)]

_ = remove(WRITE_PATH)  # type: ignore


def test_predict(image_path: str = IMAGE_PATH, audio_path: str = AUDIO_PATH):
    ret_path = predict(image_path=image_path, audio_path=audio_path, path=WRITE_PATH)
    assert os.path.exists(WRITE_PATH)
