from abc import ABC, abstractmethod

class IQuackBehaviour(ABC):
    @abstractmethod
    def quack(self):
        pass

class SimpleQuack(IQuackBehaviour):
    def quack(self):
        return "Simple quack"

class NoQuack(IQuackBehaviour):
    def quack(self):
        return "No quack"

class IFlyBehaviour(ABC):
    @abstractmethod
    def fly(self):
        pass

class SimpleFly(IFlyBehaviour):
    def fly(self):
        return "Simple fly"

class NoFly(IFlyBehaviour):
    def fly(self):
        return "No fly"

class Duck:
    def __init__(self, fly_behaviour: IFlyBehaviour, quack_behaviour: IQuackBehaviour) -> None:
        self.fly_behaviour:IFlyBehaviour  = fly_behaviour
        self.quack_behaviour:IQuackBehaviour = quack_behaviour

    def fly(self):
        return self.fly_behaviour.fly()

    def quack(self):
        return self.quack_behaviour.quack()

def main():
    city_duck = Duck(NoFly(), SimpleQuack())
    wild_duck = Duck(SimpleFly(), SimpleQuack())
    ducks = [city_duck, wild_duck]

    for duck in ducks:
        print(duck.fly())
        print(duck.quack())

if __name__ == "__main__":
    main()

 
