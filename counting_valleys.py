import os


def counting_valleys(steps, path):
    SEE_LEVEL = 0
    level = 0
    valley_count = 0
    for i in range(0, steps):
        step = path[i].upper()
        if step == 'D':
            level -= 1
        elif step == 'U':
            level += 1
        if level == (SEE_LEVEL-1) and step == 'D':
            valley_count += 1
    return valley_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = counting_valleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
