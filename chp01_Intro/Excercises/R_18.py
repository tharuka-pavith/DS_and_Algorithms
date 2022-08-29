'''
Demonstrate how to use Python’s list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

References:
https://stackoverflow.com/questions/25077095/what-is-a-clearer-way-to-generate-this-sequence-of-numbers
'''

if __name__ == '__main__':
    l = [i*(i+1) for i in range(10)] #Pronic numbers

    print(l) 