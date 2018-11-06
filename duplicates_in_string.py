# Count the number of Duplicates

# Write a function that will return the count of 
#distinct case-insensitive alphabetic characters 
#and numeric digits that occur more than once in
#the input string. The input string can be assumed
 #to contain only alphabets (both uppercase and 
#lowercase) and numeric digits.
# Example

# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (bandB)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice

# a = [{'a': 123}, {'b': 123}, {'a': 123}]
# b = []
# for i in range(0, len(a)):
#     if a[i] not in a[i+1:]:
#         b.append(a[i])


def duplicate_count(text):
    text = text.lower()  # => 'aAbBcC' = 'aabbcc'
    res = 0
    chars = list(text)  # => ['a','a','b','b','c','c']
    b = dict.fromkeys(chars, 0)  # => {'a': 0,'b': 0,'c': 0}
    for i in range(len(chars)):
        if chars[i] in chars[i+1:]:
            b[chars[i]] += 1
    for i in b:
        if (b[i] > 0):
            res += 1
    return res


print(duplicate_count('aAbBcCccceqq'))

# def duplicate_count(text):
#     count = 0
#     for c in set(text.lower()):
#         if text.lower().count(c) > 1:
#             count += 1
#     return count