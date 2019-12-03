import sys

def reducer():

    max_hits = 0
    max_page = None
    current_hits = 0
    old_key = None

    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        page, _ = data

        if old_key and old_key != page:
            if current_hits > max_hits:
                max_hits = current_hits
                max_page = old_key

            current_hits = 0

        old_key = page
        current_hits += 1

    if old_key:
        if current_hits > max_hits:
            max_hits = current_hits
            max_page = old_key

    print("{0}\t{1}".format(max_page, max_hits))


def main():
    reducer()


if __name__ == "__main__":
    main()
