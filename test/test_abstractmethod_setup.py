import inspect
import typing
from ADFA.abstract import AnimatorAbstract

def test_setup_exist(abstract: typing.Type[AnimatorAbstract]):
    assert inspect.isabstract(AnimatorAbstract.setup)