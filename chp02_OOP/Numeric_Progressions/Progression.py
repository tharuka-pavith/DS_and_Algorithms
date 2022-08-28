class Progression:
    '''Iterator producing generic progression
    
    Default iterator produces whole numbers, 0,1,2,3,...'''

    def __init__(self, start: int = 0):

        self._current = start

    def _advance(self):
        self._current += 1

    
    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            val = self._current
            self._advance()
            return val

    def __iter__(self):
        return self
    

if __name__ == '__main__':
    pr = Progression()
    it = iter(pr)

    print(next(it))