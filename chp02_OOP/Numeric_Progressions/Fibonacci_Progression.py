from Progression import Progression

class FibonnacciProgression (Progression):
    def __init__(self, start: int = 0):
        super().__init__(start)
        self._prev = 1
        self._prevprev = 1
    
    def _advance(self):
        temp = self._current
        self._current = self._current + self._prev
        self._prev += temp

if __name__ == '__main__':
    fp = FibonnacciProgression()

    it = iter(fp)

    for i in range(10):
        print(next(it))