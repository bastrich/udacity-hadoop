import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    old_tag = None
    top_tags = []
    tag_count = 0

    for line in reader:
        tag = line[0]

        if old_tag and old_tag != tag:
            if len(top_tags) == 0:
                top_tags.append([old_tag, tag_count])
            else:
                i = 0
                for top_tag in top_tags:
                    if top_tag[1] >= tag_count:
                        top_tags.insert(i, [old_tag, tag_count])
                        break
                    if i == len(top_tags) - 1:
                        top_tags.append([old_tag, tag_count])
                        break
                    i += 1

            if len(top_tags) > 10:
                top_tags.pop(0)

            tag_count = 0

        old_tag = tag
        tag_count += 1

    if old_tag:
        if len(top_tags) == 0:
            top_tags.append([old_tag, tag_count])
        else:
            i = 0
            for top_tag in top_tags:
                if top_tag[1] >= tag_count:
                    top_tags.insert(i, [old_tag, tag_count])
                    break
                if i == len(top_tags) - 1:
                    top_tags.append([old_tag, tag_count])
                    break
                i += 1

        if len(top_tags) > 10:
            top_tags.pop(0)

    for tag in reversed(top_tags):
        writer.writerow(tag)


def main():
    reducer()


if __name__ == "__main__":
    main()
