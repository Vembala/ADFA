import inspect
import typing

import pytest

from ADFA.abstract import AnimatorAbstract

PARAMETERS = [(AnimatorAbstract, ["setup", "predict"])]


@pytest.mark.parametrize("abstract, names", PARAMETERS)
def test_setup_exist(abstract: typing.Type[AnimatorAbstract], names: str):
    assert sorted(names) == sorted(list(AnimatorAbstract.__abstractmethods__))
