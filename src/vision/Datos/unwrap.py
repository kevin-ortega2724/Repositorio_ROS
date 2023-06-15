import csv

def remove_after_quote(csv_file, col_num):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        for row in rows:
            row[col_num] = row[col_num].split('"')[0]
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
remove_after_quote('poseszzz.csv', 5)
