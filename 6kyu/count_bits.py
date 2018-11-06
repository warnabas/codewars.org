
"""
Write a function that takes an integer as input, and returns the number
of bits that are equal to one in the binary representation of that number.
You can guarantee that input is non-negative.

Example: The binary representation
of 1234 is 10011010010,
the function should return 5 in this case
"""


def countBits(n):
    return sum(map(int, list((bin(n)[2:]))))
    # return bin(n).count('1') //faster and cleaner then mine
    # return '{:b}'.format(n).count('1')

if __name__ == '__main__':
    print(countBits(12343192839182931923890128390812903819192389128391823780172830718027109237881209381209189237812738128378**10000))
