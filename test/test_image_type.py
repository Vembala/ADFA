import gradio
import pytest

from ADFA.gradio_interface import GradioInterface

ID = 0
TYPE = "filepath"


def test_image_type_is_filepath(idx: int = ID, type_: str = TYPE):

    assert GradioInterface.input_components[idx].type == type_
