"""In this kata, you must create a digital root function.

A digital root is the recursive sum of all the digits in a number.
Given n, take the sum of the digits of n. If that value has two digits,
continue reducing in this way until a single-digit number is produced.
This is only applicable to the natural numbers.

Here's how it works:

digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6

digital_root(132189)
=> 1 + 3 + 2 + 1 + 8 + 9
=> 24 ...
=> 2 + 4
=> 6

digital_root(493193)
=> 4 + 9 + 3 + 1 + 9 + 3
=> 29 ...
=> 2 + 9
=> 11 ...
=> 1 + 1
=> 2
"""


def making_diglist(digit):
    return [int(x) for x in str(digit)]


def digital_root(digit):
    dig_list = making_diglist(digit)  # making list of digits from a number
    while len(dig_list) > 1:
        # making list of sum(digits) until there is only one
        dig_list = making_diglist(sum(dig_list))
    return dig_list[0]


if __name__ == '__main__':
    print(digital_root(100000))


"""1 year ago
any number x can be wroten as x = 9a + b (b=x%9)

other side x can be wroten as 10-based x = 10k + n = 9k + k + n = 9k + (k+n)
it means k+n == b
three digit number can be wroten as
x = 100m+10k+n = 99m + m + 9k + k + n = 9(11m+k) + (m+k+n) it means m+k+n == b
and so on
this guys are genius.

If n % 9 != 0 return n % 9. Otherwise return n (if n == 0) or 9 (if n != 0).

def digital_root(n):
  return n%9 or n and 9

Here's a non truthy/falsy version that shows the
"magic" is mainly in the modulo operator.

def digital_root(n):
  remainder = n % 9
  return remainder if remainder != 0 or n == 0 else 9
In my opinion the truth/falsy shorthand and even more so the fact that
"x and y" in python returns y if x!=0, while admitedly quite clever, is
only applicable to codegolf and not good for use in software products.
Martin Fowler says it best:
https://www.goodreads.com/quotes/6341736-any-fool-can-write-code-that-a-computer-can-understand

Why modulo has this property seems to be an aspect of 9 magic.
Note that all multiples of 9 hit the last "else 9" case: 18, 27, 36, etc
http://www.quickanddirtytips.com/education/math/the-magic-of-number-9-part-1

"""