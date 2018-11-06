""" there is an array, if there are 3+ 'good' return  'I smell a series!'
if there one 'good' - 'Publish!', if there is not 'Fail!'"""


def well(arr):
    good = [str(x).lower() == 'good' for y in arr for x in y]
    if sum(good) >  2:
        return "I smell a series!"
    elif sum(good):
        return "Publish!"
    else:
        return "Fail!"


if __name__ == '__main__':
    print(well([['bad', 'bAd', 'bad'], ['bad', 'bAd', 'bad'], ['bad', 'bAd', 'bad']]))