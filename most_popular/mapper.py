import sys


def mapper():
    for line in sys.stdin:
        data = line.strip().split(' ')

        path = data[6]
        if path.startswith('http://www.the-associates.co.uk'):
            path = path[31:]

        print("{0}\t{1}".format(path, 1))


def main():
    mapper()


if __name__ == "__main__":
    main()
