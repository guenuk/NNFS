import json
with open("./58v2.json", "r") as f:
    file = json.load(f)
# print(file)


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
def hw2normal():
    for key in file:
        for key2 in list(file[key]):
            print(key2)
            if key2 == "fileref" or key2 == "base64_img_data" or key2 == "file_attributes":
                file[key].pop(key2)
                print("POP")
            elif key2 == "file_attributes":
                file[key][key2] = {}
            elif key2 == 'regions':
                if not isinstance(file[key][key2], list):
                    temp = []
                    for rKey in file[key][key2]:
                        # print(file[key][key2][rKey])
                        print('file[key][key2] ', file[key][key2])
                        print('rKey ', rKey)
                        print('file[key][key2][rKey] ' , file[key][key2][rKey])
                        temp.append(file[key][key2][rKey])
                    print(temp)
                    # print(file[key][key2])
                    for e in temp:
                        if 'region_attributes' in e:
                            print('region_attribues: ', e['region_attributes'])
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
        file[key]['file_attributes'] = {}
    print(file)


    #uncomment to write file
    # with open('result.json', "w") as outfile:
    #     json.dump(file,outfile)

    # with open('482v2.json', "w") as outfile:
    #     json.dump(file,outfile)
    with open('58v2.json', "w") as outfile:
        json.dump(file,outfile)
    count =0
    for key in file:
        print(key)
        count += 1
    print(count)

def is_polygon():
    for key in file:
        for key2 in list(file[key]):
            if key2 == "regions":
                for key3 in file[key][key2]:
                    # print(file[key][key2])
                    # print(key3)
                    for key4 in key3:
                        # print(key4)
                    # for key4 in file[key][key2][key3]:
                        if key4 == "shape_attributes":
                            # print(key3[key4])
                            for key5 in key3[key4]:
                                if key5 == 'name':
                                    # print(key3[key4][key5])
                                    if key3[key4][key5] == "polygon":
                                        print("PASS")
                                    else:
                                        print("[@@@ NOT POLYGON @@@] Filename: ", key)

def is_minkb():
    for key in file:
        for key2 in list(file[key]):
            if key2 == "regions":
                for key3 in file[key][key2]:
                    # print(file[key][key2])
                    # print(key3)
                    for key4 in key3:
                        # print(key4)
                    # for key4 in file[key][key2][key3]:
                        if key4 == "region_attributes":
                            # print(key3[key4])
                            for key5 in key3[key4]:
                                if key5 == 'type':
                                    # print(key3[key4][key5])
                                    if key3[key4][key5] == "M" or key3[key4][key5] == "I" or key3[key4][key5] == "N" or key3[key4][key5] == "K" or key3[key4][key5] == "B":
                                        print("PASS")
                                    else:
                                        print("[@@@ Wrong type @@@] Filename: ", key)

is_polygon()
is_minkb()




