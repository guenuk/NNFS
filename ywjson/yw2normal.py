import json
with open("./via_region_data_yw.json", "r") as f:
    file = json.load(f)
print(file)
count =0
for key in file:
    count += 1
print(count)

for key in file:
    for key2 in list(file[key]):
        print(key2)
        if key2 == "fileref" or key2 == "base64_img_data" or key2 == "file_attributes":
            file[key].pop(key2)
            print("POP")
        elif key2 == 'regions':
            temp = []
            for rKey in file[key][key2]:
                temp.append(file[key][key2][rKey])
            print(temp)
            for e in temp:
                if 'region_attributes' in e:
                    print(e['region_attributes'])
                    for typeKey in list(e['region_attributes']):
                        print(typeKey)
                        print(e['region_attributes'][typeKey])
                        if e['region_attributes'][typeKey] == "":
                            e['region_attributes'].pop(typeKey)
                            continue
                        e['region_attributes']['type'] = e['region_attributes'].pop(typeKey)
                        print(e['region_attributes'])

                        # e['type'] = e['region_attributes'].pop(typeKey)
                    print(e)
                print(temp)

            file[key][key2] = temp
print(file)

#uncomment to write file
# with open('result.json', "w") as outfile:
#     json.dump(file,outfile)


