import utils.utils as utils

open_nodes=[]

def insert_node(node):
    global open_nodes
    if len(open_nodes)==0: open_nodes.append(node)
    else:
        inserted=False
        for i in range(len(open_nodes)-1,-1,-1):
            if (node['risk'] > open_nodes[i]['risk']):
                open_nodes.insert(i+1,node)
                inserted=True
                break
        if not inserted: 
            open_nodes.insert(0,node)
    return

inp_list = utils.read_num_list("files/task15.txt")
dij_field = []
for i in range(len(inp_list)):
    new_line=[]
    for j in range(len(inp_list[i])):
        new_line.append({'pos': (i,j), 'pre': None, 'risk': -1,
        'finished': False, 'value':inp_list[i][j]})
    dij_field.append(new_line)
dij_field[0][0]['risk']=0   
open_nodes.append(dij_field[0][0])
finished=False
while not finished:
    curr_node = open_nodes.pop(0)
    curr_node['finished']=True
    n_pos=[(curr_node['pos'][0]-1, curr_node['pos'][1]), (curr_node['pos'][0], curr_node['pos'][1]-1),
    (curr_node['pos'][0]+1, curr_node['pos'][1]), (curr_node['pos'][0], curr_node['pos'][1]+1)]
    n_list=[]
    for elem in n_pos:
        if elem[0]>=0 and elem[0]<len(inp_list) and elem[1]>=0 and elem[1]<len(inp_list[0]):
            if not dij_field[elem[0]][elem[1]]['finished']:
                new_risk = curr_node['risk']+dij_field[elem[0]][elem[1]]['value']
                if dij_field[elem[0]][elem[1]]['risk']>=0:
                    if new_risk<dij_field[elem[0]][elem[1]]['risk']:
                        dij_field[elem[0]][elem[1]]['risk']=new_risk
                        dij_field[elem[0]][elem[1]]['pre']=(curr_node['pos'])
                else:
                    dij_field[elem[0]][elem[1]]['risk']=new_risk
                    dij_field[elem[0]][elem[1]]['pre']=(curr_node['pos'])
                    if elem[0]==len(inp_list)-1 and elem[1]==len(inp_list[0])-1: 
                        finished=True
                        break
                    else: 
                        insert_node(dij_field[elem[0]][elem[1]])
print (f"Result = {dij_field[len(dij_field)-1][len(dij_field[0])-1]['risk']}")
finished=False
curr_node=dij_field[len(dij_field)-1][len(dij_field[0])-1]
# while not finished:
#     if curr_node['pos']==(0,0): finished=True
#     else:
#         print(curr_node['pos'],'   ',curr_node['risk'],'   ',curr_node['value'])
#         curr_node=dij_field[curr_node['pre'][0]][curr_node['pre'][1]]