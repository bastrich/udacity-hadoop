import sys
from decimal import Decimal

def reducer():

    total_number = 0
    total_value = Decimal(0)

    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        _, sale = data

        total_number += 1
        total_value += Decimal(sale)

    print("{0}\t{1}".format(total_number, str(total_value)))


def main():
    reducer()


if __name__ == "__main__":
    main()
