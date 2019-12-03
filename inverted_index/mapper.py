import sys
import csv
import re


def mapper():
        reader = csv.reader(sys.stdin, delimiter='\t')

        next(reader, None)

        for line in reader:
            words = line[4].strip()\
                .replace('.', ' ')\
                .replace(',', ' ')\
                .replace('!', ' ')\
                .replace('?', ' ')\
                .replace(':', ' ')\
                .replace(';', ' ')\
                .replace('"', ' ')\
                .replace('(', ' ')\
                .replace(')', ' ')\
                .replace('<', ' ')\
                .replace('>', ' ')\
                .replace('[', ' ')\
                .replace(']', ' ')\
                .replace('#', ' ')\
                .replace('$', ' ')\
                .replace('=', ' ')\
                .replace('-', ' ')\
                .replace('/', ' ')\

            words = re.sub(r'\s', ' ', words)

            words = words.split(' ')

            for word in words:
                if word == '':
                    continue
                print('{0}\t{1}'.format(word.lower(), int(line[0])))


def main():
    mapper()


if __name__ == "__main__":
    main()
