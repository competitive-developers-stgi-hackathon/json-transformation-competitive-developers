import csv
import json


def shift(file, data):
    data["operation"] = "shift"

    n = len(file)
    content = {}
    for i in range(n):
        
        if (len(file[i][2]) == 2):
            if "+" not in file[i][1]:
                dot_split = file[i][1].split(".")
                dot_split = dot_split[1:]
                
                if len(dot_split) == 1:
                    content[file[i][0]] = dot_split[0]
                else:
                    dot_copy = dot_split
                    dot_split.reverse()

                    past = {}
                    past[dot_split[0]] = row[1]
                    cur = {}
                    dot_split = dot_split[1:]
                
                    for x in dot_split:
                        cur[x] = past
                        past = cur

                # print(past)
                    for x in past:
                        content[x] = past[x]

                
    data["spec"] = content
    return data


with open ("mapping.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    output = []
    file = []
    data = {}
    for row in reader:
        file.append(row[1:])
        
    
    output.append(shift(file,data))
    print(output)

    # print(data)
with open("mapping.json", "w") as f:
    json.dump(data, f)

