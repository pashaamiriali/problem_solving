def main():
    inputs = validate_input(get_inputs())
    if(inputs == None):
        print('invalid input exiting...')
        return
    print(traverse(inputs['ch_bar'], inputs['d'], inputs['m']))


def get_inputs():
    inputs = {'ch_bar': [], 'd': 0, 'm': 0}
    n = int(input())
    inputs['ch_bar']=list(map(int,input().strip().split()))[:n]
    dm = list(map(int, input().strip().split()))[:2]
    inputs['d'] =dm[0]
    inputs['m'] = dm[1]
    return inputs


def validate_input(inputs):
    if len(inputs['ch_bar']) > 100 or len(inputs['ch_bar']) < 1:
        return None
    if inputs['d'] > 31 or inputs['d'] < 1:
        return None
    if inputs['m'] > 12 or inputs['d'] < 1:
        return None
    return inputs


def traverse(ch_bar: list, d, m):
    solutions = 0
    for i in range(0, len(ch_bar)):
        sq_sum = 0
        for j in range(i, i+m):
            if j>len(ch_bar)-1:
                break
            sq_sum += ch_bar[j]
        if sq_sum == d:
            solutions += 1
    return solutions


if __name__ == "__main__":
    main()
