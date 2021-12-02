with open("files/task1.txt") as f: content = f.read().splitlines()
count=0
for i in range(0,len(content)-3):
    if int(content[i+3])>int(content[i]): count=count+1
print (f"Number={count}")