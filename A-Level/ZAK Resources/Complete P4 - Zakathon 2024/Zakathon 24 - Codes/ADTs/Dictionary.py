# dictionary practices
# thisDict = {"name" : "ABC", "age" : 19, "class" : "a2s3", "examPassed" : True}

file = open("pafData.txt", "rt")
stuName = ""
stuAge = 0
stuArr = []

sturec = file.readline()
while sturec != "":
    stuName, stuAge = sturec.split()
    dictItem = {"name" : stuName, "age" : int(stuAge)}
    stuArr.append(dictItem)

    sturec = file.readline()
file.close()

"""
for i in stuArr:
    print(i)

xAge = stuArr[2]["age"]
print(xAge)
"""

newFile = open("newfiledictpaf.txt", "wt")
for i in stuArr:
    newFile.write(str(i) + "\n")
newFile.close()

stuArr.clear()

newFile = open("newfiledictpaf.txt", "rt")
for i in newFile:
    stuArr.append(eval(i)) # eval method cast string to dictionary
newFile.close()

for i in range(len(stuArr)):
    print(stuArr[i]["age"])