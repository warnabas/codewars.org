def green(n):
    return len([x for x in range(n*100000) if (x == int(str(x**2)[-len(str(x)):]))])
    

if __name__ == '__main__':
    print(green(14))