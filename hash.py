hash_table = [0 for i in range(8)]

def hash_func(data):
    return hash(data) % 8

def set_data(data,value):
    key = hash_func(data)
    hash_table[key] = value

def get_data(data):
    key = hash_func(data)
    return hash_table[key]
  
  
#Chaining 기법
def hash_func(key):
    return key % 8

def set_data(data,value):
    hash_idx = hash(data)
    hash_key = hash_func(hash_idx)
    if hash_table[hash_key] != 0:
        for i in range(len(hash_table[hash_key])):
            if hash_table[hash_key][i][0] == hash_idx:
                hash_table[hash_key][i][1] = value
                return True
        hash_table[hash_key].append([hash_idx,value])
        return True
    else:
        hash_table[hash_key] = [[hash_idx,value]]
        return True

def get_data(data):
    hash_idx = hash(data)
    hash_key = hash_func(hash_idx)
    if hash_table[hash_key]:
        for value in hash_table[hash_key]:
            if value[0] == hash_idx:
                print(value[1])
                return value[1]
        print("None")
        return None
    else:
        print("None")
        return None
