import math

def check_packet(packet_bin):
    end_ind = 0
    ver_value = 0
    v = int(packet_bin[0:3],2)
    t = int(packet_bin[3:6],2)
    ver_value += v
    if t == 4:
        num_point = 6
        str_val = ""
        while packet_bin[num_point:num_point+1] == "1": 
            str_val += packet_bin[num_point+1:num_point+5]
            num_point += 5 
        str_val += packet_bin[num_point+1:num_point+5]
        value = int(str_val,2)
        end_ind = num_point + 4
    else:
        val_list =[]
        if packet_bin[6:7] == '0':
            num_bits = int(packet_bin[7:22],2)
            end_ind = 0
            while end_ind < num_bits:
                v, e, val = check_packet(packet_bin[22+end_ind:22+num_bits])
                val_list.append(val)
                end_ind = end_ind + e + 1
                ver_value += v
            end_ind = 21 + num_bits
        else:
            num_packets = int(packet_bin[7:18],2)
            start = 18
            for i in range(num_packets):
                v, end_ind, val = check_packet(packet_bin[start:])
                val_list.append(val)
                ver_value += v
                start = start + end_ind + 1
            end_ind = start - 1
        if t == 0: value = sum(val_list)
        if t == 1: value = math.prod(val_list)
        if t == 2: value = min(val_list)
        if t == 3: value = max(val_list)
        if t == 5: 
            if val_list[0] > val_list[1]: value = 1
            else: value = 0
        if t == 6: 
            if val_list[0] < val_list[1]: value = 1
            else: value = 0
        if t == 7: 
            if val_list[0] == val_list[1]: value = 1
            else: value = 0

    return ver_value, end_ind, value

with open("files/task16.txt") as f: packet_hex = f.readline().strip()
packet_bin = ""
for i in range(len(packet_hex)):
    bin_str = "{0:04b}".format(int(packet_hex[i], 16))
    packet_bin += bin_str
ver_value, end_ind, end_value = check_packet(packet_bin)
print (f"Value: {end_value}")
