import abc


class AnimatorAbstract(abc.ABC):
    def __init__(self):

        self.setup = None

    @abc.abstractmethod
    def setup(
        self, argdict
    ):
        pass

    @abc.abstractmethod
    def predict(
        self,
    ):
        pass
