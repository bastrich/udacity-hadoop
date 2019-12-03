import sys
from decimal import Decimal

def reducer():

    sum = Decimal(0)
    count = 0
    old_key = None

    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        this_key, this_sale = data

        if old_key and old_key != this_key:
            print("{0}\t{1}".format(old_key, sum/count))

            sales_total = Decimal(0)

        old_key = this_key
        sum += Decimal(this_sale)
        count += 1

    if old_key:
        print("{0}\t{1}".format(old_key, sum/count))


def main():
    reducer()


if __name__ == "__main__":
    main()
