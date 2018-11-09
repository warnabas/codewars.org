
"""Task.
You're given an integer n (0 <= n <= 10000).
You need to create a function which returns:

Fizz when n is divisible by 3
Buzz when n is divisible by 5
Fizz Buzz when n is divisible by both 3 and 5
Otherwise it should return the string representation of n
Restrictions
Your code mustn't contain:

if
== or !=
+ or -
str (including strip, lstrip, rstrip)
def
eval or exec
return
import
The check for restricted words is case-insensitive.
"""


#def fizz_buzz(n):
#     fizz_buzz = not n % 3 and not n % 5 and "Fizz Buzz"
#     fizz_buzz = not n % 3 and "Fizz"
#     fizz_buzz = not n % 5 and "Buzz"
fizz_buzz = (lambda x: not (x % 3) and not (x % 5) and "Fizz Buzz")
buzz = (lambda x: not (x % 5) and "Buzz")
fizz = (lambda x: not (x % 3) and "Fizz")



            #and '{}'.format(3)
if __name__ == '__main__':
    n = 17
    print(fizz_buzz(n) or fizz(n) or buzz(n) or "{}".format(n))
