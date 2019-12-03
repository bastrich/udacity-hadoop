import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    old_node_id = None

    question_id = None
    question_length = 0
    answer_sum_length = 0
    answer_count = 0

    for line in reader:
        node_id, node_type, length = line

        if old_node_id and old_node_id != node_id:
            if question_id:
                if answer_count != 0:
                    average_answer_length = answer_sum_length/answer_count
                else:
                    average_answer_length = 0

                writer.writerow([question_id, question_length, average_answer_length])

            question_id = None
            question_length = 0
            answer_sum_length = 0
            answer_count = 0

        old_node_id = node_id
        if node_type == 'question':
            question_id = node_id
            question_length = int(length)
        else:
            answer_sum_length += int(length)
            answer_count += 1

    if old_node_id:
        if question_id:
            if answer_count != 0:
                average_answer_length = answer_sum_length / answer_count
            else:
                average_answer_length = 0

            writer.writerow([question_id, question_length, average_answer_length])


def main():
    reducer()


if __name__ == "__main__":
    main()
