import sys
import csv


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        if line[0] == 'user_ptr_id' or line[0] == 'id':
            continue

        if len(line) == 19:
            id, title, tagnames, author_id, _, node_type, parent_id, abs_parent_id, added_at, score, _, _, _, _, _, _, _, _, _ = line
            writer.writerow([author_id, 'A', id, title, tagnames, author_id, node_type, parent_id, abs_parent_id, added_at, score])

        if len(line) == 5:
            user_ptr_id, reputation, gold, silver, bronze = line
            writer.writerow([user_ptr_id, 'B', reputation, gold, silver, bronze])


def main():
    mapper()


if __name__ == "__main__":
    main()
