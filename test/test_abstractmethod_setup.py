import inspect
import typing
import pytest
from ADFA.abstract import AnimatorAbstract

PARAMETERS = [(AnimatorAbstract, ['setup'])]

@pytest.fixtures.parameterize("abstract, name", PARAMETERS)
def test_setup_exist(abstract: typing.Type[AnimatorAbstract], name: str):
    assert sorted(NAMES) == sorted(list(AnimatorAbstract.__abstractmethods__))