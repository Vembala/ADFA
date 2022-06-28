import inspect
import typing

import pytest

from ADFA.abstract import AnimatorAbstract
from ADFA.makeittalk import MakeItTalk

PARAMETERS = [
    (AnimatorAbstract, ["setup", "predict"]),
]


@pytest.mark.parametrize("aclass, names", PARAMETERS)
def test_setup_exist(aclass: typing.Type[AnimatorAbstract], names: str):
    assert sorted(names) == sorted(list(aclass.__abstractmethods__))
