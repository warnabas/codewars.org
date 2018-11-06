"""" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
"""


def generate_hashtag(s):
    if (not s) or (len(s) > 140):
        return False
    else:
        return '#'+''.join([x.capitalize() for x in s.split()])


if __name__ == '__main__':
    print(generate_hashtag("Hello there thanks for trying"))