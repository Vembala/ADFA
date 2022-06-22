from ADFA.gradio_interface import animator
from sda import VideoAnimator

def test_animator_exist():
    assert type(animator) == VideoAnimator