import math
# def cooking_time(eggs):
#     if not eggs:
#         return 0
#     elif not eggs % 8:
#         return eggs//8*5
#     else:
#         return (eggs//8+1)*5

def cooking_time(eggs):
    return math.ceil(eggs/8)*5

if __name__ == '__main__':
    print(cooking_time(8))
