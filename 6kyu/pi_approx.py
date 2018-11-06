from math import pi

def iter_pi(epsilon):
    # pi = 4 - 4/3 + 4/5 - 4/7 ...
    i = 1
    calc_pi = 4.0
    sign = -4.0
    while(abs(pi - calc_pi) > epsilon):
        calc_pi += sign/(2 * i + 1)
        i, sign = i + 1, -sign
    return [i, round(calc_pi, 10)]

if __name__ == '__main__':
    print(iter_pi(.1))