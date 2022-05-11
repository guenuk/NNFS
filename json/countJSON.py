import json
with open("./482v2.json ", "r") as f:
    file = json.load(f)
print(file)
count =0
for key in file:
    count += 1
print(count)