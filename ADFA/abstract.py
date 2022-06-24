import abc
import typing

AnimatorAbstract: typing.Any = None

class AnimatorAbstract(abc.ABC):

    def __init__(self):

        pass

    @abc.abstractmethod
    def dummy_method():
        pass
    