import os

cwd = os.getcwd()
ignorepath = os.path.join(cwd , '.gitignore')

def getIgnoreFiles():
    ignorefiles = []
    with open(ignorepath) as ignore:
        files = ignore.readlines()
        for file in files:
            file = file.split('\n')[0]
            ignorefiles.append(file)
    return ignorefiles
