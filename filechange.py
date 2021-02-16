import os
from os import listdir
from os.path import isfile, join
import gitcommands as git
import diffcalc
import ignore
import logger
import time
from colors import logcolors
mypath = os.getcwd()
nestfiles = []

ignoredirs = ignore.getIgnoreFiles()
print(ignoredirs)
# gets the list of all nested files


def getNestedFiles(rootDir):
    for path, subdirs, files in os.walk(rootDir):
        if(all(ele not in path for ele in ignoredirs)):
            for name in files:
                nestfiles.append(join(path, name))
    return nestfiles


onlyfiles = getNestedFiles(mypath)

# Reads and appends the contents of each file


def read_file():
    filecontent = []
    for file in onlyfiles:
        with open(onlyfiles[onlyfiles.index(file)], "r") as f:
            filecontent.append(f.readlines())
    return filecontent


def ischanged(url, branch,*args,**kwargs):
    changedfile = []
    diffarr = []
    initbuffer = kwargs.get('initbuffer' , -1)
    if(initbuffer != -1):
        for obj in initbuffer:
            file = obj['path']
            diff = obj['changes']
            diffarr.append(diff)
            changedfile.append(file)
        git.add(changedfile)
            # Performing Git Commit
        if(git.commit(changedfile,diffarr) == False):
            print(f'{logcolors.ERROR}Reverting Push{logcolors.ENDC}')
            logger.updatedata(changedfile, diffarr)
        else:
            print(f'{logcolors.SUCCESS}Updating Logs{logcolors.ENDC}')
            logger.updatedata(changedfile, diffarr)
            if(len(changedfile) == 0):
                git.push(url, branch)
    print('Listening for changes....')
    initial = list(read_file())
    while True:
        current = list(read_file())
        changeditem = []
        previtem = []
        if(current != initial):
            # Calculating Previous Version of File
            for ele in initial:
                if ele not in current:
                    for item in ele:
                        previtem.append(item)
            # Calculating New Version of File
            for ele in current:
                if ele not in initial:
                    changeditem.append(ele)
            # calculating changed file's name
            for i in range(0, len(changeditem)):
                print('loop :-', i)
                changedfile.append(onlyfiles[current.index(changeditem[i])])
            print(f"Changed file is {logcolors.BOLD}{changedfile}{logcolors.ENDC}\n")
            # Calculating Diff for previous and changed version of file
            diff = diffcalc.calcDiff(previtem, changeditem[0])
            diffarr.append(diff)
            for file in changedfile:
                logger.writedata(path=file, diff=diff)
            # Performing Git Commands For Changed File
            # Performing Git Add
            git.add(changedfile)
            # Performing Git Commit
            if(git.commit(changedfile,diffarr) == False):
                print(f'{logcolors.ERROR}Reverting Push{logcolors.ENDC}')
            else:
                print(f'{logcolors.SUCCESS}Updating Logs{logcolors.ENDC}')
                logger.updatedata(changedfile, diffarr)
                if(len(changedfile) == 0):
                    git.push(url, branch)


            initial = current
            # time.sleep(5)
