import os
import json
import hashlib

import colorama
import termcolor



class Container:

    def __init__(self, filename : str, createNew : bool = False) -> None :
        """Init function

        Args:
            filename (str): the file's name
            createNew (bool, optional): Parameter to know if we can overwrite an existing file. Defaults to False.
        """

        if createNew:
            with open(filename, 'w') as f:
                f.write("")

        self.__filename = filename
        self.__absolutePath = os.path.abspath(self.__filename)


    def write(self, text : str) -> None :
        """Method to write text in a file, it will overwrite the file. For not overwriting the file, use the 'append' method

        Args:
            text (str): the text to write in the file
        """
        
        if not text:
            return

        with open(self.__filename, 'w') as f:
            f.write(text)


    def append(self, text : str) -> None :
        """Method to write text in a file, it will not overwrite it, just append the text in the end of the file

        Args:
            text (str): the text to write in the file
        """

        if not text:
            return

        with open(self.__filename, 'a') as f:
            f.write(text)


    def read(self, encoding : str = 'utf-8') -> str :
        """Method to read the content of the file

        Args:
            encoding (str, optional): the encoding you want to read the file with. Defaults to 'utf-8'.

        Returns:
            str: the file's content
        """
        
        with open(self.__filename, 'r') as f:
            fileContent = f.read()

        return fileContent


    def binaryRead(self) -> str :
        """Method to read the content of the file, in binary

        Returns:
            str: the file's content, in binary
        """
        
        with open(self.__filename, 'rb') as f:
            binaryContent = f.read()
            
        return binaryContent


    def getLines(self, encoding : str = 'utf-8', delimitor : str = '\n') -> list[str] :
        """Method to get files lines

        Args:
            encoding (str, optional): the encoding you want to read the file with. Defaults to 'utf-8'.
            delimitor (str, optional): the delimitor between the lines. Defaults to '\\n'

        Returns:
            list[str]: a list containing the file's lines
        """
        
        return self.read(encoding=encoding).split(delimitor)


    def xorCrypt(self, password : str, outputFile : str) -> None :
        if outputFile == self.__filename:
            raise FileExistsError("You can't replace your actual file, for the moment...")

        hashedPasswd = hashlib.sha256(password.encode('utf-8')).digest()
        
        with open(self.__filename, 'rb') as f:
            with open(outputFile, 'wb') as f2:
                i = 0

                while f.peek():
                    c = ord(f.read(1))
                    j = i % len(hashedPasswd)
                    b = bytes([c^hashedPasswd[j]])
                    f2.write(b)

                    i += 1


    def exists(self) -> bool :
        try:
            with open(self.__filename, 'rb') as f:
                fileExists = True
        except FileNotFoundError:
            fileExists = False
        finally:
            return fileExists


    def setPassword(self, password : str) -> None :
        self.__password = password


    def isReadable(self) -> bool :
        try:
            with open(self.__filename, 'r') as f:
                json.load(f)
                
                readable = True
        except json.decoder.JSONDecodeError:
            readable = False
        except UnicodeDecodeError:
            readable = False
        finally:
            return readable


    def updateDict(self, newDict : dict) -> None :
        if not self.isReadable():
            raise OSError("I can't read the file, you mabe forgot to decrypt it first")


    def createContainer(self) -> None :
        if self.exists():
            raise FileExistsError(f"container '{self.__filename}' already exists")
        
        with open(self.__filename, 'w') as f:
            f.write("{}")


    def reinitialize(self, forceReinitalize : bool = False) -> None :
        if forceReinitalize:
            try:
                os.remove(self.__filename)
            except FileNotFoundError:
                pass

        with open(self.__filename, 'w', encoding="utf-8") as f:
            f.write("{}\n")



class ColoredString:

    def __init__(self, string: str = "") -> None :
        self.string = string

        self.__colors = {
            "red" : colorama.Fore.RED,
            "lightred" : colorama.Fore.LIGHTRED_EX,

            "green" : colorama.Fore.GREEN,
            "lightgreen" : colorama.Fore.LIGHTGREEN_EX,

            "blue" : colorama.Fore.BLUE,
            "lightblue" : colorama.Fore.LIGHTBLUE_EX,

            "white" : colorama.Fore.WHITE,
            "lightwhite" : colorama.Fore.LIGHTWHITE_EX,

            "black" : colorama.Fore.BLACK,
            "lightblack" : colorama.Fore.LIGHTBLACK_EX,

            "cyan" : colorama.Fore.CYAN,
            "lightcyan" : colorama.Fore.LIGHTCYAN_EX,

            "yellow" : colorama.Fore.YELLOW,
            "lightyellow" : colorama.Fore.LIGHTYELLOW_EX,

            "magenta" : colorama.Fore.MAGENTA,
            "lightmagenta" : colorama.Fore.LIGHTMAGENTA_EX,
        }


    def color(self, color : str, fromwhere : int = 0, toWhere : int = -1, changeDefaultString : bool = False) -> str :
        if not self.colorExists(color):
            raise ValueError(f"Color '{color}' does not exists, to check if a color exits, you can check the method 'colorExits'")

        coloredstr = f"{self.__colors[color]}{self.string}{colorama.Fore.RESET}"

        if changeDefaultString:
            self.string = coloredstr

        return coloredstr


    def colorExists(self, color: str) -> bool :
        return color in self.colorList()


    def colorList(self) -> list[str] :
        return [color for color in self.__colors.keys()]


    def show(self) -> None :
        print(self.string)


