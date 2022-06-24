import abc
import inspect
import typing

from ADFA.abstract import AnimatorAbstract


def test_abstract_animator(abstract: typing.Type(AnimatorAbstract) = AnimatorAbstract) -> None:
    assert inspect.isabstract(abstract)
