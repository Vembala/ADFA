import inspect
import typing
import pytest
from ADFA.abstract import AnimatorAbstract

PARAMETERS = [(AnimatorAbstract, ['setup'])]

@pytest.mark.parameterize("abstract, name", PARAMETERS)
def test_setup_exist(abstract: typing.Type[AnimatorAbstract], names: str):
    assert sorted(names) == sorted(list(AnimatorAbstract.__abstractmethods__))