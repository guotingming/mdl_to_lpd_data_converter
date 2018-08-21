# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from Ui_converter import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
#from test import *
#from Gamma_converter import *
#from mdf_to_lpd import converter_data
from mdf_to_lpd import *
class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        Conversion_results='转换失败，未选择mdf文件'
        filename=QFileDialog.getOpenFileName(self,'open file','/home/jm/')
        filename=filename[0]
        print(filename)
        self.lineEdit.setText(filename)
        self.checkBox.setChecked(True)
        self.checkBox.setText('Checked')
        if filename[-3:]=='mdf':
            savefilename_dir=QFileDialog.getExistingDirectory(self, '选择文件夹', 'C:/')
            self.lineEdit_2.setText(savefilename_dir)
            self.checkBox_2.setChecked(True)
            self.checkBox_2.setText('Checked')
            errors=['1']
            
            errors=converter_data(filename, savefilename_dir)
             

            
            if errors==[]:
               # self.textEdit.setPlainText('转换成功')
                Conversion_results = '转换成功'
            else:
                out=''
                for i in errors:
                    out=out+i+'\n'
                #self.textEdit.setPlainText(errors[0])
                print('---------')
                print(errors)
                Conversion_results =errors[0]


        else:
            #self.textEdit.setPlainText('转换失败，选择的文件不是mdf格式')
            Conversion_results = '转换失败，选择的文件不是mdf格式'
        reply = QMessageBox.information(self, '转换结果', Conversion_results, QMessageBox.Ok)
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec_())
