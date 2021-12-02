with open("files/task2.txt") as f: content = f.read().splitlines()
position=0
depth=0
for i in range(0,len(content)):
    curr=content[i].split(" ")
    if curr[0] =='up': depth=depth-int(curr[1])
    if curr[0] =='down': depth=depth+int(curr[1])
    if curr[0] =='forward': position=position+int(curr[1])
print (f"Depth={depth}")
print (f"Position={position}")
print (f"Result={depth*position}")