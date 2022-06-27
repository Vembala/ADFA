import inspect
import typing
import pytest

import ADFA

PAIRS = [(ADFA.abstract.AnimatorAbstract.setup, ['argdict']),]

@pytest.mark.parametrize("function, arguments", )
def test_arguments(function: typing.Function, arguments: typing.List):
    assert sorted(arguments) == sorted(list(inspect.signature(function).parameters))