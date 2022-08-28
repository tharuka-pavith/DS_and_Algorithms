'''
Write a short Python function, is_even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
'''

def is_even(k : int):
    '''Returns True if k is even and vice versa'''
    return True if (divmod(k,2)[1] == 0) else False #ternary operator

if __name__ == '__main__':
    a,b = 5,8
    print(f'{a} is even = {is_even(a)}')
    print(f'{b} is even = {is_even(b)}')