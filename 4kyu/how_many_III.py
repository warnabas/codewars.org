def is_sorted(number):
    return str(number) == ''.join(sorted(str(number)))
def cond(number, summa):
    chk = [int(x) for x in str(number)]
    if chk == sorted(chk) and (sum(chk) == summa):
        return number

def find_all(sum_dig, number_of_digs):
    '''number_of_digs = 2 - 15
       sum_dig = 20 - 65 '''
    # if sum_dig == digs:
    #     return [1, int('1'*digs), int('1'*digs)]
    # if sum_dig == digs+1:
    #     return [1, int('1'*digs)+1, int('1'*digs)+1]
    # if digs > 6 and  
    if sum_dig == 9 * number_of_digs:
        return [1, int('9' * number_of_digs), int('9' * number_of_digs)]
    if sum_dig > number_of_digs*9:
        return []
    b = [x for x in range((int('1'*number_of_digs)), int('9'*number_of_digs)+1) if cond(x, sum_dig)]
    print(b)
    return [len(b), min(b), max(b)] if b else []


if __name__ == '__main__':
    print(find_all(11, 3))