import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    result = []
    old_key = None

    for line in reader:
        this_key = line[0]

        if old_key and old_key != this_key:
            writer.writerow(result)

            result = []

        old_key = this_key

        if line[1] == 'A':
            result = line[2:] + result

        if line[1] == 'B':
            result = result + line[2:]

    if old_key:
        writer.writerow(result)


def main():
    reducer()


if __name__ == "__main__":
    main()
