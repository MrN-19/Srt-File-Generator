from PyQt5 import QtWidgets


class QtStyle:

    def __init__(self,widget:QtWidgets.QWidget) -> None:
        self._widget:QtWidgets.QWidget = widget

    @property
    def widget(self) -> QtWidgets.QWidget:
        return self._widget
    
    

class TextInputStyle(QtStyle):

    def __init__(self, widget:QtWidgets.QWidget) -> None:
        super().__init__(widget)

    
    def custom_style(self,style:str) -> None:
        
        self._widget.setStyle(style)

    def border_danger(self) -> None:
        
        style_text:str = "border: 1px solid red"

        self._widget.setStyleSheet(style_text)


class WidgetAction:

    def __init__(self,widget:QtWidgets.QWidget) -> None:

        self.__widget = widget

    def disable_widget(self) -> None:

        self.__widget.setEnabled(False)

    def enable_widget(self) -> None:

        self.__widget.setEnabled(True)

class MessageBox:

    INFORMATION = QtWidgets.QMessageBox.Information
    ERROR = QtWidgets.QMessageBox.Critical
    WARNING = QtWidgets.QMessageBox.Warning


    def __init__(self,text:str,title:str,icon,**kwargs):

        self.__text = text
        self.__title:str = title
        self.__icon = icon
        self.__kwargs = kwargs

    def show(self) -> None:

        message = QtWidgets.QMessageBox()
        message.setIcon(self.__icon)
        message.setWindowTitle(self.__title)
        message.setText(self.__text)
        message.exec_()