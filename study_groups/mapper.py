import sys
import csv


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    next(reader)

    for line in reader:
        node_id = line[0]
        node_type = line[5]
        abs_parent_id = line[7]
        author_id = line[3]

        if node_type == 'question':
            writer.writerow([node_id, author_id])
        else:
            writer.writerow([abs_parent_id, author_id])


def main():
    mapper()


if __name__ == "__main__":
    main()
