'''
Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
'''
from random import seed, random
from time import time_ns
def minmax(seq: list|tuple|set):
    '''Returns smallest and largest numbers in seq'''
    min = max = seq[0]
    for i in seq:
        if i > max: max = i
        if i < min: min = i

    return (min,max)

if __name__ == '__main__':
    s = seed(time_ns()) #seed
    
    ls = [int(random()*1000)%50 for i in range(20)]
    print(ls)
    min, max = minmax(ls)
    print(f'min = {min} max = {max}')
