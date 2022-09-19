from random import randint
from math import pow


class countNumbers():
    def __init__(self) -> None:
        self.count: list[int] = [0, 0, 0, 0, 0, 0]

    def add(self, number) -> None:
        self.count[number - 1] += 1
        return

    def generate_random(self, start: int, end: int) -> None:
        number: int = randint(start, end)
        self.add(number)
        return


def simulate(*values: tuple[int], rep: int) -> list[int] or None:
    list(values).sort()
    my_count: object = countNumbers()
    while (rep >= 1):
        my_count.generate_random(values[0], values[-1])
        rep -= 1
    return my_count.count


def multiple_simulate(n=6, index=0):
    if (n > 0):
        reps = pow(10, index)
        print(simulate(1, 2, 3, 4, 5, 6, rep=reps))
        multiple_simulate(n - 1, index + 1)


multiple_simulate()
