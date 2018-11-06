"""11111111  00000000  00001111  10101010
  byte1     byte2     byte3     byte4
should become:

10101010  00001111  00000000  11111111
  byte4     byte3     byte2     byte1
"""
'''
zebulan
def data_reverse(data):
    return [b for a in range(len(data) - 8, -1, -8) for b in data[a:a + 8]]
'''


def data_reverse(data):
    result = []
    for i in range(8, len(data)+1, 8):
        result.append(data[i-8:i])
    result.reverse()
    return [x for y in result for x in y]

if __name__ == '__main__':
    print(data_reverse([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]))