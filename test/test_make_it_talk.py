from inspect import issubclass
from pytest.mark import parametrize
from ADFA.makeittalk import MakeItTalk
from ADFA.abstract import AnimatorAbstract

PAIRS = [(MakeItTalk, AnimatorAbstract)]

@parametrize("child, parent", PAIRS)
def test_issubclass(child: Any, parent: Any):
    assert issubclass(child, parent)