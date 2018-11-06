def last_digit(n1, n2):
    if (n2 % 400):
        return ((n1 % 10)**(n2 % 400)) % 10
    else:
        return ((n1 % 10)**(n2 % 4)) % 10 if not(n1 % 10 == 0) else 0

if __name__ == '__main__':
    print(last_digit(10, 10**10))
  