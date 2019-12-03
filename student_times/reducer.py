import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    sum = 0
    max_h = 0
    old_id = None
    old_hour = None

    max_list = []

    for line in reader:
        this_id, this_hour = line[0].split(' ')

        if old_id and old_id != this_id:

            if sum > max_h:
                max_list = [[old_id, old_hour]]
                max_h = sum
            else:
                if sum == max_h:
                    max_list.append([old_id, old_hour])

            for row in max_list:
                writer.writerow(row)

            sum = 0
            max_h = 0
            max_list = []
        else:
            if old_hour and old_hour != this_hour:
                if sum > max_h:
                    max_list = [[old_id, old_hour]]
                    max_h = sum
                else:
                    if sum == max_h:
                        max_list.append([old_id, old_hour])

                sum = 0

        old_id = this_id
        old_hour = this_hour

        sum += 1

    if old_id:
        if sum > max_h:
            max_list = [[old_id, old_hour]]
        else:
            if sum == max_h:
                max_list.append([old_id, old_hour])

        for row in max_list:
            writer.writerow(row)


def main():
    reducer()


if __name__ == "__main__":
    main()
