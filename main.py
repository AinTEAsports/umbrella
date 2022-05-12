import os
import sys
import time

import termcolor

from utils import Container, ColoredString



asciiText = """
██╗   ██╗███╗   ███╗██████╗ ██████╗ ███████╗██╗     ██╗      █████╗ 
██║   ██║████╗ ████║██╔══██╗██╔══██╗██╔════╝██║     ██║     ██╔══██╗
██║   ██║██╔████╔██║██████╔╝██████╔╝█████╗  ██║     ██║     ███████║
██║   ██║██║╚██╔╝██║██╔══██╗██╔══██╗██╔══╝  ██║     ██║     ██╔══██║
╚██████╔╝██║ ╚═╝ ██║██████╔╝██║  ██║███████╗███████╗███████╗██║  ██║
 ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
""".center(20)

asciiText = ColoredString(asciiText)
asciiText.color('lightgreen', changeDefaultString=True)

asciiText.show()


container = Container('container.crypt')

if not container.exists():
    print("[+] The container do not exists, creating it...\n")
    container.createContainer()


OPTIONS = """
0- Quit
1- Encrypt/Decrypt container
2- Add passwords
3- Change passwords
4- Delete passwords
5- Show all passwords
6- Delete all passwords
"""


while True:
    print(OPTIONS)
    userChoice = input("Enter your choice : ")


    match userChoice:
        case '0':
            # verifier que le contaihner a bien ete encrypt sinon proposer a l'utlisateur de l'encrypt
            print("\n[+] Cleaning a little bit...\n")
            time.sleep(1.5)
            sys.exit()
        case '1':
            pass
        case '2':
            pass
        case '3':
            pass
        case '4':
            pass
        case '5':
            pass
        case '6':
            container.reinitialize(forceReinitalize=True)
        case _:
            print("\n---| INVALID CHOICE |---")


