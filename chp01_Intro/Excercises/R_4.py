'''
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
'''

def square_sum(n: int):
    if n<0: 
        raise ValueError('n should be positive')

    elif type(n) != int:
        raise TypeError('n should b an integer')
    
    else:
        return n*(n-1)*(2*n-1) // 6
        #return sum([i**2 for i in range(1,5)])

if __name__ == '__main__':
    print(f'{square_sum(5) = }')