import itertools

def fib_gen():
    """generates Fibonacci number"""
    current, nxt = 0, 1

    while True:
        yield current
        current, nxt = nxt, current + nxt
        


def fib(n):
    if n < 2:
        return n
    return (next(itertools.islice(fib_gen(), n, None)))
    

def fib_loop(n):
    if n < 2:
        return n
    current, nxt = 0, 1
    for i in range(n):
        current, nxt = nxt, current + nxt
    return current    

if __name__ == '__main__':
        print(fib_loop(110000))
