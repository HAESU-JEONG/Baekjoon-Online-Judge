while True:
    string = input()
    if string == "EOI":
        break
    string2 = string.lower()
    if string2.find("nemo") != -1:
        print("Found")
    else:
        print("Missing")