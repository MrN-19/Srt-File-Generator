from typing import Iterable

from src.tools import FileManager


SRT_OBJECT_DATA = []

class SrtObject:
    
    def __init__(self,number:int,from_time:str,until_time:str,text:str) -> None:

        self.__number:int = number
        self.__from_time:str = from_time
        self.__until_time:str = until_time
        self.__text:str = text

    @property
    def number(self) -> int:return self.__number

    @property
    def from_time(self) -> str: return self.__from_time

    @property
    def until_time(self) -> str: return self.__until_time

    @property
    def text(self) -> str: return self.__text


    def __str__(self) -> str:

        format:str = f"""
            
        {self.__number}
        {self.__from_time} --> {self.__until_time}
        {self.__text}
        
        """

        return format 


class SrtFile(FileManager):

    def __init__(self,filename:str) -> None:

        super().__init__(filename)


    def save_file(self,data:Iterable[SrtObject]) -> None:

        with open(self._file_name,"w") as srt_file:

            for srt_data in data:

                srt_file.writelines(str(srt_data))
                srt_file.writelines("\n")



    