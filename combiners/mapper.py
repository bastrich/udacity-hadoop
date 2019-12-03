import sys
from datetime import datetime

def mapper():
    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 6:
            continue

        date, time, store, category, cost, payment = data

        print("{0}\t{1}".format(datetime.strptime(date, "%Y-%m-%d").weekday(), cost))


def main():
    mapper()


if __name__ == "__main__":
    main()
