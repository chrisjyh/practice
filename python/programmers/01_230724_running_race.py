players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
answer = []

dic_pl = {}
dic_no = {}

for key, value in enumerate(players):
    dic_pl[key] = value
    dic_no[value] = key

for i in callings:
    num = dic_no[i]
    dic_pl[num], dic_pl[num-1] = dic_pl[num-1], dic_pl[num]
    dic_no[dic_pl[num]], dic_no[dic_pl[num-1]] = dic_no[dic_pl[num-1]], dic_no[dic_pl[num]] 

print(dic_pl)

for values in dic_pl.values():
    answer.append(values)

print(answer)
    



