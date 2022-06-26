import pytest
from typing import Any
from ADFA.makeittalk import MakeItTalk
from ADFA.abstract import AnimatorAbstract

PAIRS = [(MakeItTalk, AnimatorAbstract)]

@pytest.mark.parametrize("child, parent", PAIRS)
def test_issubclass(child: Any, parent: Any):
    assert issubclass(child, parent)