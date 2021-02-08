from colors import logcolors
import difflib


def getMaxSpaces(file):
    max = float('-inf')
    for ele in file:
        ele = ele.strip()
        if(len(ele) > max):
            max = len(ele)
    return max


def calcDiff(firstFile, secondFile):
    diff = difflib.ndiff(firstFile, secondFile)
    deltainit = ''.join(x[2:] for x in diff if x.startswith('+ '))
    deltainit = deltainit.split('\n')
    maxspacesinit = getMaxSpaces(deltainit)
    print(f'{logcolors.BOLD}CHANGED LINES ARE{logcolors.ENDC}\n',
          f'{logcolors.BOLD}-{logcolors.ENDC}' * maxspacesinit)
    for ele in deltainit:
        print(f'{logcolors.SUCCESS}{str(ele.strip())}{logcolors.ENDC}',
              ' ' * (maxspacesinit - len(ele.strip())), '+')
    print('', f'{logcolors.BOLD}-{logcolors.ENDC}' * maxspacesinit)
    return deltainit
