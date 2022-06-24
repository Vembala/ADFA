import abc
import inspect

from ADFA.abstract import AnimatorAbstract

def test_abstract_animator(abstract: abc.ABC = AnimatorAbstract) -> None:
    assert inspect.isabstract(abstract)