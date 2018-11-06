#дана арифметическая последовательность с потерянным элементом
#нужно вернуть потерянный элемент, найдём разницу по формуле энного элемента
#в условии дано что 1 и последний на месте, через них найдем шаг и пробежим по рэнжу
# def find_missing(sequence):
# 	d = ((sequence[-1]) - sequence[0])//(len(sequence)) # тут была заковырка, т.к. в формуле н-1
# 	print(sequence)
# 	print(d)
# 	for i in range(sequence[0]+d, sequence[-1], d):
# 		if i not in sequence: return i
# 	return sequence[0]
	

# print(find_missing([10,0]))

def find_missing(sequence):
    diff = (sequence[-1] - sequence[0]) / len(sequence)
    for i in range(0, len(sequence)):
        if sequence[0] + diff * i != sequence[i]:
            return sequence[0] + diff * i  
