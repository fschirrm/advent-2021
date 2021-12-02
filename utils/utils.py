def read_file(f):
    with open(f) as f: 
        content = [line.strip().split(" ") for line in f.readlines()]
    return content