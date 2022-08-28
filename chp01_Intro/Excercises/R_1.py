'''
Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.
'''

def is_multiple(n:int,m: int):
    return  True if (n%m == 0) else False

if __name__ == '__main__':
    n,m = 21, 7
    print(f'{n} is multiple of {m} = {is_multiple(n,m)}')
