"""
Processes and mergesfiles to desired format
"""
from os import listdir

IN_DIR = "C:/Users/Inofearu/Desktop/Work/Work Experience/quantium-starter-repo/raw_data"
OUT_FILE = "C:/Users/Inofearu/Desktop/Work/Work Experience/quantium-starter-repo/data/merged_sales_data.csv"
NEW_HEADER = "product,sales,date,region"

with open(OUT_FILE,"w", encoding = "UTF-8") as out_file:
    out_file.write(F"{NEW_HEADER}\n")
    for index in range(len(sorted(listdir(IN_DIR)))):
        with open(f"{IN_DIR}/daily_sales_data_{index}.csv", "r", encoding = "UTF-8") as in_file:
            if index == 0:
                header_count = len(in_file.readline().split(",")) - 1
            storedlines = []
            for line in in_file: # split into 2d array
                content = line.split(",")
                if content[0] != "pink morsel": # filter to product
                    continue
                storedlines.append(content)
            for line in storedlines: # multiply price and quantity to get sales
                line[1] = line[1][1:] # dollar trim
                sales = float(line[1]) * int(line[2])
                line[1] = sales; line.pop(2) # remove price and quantity#
                _index = 0
                for item in line:
                    _index += 1
                    item = str(item)
                    if _index == header_count:
                        out_file.write(f"{item.strip()}\n")
                        _index = 0
                    else:
                        out_file.write(f"{item.strip()},")
