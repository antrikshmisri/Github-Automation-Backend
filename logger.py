import json
import os

jsonpath = os.path.join(os.getcwd(), 'auto-scripts\\tmp.json')
buffer = []


def writedata(*args, **kwargs):
    data = {}
    global buffer
    updatedbuffer = kwargs.get('buffer', -1)
    path = kwargs.get('path', None)
    diff = kwargs.get('diff', None)
    if(updatedbuffer != -1):
        buffer = updatedbuffer
        with open(jsonpath, 'w') as file:
            json.dump([obj for obj in buffer], file, indent=4)
    elif(path and diff):
        data['path'] = path
        data['changes'] = diff
        buffer.append(data)
        with open(jsonpath, 'w') as file:
            json.dump([obj for obj in buffer], file, indent=4)


def readdata(filename, diff):
    if(os.path.getsize(jsonpath) > 0):
        with open(jsonpath, 'r') as file:
            readdata = json.load(file)
        if(len(readdata) == 0):
            print('No changed file left')
        else:
            print('Found some changed files')
            for file in filename:
                print('Removing ' + str(file) + ' from json file')
                for obj in readdata:
                    if obj['path'] == file and obj['changes'] == diff:
                        readdata.remove(obj)
                filename.remove(file)
            writedata(buffer=readdata)

    else:
        print('No data to read')
