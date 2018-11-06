# def sum_of_digs(number):
#     return sum([int(x) for x in str(number)])

def  list_to_int(list):
    return int(''.join([str(x) for x in list]))


def is_number_sorted(number):
    return str(number) == ''.join(sorted(str(number)))

def find_all(sum_dig, number_of_digs):

    result = []

    list_of_search = [1 for x in 'x' * number_of_digs]

    end_of_search = [9 for x in '9' * number_of_digs]

    while list_of_search != end_of_search:
        # loop for all digits
        


        for номер_цифры_в_числе in range(количество_цифр, 0, -1):
            # loop for every digit
            for i in range(посчитать_цифру, которая должна быть тут, 9+1):
                list_of_search[номер_цифры_в_числе] = i
                if sum(list_of_search) == sum_dig:
                    result.append(list_to_int(list_of_search))
                    continue
                