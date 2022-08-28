from Progression import Progression

class GeometricProgression (Progression):
    def __init__(self,start: int = 1, base: int = 2):
        super().__init__(start)
        self._base = base

    def _advance(self):
        self._current = self._current * self._base

if __name__ == '__main__':
    gp = GeometricProgression()

    it = iter(gp)

    for i in range(10):
        print(next(it))
