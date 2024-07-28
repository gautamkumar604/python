# temp = open("text.txt","r")
# r = temp.read()
# print(r)

# temp.close()
# print(temp.read()) #produce an error becouse you operate on closed file

# with open('text.txt', 'r') as f:    
#     for i, line in enumerate(f):         
#         print('Line', i, '--', line)

with open("text.txt","r") as f:
    # l = len(f.readline())
    # print(l)
    # r = f.readline()
    # print(r)

    for line in f:
        print(line, end="")
    