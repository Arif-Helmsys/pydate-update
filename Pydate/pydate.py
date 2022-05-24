from .Exceptions import *
import os
import requests
import json

class PyDate:
    def __init__(self,path:str,rawlink:str) -> None:
        """
        :param `path`: lokal versiyon dosyasının konumu
        :param `rawlink`: Githubdaki en güncel versiyon numarasının raw linkidir
        """
        self.__path = path
        self.__rawlink = rawlink
        self.__version = ""
        self.__read = None

    def CreateVersionFile(self) -> bool:
        """ 
        Versiyon dosyası yoksa oluşturur.
        Oluşan dosya json dosyasıdır.
        
        Versiyon dosyası varsa `False` döndürür.
        Versiyon dosyası yoksa `True` döndürür.
        """
        if not os.path.isdir(self.__path):
            raise PathIsEmpty()

        if not os.path.exists(f"{self.__path}\\version.json"):
            with open(f"{self.__path}\\version.json","w") as f:
                json.dump({'version':"0.0"},f)
            return True
        else:
            return False
    
    @property
    def get_version(self):
        " Githubda yazılan versiyon dosyasını döndürür (txt olması önerilir) "
        r = requests.get(self.__rawlink)
        self.__version = r.content.decode()
        self.__read = json.loads(self.__version)
        return self.__read
    
    def isUpdate(self) -> bool:
        " Güncelse `True`, Güncel değilse `False` döndürür "
        with open(f"{self.__path}\\version.json","rb") as g:
            data = json.load(g)["version"]
            print(data)
            if data < self.get_version["version"]:
                return False

            elif data > self.get_version["version"]:
                raise LogicError()
            
            elif data == self.get_version["version"]:
                return True