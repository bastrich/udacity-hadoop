import sys
from decimal import Decimal

def reducer():

    highest_sale = 0
    old_key = None

    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        this_key, this_sale = data

        if old_key and old_key != this_key:
            print("{0}\t{1}".format(old_key, highest_sale))
            highest_sale = 0

        old_key = this_key
        if float(this_sale) > highest_sale:
            highest_sale = float(this_sale)

    if old_key:
        print("{0}\t{1}".format(old_key, highest_sale))


def main():
    reducer()


if __name__ == "__main__":
    main()
