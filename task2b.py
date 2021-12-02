with open("files/task2.txt") as f: content = f.read().splitlines()
aim=0; position=0; depth=0
for i in range(0,len(content)):
    curr=content[i].split(" ")
    if curr[0] =='up': aim=aim-int(curr[1])
    if curr[0] =='down': aim=aim+int(curr[1])
    if curr[0] =='forward': 
        position=position+int(curr[1])
        depth = depth+(int(curr[1])*aim)
print (f"Aim={aim}"); print (f"Depth={depth}"); print (f"Position={position}")
print (f"Result={depth*position}")