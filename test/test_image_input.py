"""The test case for image input

This module contain tests for the image interface.

Example:
    $ python -m pytest test_image_input.py

Attributes:
"""

import gradio
import pytest

from ADFA.gradio_interface import GradioInterface

ID = 0


def test_image_interface_exist(idx: int = ID):

    """This function test if image interface instantiated

    This function test if the gradio app contains the image
    input.

    Args:
        id (int): The ID of the component.

    Returns
    """

    assert type(GradioInterface.input_components[idx]) == gradio.Image
