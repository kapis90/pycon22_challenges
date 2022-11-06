import random
from enum import Enum, auto
from pprint import pp

random.seed(0xDEADBEEF)


class Power(Enum):
    SPEED_BOOTS = auto()
    STRONG_WILL = auto()
    MONEY_MAKER = auto()
    SUPER_STRENGTH = auto()


class WeaklingDuck:
    power = 6

    def __repr__(self):
        if isinstance(self.power, Power):
            return f"{self.__class__.__name__} with {self.power.name}"
        return f"{self.__class__.__name__}"


class Duck(WeaklingDuck):
    power = 5

    def __init__(self, name):
        self.name = name


class SuperDuck(Duck):
    def __init__(self, name, power):
        super().__init__(name)
        if isinstance(power, Power):
            self.power = power
        else:
            self.power = random.choice(list(Power))


def get_power(obj):
    if isinstance(obj.power, Power):
        return obj.power.value
    return obj.power


def main():
    d1 = WeaklingDuck()
    d2 = Duck("Huey")
    d3 = SuperDuck("Scrooge McDuck", Power.MONEY_MAKER)
    d4 = SuperDuck("Launchpad McQuack", Power.SPEED_BOOTS)
    ducks_in_a_row = [d2, d4, d3, d1]
    ducks_in_a_row.sort(key=get_power)
    pp(ducks_in_a_row)

    # add some code here (and/or edit that above this line)


if __name__ == '__main__':
    main()
