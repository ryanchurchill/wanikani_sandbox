import csv

kanji_map = {}

with open('kanji.txt', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')

    for row in csv_reader:
        # print(row)
        if (row[0][0] != '#'):
            kanji_map[row[3]] = '<div>' + row[2] + '<br><br>' + 'onyomi: ' + row[5] + '<br><br>' + 'kunyomi: ' + row[6];


for key in kanji_map:
    print(key + ';' + kanji_map[key])
