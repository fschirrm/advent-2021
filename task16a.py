
def check_packet(packet_bin):
    end_ind = 0
    ver_value = 0
    v = int(packet_bin[0:3],2)
    t = int(packet_bin[3:6],2)
    ver_value += v
    if t == 4:
        num_point = 6
        while packet_bin[num_point:num_point+1] == "1": num_point += 5 
        end_ind = num_point + 4
    else:
        if packet_bin[6:7] == '0':
            num_bits = int(packet_bin[7:22],2)
            end_ind = 0
            while end_ind < num_bits:
                v, e = check_packet(packet_bin[22+end_ind:22+num_bits])
                end_ind = end_ind + e + 1
                ver_value += v
            end_ind = 21 + num_bits
        else:
            num_packets = int(packet_bin[7:18],2)
            start = 18
            for i in range(num_packets):
                v, end_ind = check_packet(packet_bin[start:])
                ver_value += v
                start = start + end_ind + 1
            end_ind = start - 1
    return ver_value, end_ind

with open("files/task16.txt") as f: packet_hex = f.readline().strip()
packet_bin = ""
for i in range(len(packet_hex)):
    bin_str = "{0:04b}".format(int(packet_hex[i], 16))
    packet_bin += bin_str
ver_value, end_ind = check_packet(packet_bin)
print (f"Version-Summe: {ver_value}")
