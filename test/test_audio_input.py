import gradio
import pytest

from ADFA.gradio_interface import GradioInterface

ID = 1


def test_audio_interface_exist(idx: int = ID):

    """This function test if image interface instantiated

    This function test if the gradio app contains the image
    input.

    Args:
        id (int): The ID of the component.

    Returns
    """

    assert type(GradioInterface.input_components[idx]) == gradio.Audio
