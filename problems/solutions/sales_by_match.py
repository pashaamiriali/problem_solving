import os


def sock_merchant(n, ar):
    sock_dict = {}
    for i in range(0, n):
        if ar[i] not in sock_dict:
            sock_dict[ar[i]] = 0
        sock_dict[ar[i]] += 1
    pairs = 0
    for key in sock_dict:
        sock_count = sock_dict[key]
        if sock_count == 2:
            pairs += 1
            continue
        if sock_count > 2 and sock_count % 2 == 0:
            pairs += sock_count/2
        else:
            pairs += (sock_count-1)/2
    return int(pairs)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sock_merchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
