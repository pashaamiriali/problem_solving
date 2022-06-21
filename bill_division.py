def evaluate_bill_division(bills, refused, charge):
    actual = find_actual_charge(bills, refused)
    return compare_actual_with_given_charge(actual, charge)


def find_actual_charge(bills, refused):
    charge = 0
    for i in range(0, len(bills)):
        if i == refused:
            continue
        charge += bills[i]
    return int(charge/2)


def compare_actual_with_given_charge(actual, given):
    if(given-actual) != 0:
        return given-actual
    else:
        return 'Bon Appetit'


def main():
    nk = list(map(int, input().strip().split()))[:2]
    bills = list(map(int, input().strip().split()))[:nk[0]]
    b = int(input())
    print(evaluate_bill_division(bills, nk[1], b))


if __name__ == '__main__':
    main()
