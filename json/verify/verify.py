import json
with open("./merge482.json", "r") as f:
    file = json.load(f)

def count():
    count = 0
    for key in file:
        count+=1
    print("COUNT:   ", count)

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
count()




