"""348597 => [7,9,5,8,4,3]."""


def digitize(n):
    return [int(x) for x in reversed(str(n))]

# def digitize(n):
#     return [int(x) for x in str(n)[::-1]]


if __name__ == '__main__':
    print(digitize(348597))
