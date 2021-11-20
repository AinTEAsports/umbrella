# ENGLISH :
#
# Umbrella password container, made by AinTea#0519, if you don't credit me or if you share this code without this
# credit then you're evil and be evil is not cool
#
# This code principally create a file with your hashed password (to verify if you entered the good password) 
# and it creates a container crypted (with XOR crypt algorythm) with your password stored as JSON data
#
# It's ot 100% secured you must know it I'm a beginner...
# If you want to secure it you can change the hash method or just have a more secured password because you "easily" can crack
# your password by brute force or dictionnary attack you can try ON YOUR CONTAINER btw because on others it's purely illegal
# If your passwords has been hacked I'm not responsible I warned you
#
# ##################### ##################### ############# ################ ############################## #################
#
# FRANCAIS :
#
# Conteneur de mot de passe a peu près sécurisé, fait par AinTea#0519, si vous ne me creditez pas ou que vous partagez ce
# code sans ce crédit bah vous serez méchant et c'est pas gentil d'etre mechant ("Par le pouvoir de la conjonctivite"
# pour les connaisseurs)
#
# En gros ce code va créer un fichier mot de passe hashé pour verifier si vous avez entré le bon mot de passe
# et ca créé un fichier conteneur qui va stocker vos mots de passe sous format JSON mais crypté par un chiffrage XOR
#
# C'est clairement pas sécurisé a 100% hein j'suis un débutant là dedans donc je préfère prévenir
# Si vous voulez plus le sécuriser vous pouvez déjà renforcer la méthode de hashage en rajoutant des parties de hash par
# ci par là et/ou avoir un mot de passe plus fort parce que pour le cracker il "suffit" d'utiliser une methode de force brute
# vous pouvez essayer SUR LE VOTRE évidemment sinon c'est juste illegal
# Si vos mots de passe sont hackés je ne suis en aucun responsable je vous ai prévenu au dessus



import os
import sys
import json
import time
import hashlib

from getpass import getpass


# ASCII art cause we're h@ck3rZ
asciiProjectName = """
  _    _           _              _ _       
 | |  | |         | |            | | |      
 | |  | |_ __ ___ | |__  _ __ ___| | | __ _ 
 | |  | | '_ ` _ \| '_ \| '__/ _ \ | |/ _` |
 | |__| | | | | | | |_) | | |  __/ | | (_| |
  \____/|_| |_| |_|_.__/|_|  \___|_|_|\__,_|
"""


# We define absolute path to create/read the container where will be stored all passwords
absolutePath = f"{os.path.dirname(os.path.abspath(__file__))}"

# We define names of the files which will be used for the program
CRYPTED_FILE_NAME = "container.crypt"
DECRYPTED_FILE_NAME = "container.decrypted"
PASSWORD_FOLDER_NAME = "password.crypt"


# A function to verify if the password container is empty
def is_container_empty(password):
    if sys.platform == "win32":
        file = f"{absolutePath}\\{DECRYPTED_FILE_NAME}"
    else:
        file = f"{absolutePath}/{DECRYPTED_FILE_NAME}"
        
    xor_crypt(fichierEntree=path_and_file(), fichierSortie=file, keyName=password, delete="n")
    with open(file, "r") as maVariable:
        read = maVariable.read()
        
    os.remove(file)
    
    if read.startswith("{") and read.endswith("}"):
        return False
    else:
        return True

    

# Function to get the absolute path and the file
def path_and_file():
    if sys.platform == "win32":
        return f"{absolutePath}\\{CRYPTED_FILE_NAME}"
    else:
        return f"{absolutePath}/{CRYPTED_FILE_NAME}"


# The principal function which will crypt the container
def xor_crypt(fichierEntree, fichierSortie, keyName, delete="n"):
    import os
    import sys
    import hashlib

    keys = hashlib.sha256(keyName.encode('utf-8')).digest()

    with open(fichierEntree, "rb") as fFichierEntree:
        with open(fichierSortie, "wb") as fFichierSortie:
            i = 0
            while fFichierEntree.peek():
                entreeRead = ord(fFichierEntree.read(1))
                moduloKey = i % len(keys)
                b = bytes([entreeRead^keys[moduloKey]])
                fFichierSortie.write(b)
                i += 1
    if delete.lower() == "y":
        if sys.platform == "win32":
            command = f"del /F {fichierEntree}"
            os.system(command)
        else:
            os.remove(fichierEntree)


# We define a function which will return if it is the first time we launch this program verifying if the container file exists
def is_first_time():
    try:
        if sys.platform == "win32":
            with open(f"{absolutePath}\\{PASSWORD_FOLDER_NAME}", "r") as maVariable:
                temp = maVariable.read()
        else:
            with open(f"{absolutePath}/{PASSWORD_FOLDER_NAME}", "r") as maVariable:
                temp = maVariable.read()
        return False
    except FileNotFoundError:
        return True


# We define a function to hash a password
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


# We define a function to verify if the entered password and the accurate password are the same
def verif_password(password):
    if sys.platform == "win32":
        filePath = f"{absolutePath}\\{PASSWORD_FOLDER_NAME}"
    else:
        filePath = f"{absolutePath}/{PASSWORD_FOLDER_NAME}"
    with open(filePath, "r", encoding='utf-8') as maVariable:
        return hash_password(password) == maVariable.read()


# We define a function to create a secure password if the user wants to
def psswrd(min_letters="N", capital_letters="N", special_caracters="N", caracter_number=8):
    """ Password generator

    This is a program which will create a secure
    password with the random py lib
    """
    import random

    class MyList(list):
        def add(self, *args):
            for arg in args:
                self.append(arg)

    lst = MyList()

    lst.add('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

    if min_letters.capitalize() == "Y":
        lst.add('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z')

    if capital_letters.capitalize() == "Y":
        lst.add('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

    if special_caracters.capitalize() == "Y":
        lst.add('&', '"', '\'', '(', '-', '_', 'ç', ')', '=', '+', '<', '>', '#', '{', '[',
                '|', '@', ']', '}', '^', '$', '£', '%', '!', ':', '/', ';', '.', ',', '?', '*')

    password_create = ""

    for i in range(0, caracter_number):
        carac_add = str(random.choice(lst))
        password_create = password_create + carac_add

    return password_create


# We define a function to return if the master password is secured
def is_secure_pasword(password):
    # must contain a low letter, a cap letter, a number and a special caracter. Also must contain at least 8 caracters
    lowInPassword = [i for i in list("abcdefghijklmnopqrstuvwxyz") if i in password]
    capInPassword = [i for i in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") if i in password]
    numInPassword = [i for i in list("0123456789") if i in password]
    specialInPassword = [i for i in list("&\"\'(-_ç)=+<>#{[|@]}^$£%!:/;.,?*") if i in password]
    isSecure = bool(lowInPassword) and bool(capInPassword) and bool(numInPassword) and bool(specialInPassword)

    return isSecure


# A function to create the session (principaly create the files)
def create_session():
    print("\n" + "-" * 79)
    print("\n/// CREATE MASTER PASSWORD /// \n")
    print("Your password need to be secure (1 cap, 1 lowercase, 1 number and 1 special carac minimum...)")
    print("YOU MUST REMEMBER THIS PASSWORD (IT WON'T BE STORED ANYWHERE BY THIS PROGRAM) AND YOU WON'T BE ABLE TO MODIFY IT !\n")

    wantsSecurePassword = input("Want you we generate a secure password ? [Y/n] : ").lower()
    
    while wantsSecurePassword not in ['y', 'n']:
        print("\n! Please enter a valid option !\n")
    if wantsSecurePassword == "y":
        passwordLen = input("How much caracters want you your password contains : ")
        
        while True:
            try:
                passwordLen = int(passwordLen)
                break
            except ValueError:
                print("\n! Please enter a valid option !\n")
                passwordLen = input("How much caracters want you your password contains : ")
        
        generatedPassword = psswrd(min_letters="Y", capital_letters="Y", special_caracters="Y", caracter_number=passwordLen)
        print(f"/// PASSWORD GENERATED ///\n\nYour password will be : {generatedPassword}")
    
    masterPassword = getpass("Master Password : ")

    while is_secure_pasword(masterPassword) == False:
        print("Your password need to be secure (1 cap, 1 lowercase, 1 number and 1 special carac minimum...)")
        masterPassword = getpass("Master Password : ")

    if sys.platform == "win32":
        passwordFilePath = f"{absolutePath}\\{PASSWORD_FOLDER_NAME}"
        containingFileDecrypted = f"{absolutePath}\\{DECRYPTED_FILE_NAME}"
        containingFileCrypted = f"{absolutePath}\\{CRYPTED_FILE_NAME}"
    else:
        passwordFilePath = f"{absolutePath}/{PASSWORD_FOLDER_NAME}"
        containingFileDecrypted = f"{absolutePath}/{DECRYPTED_FILE_NAME}"
        containingFileCrypted = f"{absolutePath}/{CRYPTED_FILE_NAME}"
        
    with open(passwordFilePath, "w", encoding='utf-8') as maVariable:
        maVariable.write(hash_password(masterPassword))
    
    # VARIABLE "containingFileDecrypted" REFERENCED BEFORE ASSIGNMENT
    # a corriger evidemment
    with open(containingFileDecrypted, "w", encoding='utf-8') as maVariable:
        maVariable.write("")
        json.dumps("{}", separators=(',', ':'))
    # ici le fichier est juste delete car y'a l'erreur de creer car le fichier
    # existe deja mais ca arrete pas le script puis ca delete le fichier
    xor_crypt(containingFileDecrypted, containingFileCrypted, masterPassword, delete="y")
        
    print("\n/// ACCOUNT SUCCESSFULLY CREATED ///")

    return


# Function to get the password from the container
def get_passwords(password):
    if sys.platform == "win32":
        exitFile = f"{absolutePath}\\container_uncrypted.crypt"
    else:
        exitFile = f"{absolutePath}/container_uncrypted.crypt"

    xor_crypt(fichierEntree=path_and_file(), fichierSortie=exitFile, keyName=password, delete="n")
    
    with open("container_uncrypted.crypt", "r") as maVariable:
        passwordsDict = maVariable.read()
        if passwordsDict == "":
            return {}
        containerPassword = json.loads(passwordsDict)
    
    os.remove(exitFile)
    
    return containerPassword


# The connected menu, if the user has logged in successfully
def connected_menu(password):
    emptyContainer = is_container_empty(password=password)
    
    if not emptyContainer:
        allPasswords = get_passwords(password=password)
    else:
        allPasswords = {}
    
    # try:
    #     allPasswords = get_passwords(password=password)
    # except JSONDecodeError:
    #     emptyContainer = True
        
    print("\n---| CONNECTED |---")
    
    print(asciiProjectName)
    
    while True:
        if emptyContainer:
            print("\n/// YOU DON'T HAVE ANY PASSWORDS AND SITE REGISTERED ///\n")
            print("1- Ajouter un site")
            print("2- Déconnexion")
            
            userChoice = input("\nEntrez votre choix : ")
            
            if userChoice == "1":
                newSite = input("Enter the name (not the URL) of the site you want to add : ").lower()
                newSiteUrl = input("Enter the URL of the site you entered : ")
                
                securePasswordProposal = psswrd(min_letters="Y", capital_letters="Y", special_caracters="Y", caracter_number=16)
                print(f"\nA proposal of secure password for this site could be : {securePasswordProposal}\n")
                
                newSitePassword = input(f"Enter your password for the site \"{newSite.title()}\" : ")
                
                allPasswords[newSite] = {"url" : newSiteUrl, "password" : newSitePassword}
                print(f"\nNEW SITE ADDED :\nSite name : {newSite.title()}\nSite URL : {newSiteUrl}\nPassword : {newSitePassword}\n\nTO APPLY CHANGES, YOU MUST DISCONNECT\n")
                
            elif userChoice == "2":
                if sys.platform == "win32":
                    containingFileDecrypted = f"{absolutePath}\\{DECRYPTED_FILE_NAME}"
                    containingFileCrypted = f"{absolutePath}\\{CRYPTED_FILE_NAME}"
                else:
                    containingFileDecrypted = f"{absolutePath}/{DECRYPTED_FILE_NAME}"
                    containingFileCrypted = f"{absolutePath}/{CRYPTED_FILE_NAME}"
                    
                with open(containingFileDecrypted, "w") as maVariable:
                    maVariable.write(json.dumps(allPasswords, separators=(',', ':')))
                
                xor_crypt(containingFileDecrypted, containingFileCrypted, password, delete="y")
                    
                print("\n---| DECONNEXION |---")
                time.sleep(2)
                sys.exit()
            else:
                print("\n/// INVALID OPTION ///\n")
        else:
            print("\n1- Afficher les sites pour lesquels un mot de passe est enregistré")
            print("2- Afficher le mot de passe d'un site")
            print("3- Ajouter un site")
            print("4- Supprimer un site")
            print("5- Modifier un mot de passe")
            print("6- Déconnexion")

            userChoice = input("\nEntrez votre choix : ")

            if userChoice == "1":
                [print(f"{list(allPasswords.keys())[i].title()} : {list(allPasswords.values())[i]}") for i in range(len(allPasswords))]
                    
            elif userChoice == "2":
                site = input("Enter the name of the site you want to know the informations : ").lower()
                    
                if site in allPasswords.keys():
                    siteUrl = allPasswords[site]["url"]
                    sitePassword = allPasswords[site]["password"]
                    print(f"Site URL : {siteUrl}\nSite Password : {sitePassword}\n")
                else:
                    print(f"\nThere are no informations registered for the site {site.title()}\n")
            
            elif userChoice == "3":
                newSite = input("Enter the name (not the URL) of the site you want to add : ").lower()
                newSiteUrl = input("Enter the URL of the site you entered : ")
                
                securePasswordProposal = psswrd(min_letters="Y", capital_letters="Y", special_caracters="Y", caracter_number=16)
                print(f"\nA proposal of secure password for this site could be : {securePasswordProposal}\n")
                
                newSitePassword = input(f"Enter your password for the site \"{newSite.title()}\" : ")

                allPasswords[newSite] = {"url" : newSiteUrl, "password" : newSitePassword}
                print(f"\nNEW SITE ADDED :\nSite name : {newSite.title()}\nSite URL : {newSiteUrl}\nPassword : {newSitePassword}\n\nTO APPLY CHANGES, YOU MUST DISCONNECT\n")
                
            elif userChoice == "4":
                siteToDelete = input("Enter the name of the site you want to delete : ").lower()
                
                if siteToDelete in allPasswords.keys():
                    del allPasswords[siteToDelete]
                    print(f"\nThe site {siteToDelete.title()} and all of these informations has been deleted...")
                else:
                    print(f"There are no informations registered for the site {siteToDelete.title()}")
                    
            elif userChoice == "5":
                siteToModify = input("Enter the site of which you want to modify the password : ").lower()
                try:
                    securePasswordProposal = psswrd(min_letters="Y", capital_letters="Y", special_caracters="Y", caracter_number=16)
                    print(f"\nA proposal of secure password for this site could be : {securePasswordProposal}\n")
                    
                    passwordModify = input("Enter the new password : ")
                    allPasswords[password]["password"] = passwordModify
                    print("\nPASSWORD SUCCESSFULLY CHANGED, TO APPLY CHANGES YOU MUST DISCONNECT")
                except IndexError:
                    print(f"\nThere's no site registered named \"{siteToModify}\"\n")
                
            
            elif userChoice == "6":
                if sys.platform == "win32":
                    containingFileDecrypted = f"{absolutePath}\\{DECRYPTED_FILE_NAME}"
                    containingFileCrypted = f"{absolutePath}\\{CRYPTED_FILE_NAME}"
                else:
                    containingFileDecrypted = f"{absolutePath}/{DECRYPTED_FILE_NAME}"
                    containingFileCrypted = f"{absolutePath}/{CRYPTED_FILE_NAME}"
                    
                with open(containingFileDecrypted, "w") as maVariable:
                    maVariable.write(json.dumps(allPasswords, separators=(',', ':')))
                
                xor_crypt(containingFileDecrypted, containingFileCrypted, password, delete="y")
                    
                print("\n---| DECONNEXION |---")
                time.sleep(2)
                sys.exit()
                
            else:
                print("\n/// INVALID OPTION ///\n")

    return


#########################################################################################################

if __name__ == "__main__":
    
    if is_first_time():
        create_session()

    print("\n---| LOGIN |---\n")
    password = getpass("Enter your master password : ")

    if verif_password(password):
        connected_menu(password=password)
    else:
        print("\n---INVALID PASSWORD---\n\n---| EXIT... |---")
        time.sleep(2)
        sys.exit()
