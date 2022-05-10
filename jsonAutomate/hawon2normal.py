import json
with open("./merge.json", "r") as f:
    file = json.load(f)
print(file)
count =0
for key in file:
    print(key)
    count += 1
print(count)

# with open("./set_1.json", "r") as f:
#     set1 = json.load(f)
# print(file)
#
# count =0
# for key in set1:
#     print(key)
#     count += 1
# print(count)
#
# with open("./set_2.json", "r") as f:
#     set2 = json.load(f)
# # print(file2)
# count =0
# for key in set2:
#     print(key)
#     count += 1
# print(count)

# count=0
# for key in set2:
#     print(key)
#     match = False
#     for key2 in set1:
#         if key == key2 :
#             match = True
#             count += 1
#             break
#     if not match :
#         print(key + " does not exist")
# print(count)

for key in file:
    for key2 in list(file[key]):
        print(key2)
        if key2 == "fileref" or key2 == "base64_img_data" or key2 == "file_attributes":
            file[key].pop(key2)
            print("POP")
        elif key2 == 'regions':
            temp = []
            for rKey in file[key][key2]:
                # print(file[key][key2][rKey])
                temp.append(file[key][key2][rKey])
            print(temp)
            # print(file[key][key2])
            for e in temp:
                if 'region_attributes' in e:
                    print(e['region_attributes'])
                    for typeKey in list(e['region_attributes']):
                        print(typeKey)
                        print(e['region_attributes'][typeKey])
                        if e['region_attributes'][typeKey] == "":
                            e['region_attributes'].pop(typeKey)
                            continue
                        e['region_attributes']['type'] = typeKey
                        e['region_attributes'].pop(typeKey)
                        print(e['region_attributes'])

                        # e['type'] = e['region_attributes'].pop(typeKey)
                    print(e)
                print(temp)

            file[key][key2] = temp
print(file)


#uncomment to write file
with open('result.json', "w") as outfile:
    json.dump(file,outfile)


