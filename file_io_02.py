# with open("text.txt","w") as f:
#     w = f.write("this is a new line \n")
#     print(w)

with open("text.txt","w") as f:
    dict = {"name :":"gautam kumar","age :":"21 years","Mobile_no :":"+91 9304157406"}
    newDict = str(dict)
    n = f.write(newDict)
    print(n)
