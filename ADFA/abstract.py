import abc


class AnimatorAbstract(abc.ABC):
    def __init__(self):

        self.setup = None

    @abc.abstractmethod
    def dummy_method(
        self,
    ):
        pass
