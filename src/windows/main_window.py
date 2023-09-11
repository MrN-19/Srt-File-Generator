from typing import Tuple
import sys
from time import sleep

from PyQt5 import QtWidgets,QtCore,uic

from src.tools import FileManager,WriteFile
from .qt_tools import WidgetAction,TextInputStyle,MessageBox

from src.srt import SrtObject,SrtFile,SRT_OBJECT_DATA

class MainWindow(QtWidgets.QMainWindow):

    UI_FILE_NAME:str = "src/uifiles/mainwindow.ui"
    WINDOW_TITLE:str = "Srt File Generator"
    GEOMTERY:Tuple[int,int] = (708,315)

    def __init__(self,*args,**kwargs) -> None:

        super().__init__(*args,**kwargs)

        uic.loadUi(self.UI_FILE_NAME,self)

        self.setWindowTitle(self.WINDOW_TITLE)

        self.setFixedSize(*self.GEOMTERY)

        self.__load_widgets()
        self.__set_events()

        self.__srt_file_item_number:int = 0


    def __load_widgets(self) -> None:

        self.__txt_text = self.findChild(QtWidgets.QTextEdit,"txtText")
        self.__file_name = self.findChild(QtWidgets.QLineEdit,"txtFileName")

        self.__txt_from_time = self.findChild(QtWidgets.QTimeEdit,"txtFromTime")
        self.__txt_to_time = self.findChild(QtWidgets.QTimeEdit,"txtToTime")

        self.__tbl_data = self.findChild(QtWidgets.QTableWidget,"tblData")
        self.__tbl_data.setRowCount(100)
    
        self.__btn_append = self.findChild(QtWidgets.QPushButton,"btnSet")
        self.__btn_save_file = self.findChild(QtWidgets.QPushButton,"btnSelectFile")
        self.__btn_save_data = self.findChild(QtWidgets.QPushButton,"btnSave")

        self.__load_checkboxes()


    def __load_checkboxes(self) -> None:

        self.__chk_bold = self.findChild(QtWidgets.QCheckBox,"chkBold")
        self.__chk_italic = self.findChild(QtWidgets.QCheckBox,"chkItalic")
        self.__chk_underline = self.findChild(QtWidgets.QCheckBox,"chkUnderline")

    def __set_events(self) -> None:

        self.__btn_append.clicked.connect(self.__btn_append_clicked)
        self.__btn_save_file.clicked.connect(self.__btn_selecte_file_clicked)
        self.__btn_save_data.clicked.connect(self.__btn_save_data_clicked)


    def __btn_save_data_clicked(self) -> None:

        if self.__file_name.text():
        
            file_name:str = self.__file_name.text()

            SrtFile(file_name).save_file(SRT_OBJECT_DATA)

            MessageBox("File Saved","Information",MessageBox.INFORMATION).show()
        
        else:

            MessageBox("Please Select File First","File Not Found",MessageBox.WARNING).show()
        

    def __btn_append_clicked(self) -> None:

        if self.__input_validator():


            

            from_time:str = self.__txt_from_time.text()
            until_time:str = self.__txt_to_time.text()

            text:str = self.__correct_text_format(self.__txt_text.toPlainText())
            
            srt_object = SrtObject(self.__srt_file_item_number + 1,from_time,until_time,text)

            SRT_OBJECT_DATA.append(srt_object)

            self.__tbl_data.setItem(self.__srt_file_item_number,0,QtWidgets.QTableWidgetItem(text))
            self.__tbl_data.setItem(self.__srt_file_item_number,1,QtWidgets.QTableWidgetItem(from_time))
            self.__tbl_data.setItem(self.__srt_file_item_number,2,QtWidgets.QTableWidgetItem(until_time))

            self.__srt_file_item_number += 1

            sleep(0.5)

        



    def __correct_text_format(self,text:str) -> None:

        corrected_text:str = ""

        if self.__chk_bold.isChecked() and (not self.__chk_italic.isChecked() and not self.__chk_underline.isChecked()):

            corrected_text = f"<b> {text} </b>"

        elif self.__chk_italic.isChecked() and (not self.__chk_bold.isChecked() and not self.__chk_underline.isChecked()):

            corrected_text = f"<i> {text} </i>"

        elif self.__chk_underline.isChecked() and (not self.__chk_bold.isChecked() and not self.__chk_italic.isChecked()):

            corrected_text = f"<u> {text} </u>"

        elif self.__chk_bold.isChecked() and self.__chk_italic.isChecked() and not self.__chk_underline.isChecked():

            corrected_text = f"<b> <i> {text} </i> </b>"

        elif self.__chk_bold.isChecked() and self.__chk_underline.isChecked() and not self.__chk_italic.isChecked():

            corrected_text = f"<u> <b> {text} </b> </u>"

        elif self.__chk_italic.isChecked() and self.__chk_underline.isChecked() and not self.__chk_bold.isChecked():

            corrected_text = f"<u> <i> {text} </i> </u>"

        elif self.__chk_bold.isChecked() and self.__chk_italic.isChecked() and self.__chk_underline.isChecked():
            
            corrected_text = f"<u> <b> <i> {text} </i> </b> </u>"
        else:
            corrected_text = text

        return corrected_text



    def __btn_selecte_file_clicked(self) -> None:

        self.__open_file_dialog()

    def __open_file_dialog(self) -> None:

        file_name,file_type = QtWidgets.QFileDialog.getSaveFileName(self,"Save File","c:\\","(Srt File) *.srt")
        
        write_file = WriteFile(file_name)

        if write_file.get_file_extension() != ".srt":
            MessageBox(
                "Please Enter Valid File Format (*.srt)",
                "File Format Error",
                MessageBox.WARNING,
            ).show()
            self.__file_name.setText("")

        else:
            
            write_file.create_empty_file()
            self.__file_name.setText(file_name)
            

            WidgetAction(self.__btn_append).enable_widget()

    def __input_validator(self) -> bool:
        
        text:str = self.__txt_text.toPlainText()

        if not text:

            TextInputStyle(self.__txt_text).border_danger()

            return False
        return True


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())