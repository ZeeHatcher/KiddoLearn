with open(r"lesson\animals.txt", "r") as f:
    cont = f.readlines()

    gif = []
    item = []

    for line in cont:
        c = eval(line)
        gif.append(c["examples"])
        item.append(c["item"])

dict = {}
for i in range(len(item)):
    dict[gif[i]] = item[i]

print(dict)
