"""We have to find the longest substring of identical characters in a very long
string.

Let's see an example:

s1 = "1111aa994bbbb1111AAAAAFF?<mmMaaaaaaaaaaaaaaaaaaaaaaaaabf"
The longest substring in s1 is "aaaaaaaaaaaaaaaaaaaaaaaaa" having a
length of 25, made of character, "a", with its corresponding ascii code equals
to "97", and having its starting index 29 and the ending one 53.

We express the results using an array in the following order:
["97", 25, [29,53]]
[ord, len, [beg, end]]
The symbols '!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~' that a string may have will be
 as noise, so they cannot be a solution even though the substring, made of one
 of them, is the longest of all. In other words, the allowed characters may
 the uppercase or lower letters of the English alphabet or the decimal digits
 ('0123456789')

Let's see an example to show what happens if we have non alphanumeric symbols.

s2 = "1111aa994bbbb1111AAAAAFF????????????????????????????" The
longest substring is "AAAAA" so the result for it is:

['65', 5, [17, 21]]
If there are two or more substrings with the maximum length value,
it will be chosen the one that starts first, from left to right.

Make an agile code that may output an array like the one shown
above when it receives a huge string."""

filter_chars = """!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"""
result = [[]]
test_string = 'aaaaaaa1111111111'


def substring(string, character, begining):
    


def find_longest_substr(s):
    
    return result
