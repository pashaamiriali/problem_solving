
def main():
    nk = list(map(int, input().strip().split()))[:2]
    if nk[0] > 100 or nk[0] < 2:
        print('n is too big')
        return
    if nk[1] > 100 or nk[1] < 1:
        print('k is too big')
        return
    arr_in = input()
    arr = list(map(int, arr_in.strip().split()))[:nk[0]]
    print(find_pairs(arr, nk[0], nk[1]))


def find_pairs(arr, n,k):
    pairs = 0
    for i in range(0, n):
        for j in range(i+1, len(arr)):
            if i == j:
                continue
            if (arr[i]+arr[j]) % k == 0:
                pairs += 1
    return pairs


if __name__ == '__main__':
    main()
