from abc import ABC, abstractmethod
from observable import IObservable

class IObserver(ABC):

    @abstractmethod
    def update(self):
        pass

class PhoneDisplay(IObserver):

    def __init__(self, observable: IObservable):
        self.observable: IObservable = observable

    def update(self):
        print(self.observable.get_temperature())
        return