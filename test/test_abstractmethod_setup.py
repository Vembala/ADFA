import inspect
import typing
from ADFA.abstracts import AnimatorAbstract

def test_setup_exist(abstract: typing.TYPE[AnimatorAbstract]):
    assert inspect.isabstract(AnimatorAbstract.setup)