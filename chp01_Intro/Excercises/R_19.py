'''
Demonstrate how to use Python’s list comprehension syntax to produce
the list [ a , b , c , ..., z ], but without having to type all 26 such
characters literally
'''

def generate_alphabet()->list:
    l = [chr(i) for i in range(ord('a'), ord('z')+1)]
    return l

if __name__ == '__main__':
    print(f'Alphabet = {generate_alphabet()}')

