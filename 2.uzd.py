import csv 
with open('fail.CSV', 'r') as csv_file:
    lasitajs=csv.reader(csv_file)

    for row in lasitajs:
        print(row)
csv_file.close()