from math import sqrt


x1, y1 = int(input('Enter x1: ')), int(input('Enter y1: '))
x2, y2 = int(input('Enter x2: ')), int(input('Enter y2: '))


def distance(*args):
    w = [args[i:i + 2] for i in range(0, len(args), 2)]
    q = list(map(lambda x: sqrt((x[0][0]-x[1][0])**2 + (x[0][1]-x[1][1])**2), w))
    return q


result1 = distance((x1, y1), (x2, y2))
result2 = distance((15, 11), (9, 17), (3, 4), (9, 1))

print(result1, result2, sep='\n')
