import inspect
import typing
import pytest

import ADFA

PAIRS = [(ADFA.abstract.AnimatorAbstract.setup, ["self", 'argdict']),]

@pytest.mark.parametrize("function, arguments", PAIRS)
def test_arguments(function: typing.Callable, arguments: typing.List):
    assert sorted(arguments) == sorted(list(inspect.signature(function).parameters))