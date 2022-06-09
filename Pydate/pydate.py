from .Exceptions import *
import os
import requests
import json
from urllib.request import urlopen

class PyDate:
    def __init__(self,path:str,version_raw_link="",isScript=False) -> None:
        """
        :param `path`: Location of local version file
        :param `version_raw_link`: Here is the `raw link` of the latest version number on github.
        If you want to update the script instead of the version numbers, leave this parameter blank.
        """
        self.__path = path
        self.__version_raw_link = version_raw_link
        self.__version = ""
        self.__isScript = isScript
        self.__read = None

    def createVersionFile(self,version:float) -> bool:
        """ 
        If the version file does not exist, it will create it.
        The resulting file is a `json` file.
        
        Returns `False` if the version file exists.
        Returns `True` if the version file does not exist.
        :param version: `float` accepts a value.
        """
        if type(version) is not float:
            raise TypeError("Float value is required!")

        if not os.path.isdir(self.__path):
            raise PathIsEmpty()

        if os.path.exists(f"{self.__path}\\version.json"):
            return False
        else:
            with open(f"{self.__path}\\version.json","w") as f:
                json.dump({'version':f"{version}"},f)
            return True
    
    @property
    def get_version(self) -> dict:
        " Returns version file written on github"
        r = requests.get(self.__version_raw_link)
        self.__version = r.content.decode()
        self.__read = json.loads(self.__version)
        return self.__read
    
    @property
    def isUpdate(self) -> bool:
        " Returns `True` if Current, `False` if Not Current "
        if os.path.exists(f"{self.__path}\\version.json"):
            with open(f"{self.__path}\\version.json","rb") as g:
                data = json.load(g)["version"]
                if float(data) < float(self.get_version["version"]):
                    return False

                elif float(data) == float(self.get_version["version"]):
                    return True
                
                else:
                    raise LogicError()
        else:
            raise VersionFileNotFound("Create version.json first!")
    
    def downloadLink(self,url:str) -> None:
        """
            The argument given to the PyDate class is used as the path.
            Creates a folder named "Installed"

            :param url: Downloadlink of current program/file/exe available on Github.     
        """
        if self.downloaded_name.count(".") > 1:
            raise TypeError("There is no such extension")
        else:
            if not os.path.exists(f"{os.getcwd()}\\Installed"):
                os.mkdir(f"{self.__path}\\Installed")
                resp = requests.get(url,allow_redirects=True)
                with open(f"{self.__path}\\Installed\\{self.downloaded_name}","wb") as file:
                    file.write(resp.content)
    
    def scriptUpdate(self,script_raw_link:str,myscript:str) -> bool:
        """Scripts update. Compares your main script with the current script you keep on githu
        If your main script is not the same as the one you keep up to date on github, it will update it.
        
            :param `script_raw_link`: eg:'https://raw.githubusercontent.com/.../../main/myScript.py'\n
            :param `myscript`: the name of my main script eg `msyscript`

        The method returns a bool value.
        If True, it is up to date. If False, it is not up-to-date.
        If false, change your script and write your script on github so that
        your relevant main script will be updated. 
        """
        if self.__isScript:
            if os.path.exists(f"{self.__path}\\{myscript}.py"):
                response = urlopen(url=script_raw_link)
                with open(f"{self.__path}\\{myscript}.py","r") as f:
                    __data1 = [i for i in f]
                    __data2 = [j.decode("utf-8") for j in response]
                if __data1 == __data2:
                    return True
                else:
                    with open(f"{self.__path}\\{myscript}.py","w",encoding="utf-8") as  f:
                        f.write("".join(j for j in __data2).replace("\n",""))
                    return False
            else:
                raise FileNotFoundError("Relevant 'py' file not found or missing")
        else:
            raise LogicError("Please give the True Argument to the isUpdate parameter first")
        

    @property
    def downloaded_name(self):
        "Value by adding an extension to the end of the name"
        return self.__name

    @downloaded_name.setter
    def downloaded_name(self,name:str) -> None:
        self.__name = name
        return self.__name

    @property
    def readLocalVersion(self) -> dict:
        "Returns the version of the locally created version file"
        
        with open(f"{self.__path}\\version.json","rb") as g:
            data = json.load(g)
        return data

    def saveNewVersion(self,open_=True):
        """
        Upgrades the version value written in the locally maintained version. json file to the version on github.
            :param open_:
                        Default `True`. If open_ parameter is `True`: Opens the downloaded file in the `Installed` folder and upgrades the `version.json` version.
                        
                        if open_ parameter is `False`: only upgrades the version of the script at the specified location
        """
        if open_:
            __file = f"{self.__path}\\Installed\\{self.downloaded_name}"
            if not os.path.exists(f"{self.__path}\\Installed"):
                os.mkdir(f"{self.__path}\\Installed")
            else:
                with open(f"{self.__path}\\version.json","w") as g:
                    json.dump({"version":self.get_version["version"]},g)
                os.startfile(__file)
        else:
            with open(f"{self.__path}\\version.json","w") as g:
                json.dump({"version":self.get_version["version"]},g)
