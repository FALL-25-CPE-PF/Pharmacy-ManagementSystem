import os

def load_file(file):
    if not os.path.exists(file):
        return []
    f = open(file, "r")
    data = f.read().splitlines()
    f.close()
    return data

def save_file(file, data):
    f = open(file, "w")
    for line in data:
        f.write(line + "\n")
    f.close()
