from sda import VideoAnimator

from ADFA.gradio_interface import animator


def test_animator_exist():
    assert type(animator) == VideoAnimator
