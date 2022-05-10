import json
with open("./merge.json", "r") as f:
    file = json.load(f)
print(file)
count =0
for key in file:
    count += 1
print(count)