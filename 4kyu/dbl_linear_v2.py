
"""For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
There are no other numbers in u.
Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]
1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13,
then 7 gives 15 and 22 and so on...
"""

def test_linear(n):
    print('y: ')
    for i in range(n):
        print((i*2+1), end=' ')
    print('\nz: ')
    for i in range(n):
        if not((3*i + 1) % 2):
            print(((3*i + 1)), end=' ')

def dbl_linear(n):
    y = {i*2+1 for i in range(n*2)}
    z = {i*3+1 for i in range(n*2) if not((i*3+1) % 2)}
    print(y, z, len(y), len(z), sep='\n')
    b = {*y, *z}
    b = list(b)

    print(b)

if __name__ == '__main__':
    dbl_linear(20)
