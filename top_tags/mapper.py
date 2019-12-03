import sys
import csv


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    next(reader)

    for line in reader:
        node_type = line[5]
        if node_type == 'question':
            tags = line[2].split(' ')
            for tag in tags:
                writer.writerow([tag, 1])


def main():
    mapper()


if __name__ == "__main__":
    main()
