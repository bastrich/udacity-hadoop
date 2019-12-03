import sys
import csv


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    next(reader)

    for line in reader:
        node_id = line[0]
        length = len(line[4])
        node_type = line[5]
        parent_id = line[6]

        if node_type == 'question':
            writer.writerow([node_id, 'question', length])

        if node_type == 'answer':
            writer.writerow([parent_id, 'answer', length])


def main():
    mapper()


if __name__ == "__main__":
    main()
