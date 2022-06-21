import os
import math


def repeated_string(s, n):
    a_proportion = find_a_proportions(s)
    if a_proportion == 0:
        return 0
    a_count = 0

    if n % len(s) != 0:
        a_count = int((a_proportion*math.floor(n/len(s))))
        remaining = int(n-(a_count/a_proportion*len(s)))
        if remaining <= len(s):
            for c in s[0:remaining:1]:
                if c == 'a':
                    a_count += 1
        else:
            for c in s[0:(remaining-len(s)):1]:
                if c == 'a':
                    a_count += 1
            a_count += a_proportion
    else:
        a_count = int((a_proportion*(n/len(s))))
    return a_count


def find_a_proportions(s):
    a_proportion = 0
    for c in s:
        if c == 'a':
            a_proportion += 1
    return a_proportion


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeated_string(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
