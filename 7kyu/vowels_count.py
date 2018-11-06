def vowels_count(inputStr):
    return sum([1 for x in inputStr if x in 'aeiouAEIOU'])

if __name__ == '__main__':
    print(vowels_count('bEArAsdsdsd'))