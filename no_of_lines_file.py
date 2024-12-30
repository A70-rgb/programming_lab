f=open("D:\\programming lab\\files\\file1.txt.txt", "r")
countlines=0
for line in f.readlines():
    countlines=countlines+1
print("No.of lines:",countlines)
f.close()