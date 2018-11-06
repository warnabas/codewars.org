def flatten_and_sort(array):
    return sorted([x for y in array for x in y])


if __name__ == '__main__':
    print(flatten_and_sort())
