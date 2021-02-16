import repoInfo
import filechange
import gitcommands as git
from colors import logcolors
import pyfiglet
import logger

def init():
    info = repoInfo.checkinfoInDir()
    url, branch = info
    logger.checkdata(url , branch)
    if('n' in info):
        info.remove('n')
        git.init()
        git.createReadme()
        git.add(['.'])
        git.commit(['README.md'])
        git.setBranch(branch)
        git.setremote(url)
        git.push(url, branch)
        print('initial setup done :)')
        filechange.ischanged(url, branch)
    else:
        print(f'{logcolors.BOLD}Retrieving info from git directory{logcolors.ENDC}')
        print(f'{logcolors.CYAN}URL:{logcolors.ENDC} {url} , {logcolors.CYAN}Branch:{logcolors.ENDC} {branch}')
        filechange.ischanged(info[0], info[1])


if __name__ == '__main__':
    f = pyfiglet.figlet_format('G - AUTO', font='5lineoblique')
    print(f"{logcolors.BOLD}{f}{logcolors.ENDC}")
    init()
