
myfile = open("files/task1.txt", "r")
myline = myfile.readline()
last = int(myline)
count=0
while myline:
    myline = myfile.readline()
    if not (myline==""):
        if (int(myline) > last): count +=1
        last=int(myline)
myfile.close()   
print (f"Anzahl: {count}")
