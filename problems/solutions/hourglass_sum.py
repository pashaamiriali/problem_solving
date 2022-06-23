
import os

limit = 3


def hourglass_sum(arr):

    length = len(arr)
    total = traverse_y(arr, length)
    return total


def traverse_y(arr, length):
    total = -999
    for i in range(length):
        if (length-i) >= limit:
            total = traverse_x(arr, length, total, i)
        else:
            break
    return total


def traverse_x(arr, length, total, i):
    for j in range(length):
        if (length-j) >= limit:
            _sum = sum_hourglass(arr, i, j)
            if _sum > total:
                total = _sum
        else:
            break
    return total


def sum_hourglass(arr, i, j):
    total = 0

    for a in range(3):
        if a == 1:
            total += arr[i+1][j+1]
            continue
        for b in range(3):
            total += arr[i+a][j+b]

    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglass_sum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
