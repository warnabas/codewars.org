string_lc = 'abcdefghijklmnopqrstuvwxyzabcdefghij'


def move_ten(string):
    return ''.join([string_lc[string_lc.find(char)+10] for char in string])


if __name__ == '__main__':
    print(move_ten("testcase"))  # docdmkco
