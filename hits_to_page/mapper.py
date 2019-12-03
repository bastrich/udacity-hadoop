import sys


def mapper():
    for line in sys.stdin:
        data = line.strip().split(' ')

        print("{0}\t{1}".format(data[6], 1))


def main():
    mapper()


if __name__ == "__main__":
    main()
