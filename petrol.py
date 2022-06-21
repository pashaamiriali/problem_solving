import os


def calculate_next_month_fuel_payment(petrol, quota):
    total_quota = quota + 60
    remained = total_quota - petrol
    if remained >= 0:
        return petrol * 1500
    if remained < 0:
        to_pay = total_quota * 1500
        to_pay += (remained * -1) * 3000
        return to_pay


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    petrol = int(input().strip())
    quota = int(input().strip())

    result = calculate_next_month_fuel_payment(petrol, quota)

    # fptr.write(str(result) + '\n')
    print(str(result) + '\n')
    # fptr.close()
