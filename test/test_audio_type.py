import gradio
import pytest

from ADFA.gradio_interface import GradioInterface

ID = 1
TYPE = "filepath"


def test_audio_type_is_filepath(idx: int = ID, type_: str = TYPE):

    assert GradioInterface.input_components[idx].type == type_
