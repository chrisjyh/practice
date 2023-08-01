import os

practice_dic = {
    "python": ['programmers', 'baeckjoon'],
    "SQL": ['programmers', 'hackerrank']
}

sql_temp = {
    "01":[],
    "02":[],
    "03":[],
    "04":[],
    "05":[],    
}

#
for k, v in practice_dic.items():
    for detail_v in v:
        path = f"./{k}/{detail_v}/"
        if k == "python":
            pass
        else:
            with os.scandir(path) as entries:
                for entry in entries:
                    if entry.is_file():
                        sql_temp[entry.name.split("_")[0]].append(entry.name.split("_")[1])

print(sql_temp)

# for k, lv in sql_temp.items():
f = open("./README.md", 'r', encoding='UTF8')
line = f.readline()
print(line)
f.close()
