"""
Consider a sequence u where u is defined as follows:

The number u(0) = 1 is the first one in u.
For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
There are no other numbers in u.
Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]
1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13,
then 7 gives 15 and 22 and so on...

#Task: Given parameter n the function dbl_linear (or dblLinear...)
#returns the element u(n) of the ordered (with <) sequence u.
#Example: dbl_linear(10) should return 22
#Note: Focus attention on efficiency.
"""

def dbl_linear(n):
    # TODO write the same code through lambdas and list comprehensions
    u = [1]
    for i in range(int(n*4.2)):
        y = (2 * u[i]) + 1
        u.append(y)
        z = (3 * u[i]) + 1
        u.append(z)
    return sorted(list(set(u)))[n]


if __name__ == '__main__':
    print(dbl_linear(10))

"""
dendisol(4 kyu)1 year ago
Missing item with a value of 159


IsHsNiKa2(4 kyu)6 months edit
Dendisol answered corectly,
according to my opinion Yflash doesnt have correct algoritm,
159 is missing and the reason probably is why calculating
of the next iteration is not included, so if you pay more
attention, you will find that 2*79+1=159....I dont know weather
i am clear enough.
"""

"""
    u = [1]
    for index in range(0, n):
        x = u[index]
        y = (2 * x) + 1
        u.append(y)
        z = (3 * x) + 1
        u.append(z)
    u.sort()
    return sorted(list(set(u)))[n]

"""