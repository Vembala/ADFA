from typing import Any

import pytest

from ADFA.abstract import AnimatorAbstract
from ADFA.makeittalk import MakeItTalk

PAIRS = [(MakeItTalk, AnimatorAbstract)]


@pytest.mark.parametrize("child, parent", PAIRS)
def test_issubclass(child: Any, parent: Any):
    assert issubclass(child, parent)
