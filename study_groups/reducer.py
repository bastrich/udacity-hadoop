import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    old_node_id = None
    students = []

    for line in reader:
        node_id = line[0]

        if old_node_id and old_node_id != node_id:
            writer.writerow([old_node_id, students])

            students = []

        old_node_id = node_id
        students.append(line[1])

    if old_node_id:
        writer.writerow([old_node_id, students])



def main():
    reducer()


if __name__ == "__main__":
    main()
