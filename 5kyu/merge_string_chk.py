"""Оказывается надо ответить на вопрос, можно ли слепить s из part1,part2."""d
ef is_merge(s, part1, part2):
    chkstr = ''
    for i in range(max(len(part1), len(part2))):
        if i < len(part1):
            chkstr = chkstr.__add__(part1[i])
        if i < len(part2):
            chkstr = chkstr.__add__(part2[i])
    print(chkstr, s)
    b = [1 for x in chkstr if x in s]
    return sum(b) == len(s)


if __name__ == '__main__':
    print(is_merge('codewars', 'cdw', 'oears'))
    print(is_merge('codewars', 'code', 'wars'))
    print(not is_merge('codewars', 'cod', 'wars'))
