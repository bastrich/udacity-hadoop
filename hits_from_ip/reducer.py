import sys

def reducer():

    hits_total = 0
    old_key = None

    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        page, _ = data

        if old_key and old_key != page:
            print("{0}\t{1}".format(old_key, hits_total))

            hits_total = 0

        old_key = page
        hits_total += 1

    if old_key:
        print("{0}\t{1}".format(old_key, hits_total))


def main():
    reducer()


if __name__ == "__main__":
    main()
