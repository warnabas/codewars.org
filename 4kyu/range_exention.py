def len_of_nexts(args):
    result = []
    for i in range(1, len(args)-1):
        if (args[i - 1] + 1 == args[i]):
            result.append(args[i - 1])
            i = i+1
            while args[i]:
                if i < len(args) and (args[i] + 1 == args[i + 1]):
                    i += 1
                    continue
                else:
                    result.append(args[i])
                    break
                i += 1
        else

                
    print(result)

def solution(args):
    result = ""
    []
    return

if __name__ == '__main__':
    len_of_nexts([1, 2, 3, 4, 5, 8, 10, 11])
