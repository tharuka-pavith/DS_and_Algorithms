from Progression import Progression

class ArithmeticProgression(Progression):
    def __init__(self, start: int = 0, step: int = 1):
        super().__init__(start)
        self._step = step

    def _advance(self):
        self._current += self._step
    


if __name__ ==  '__main__':
    ap = ArithmeticProgression(step = 3)

    it = iter(ap)
    for i in range(10):
        print(next(it))