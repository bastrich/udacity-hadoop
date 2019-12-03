import sys
import csv


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    next(reader)

    for line in reader:
        author_id = line[3]
        added_at = line[8][11:13]

        writer.writerow([author_id + ' ' + added_at, 1])


def main():
    mapper()


if __name__ == "__main__":
    main()
