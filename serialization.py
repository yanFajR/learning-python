try:
    import cPickle as pickle
except:
    import pickle

import json

def serialize(obj, file, type):
    if type == 'pickle':
        f = open(file, 'wb')
        pickle.dump(obj, f)
        f.close()
    elif type == 'json':
        f = open(file, 'wt')
        json.dump(obj, f)
        f.close()

def deserialize(file, type):
    if type == 'pickle':
        f = open(file, 'rb')
        hasil = pickle.load(f)
        f.close()
        return hasil
    elif type == 'json':
        f = open(file, 'rt')
        hasil = json.load(f)
        f.close()
        return hasil

if __name__ == "__main__":
    d1 = {'a':'x', 'b':'y', 'c':'x', 30: (2,3, 'a')}
    serialize(d1, 'a.dat', 'pickle')
    myDict = deserialize('a.dat', 'pickle')
    print(f'pickle: {myDict}')
    print('#' * 20)
    serialize(d1, 'a.json', 'json')
    x = deserialize('a.json', 'json')
    print(f'json: {x}')