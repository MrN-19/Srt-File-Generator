import os

class FileManager:

    def __init__(self,filename:str) -> None:
        self._file_name = filename

    def check_file_exists(self) -> bool:

        return os.path.isfile(self._file_name)
    
    def get_file_extension(self) -> str:
        return os.path.splitext(self._file_name)[1]
    
    def get_file_path(self) -> str:

        return os.path.splitext(self._file_name)[0]
    

class WriteFile(FileManager):

    def __init__(self,filename:str) -> None:

        super().__init__(filename)

    def create_empty_file(self) -> None:

        with open(self._file_name,"w") as file:
            ...
        

