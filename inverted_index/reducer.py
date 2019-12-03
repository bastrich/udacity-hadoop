import sys

def reducer():
    nodes = []
    old_key = None

    for line in sys.stdin:
        data = line.strip().split('\t')

        if len(data) != 2:
            continue

        word = data[0]
        node = data[1]

        if old_key and old_key != word:
            nodes.sort()
            print('{0}\t{1}'.format(old_key, nodes))

            nodes = []

        old_key = word
        nodes.append(int(node))

    if old_key:
        nodes.sort()
        print('{0}\t{1}'.format(old_key, nodes))

def main():
    reducer()


if __name__ == "__main__":
    main()
