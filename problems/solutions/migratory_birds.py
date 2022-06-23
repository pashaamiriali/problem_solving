n = int(input())
arr = list(map(int, input().strip().split()))[:n]
arr_map = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
for i in range(0, n):
    arr_map[arr[i]] += 1
first = 0
second = 0
for i in range(1, 6):
    if arr_map[i] > arr_map[second]:
        second = i
    if arr_map[i] > arr_map[first]:
        first = i
if arr_map[first] == arr_map[second]:
    if first > second:
        print(second)
    else:
        print(first)
else:
    print(first)
