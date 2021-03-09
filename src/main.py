# -*- encoding: utf-8 -*-
'''
Created on May 14, 2020

@author: lohanrodrigues
'''
import sys
import view
from PyQt5 import QtWidgets, QtCore
from PyQt5.uic.Compiler.qtproxies import QtGui

class Main(QtWidgets.QWidget, view.Ui_Form):
    
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.pedra = "vazio";
        self.posicao = "vazio";
        self.startBtn.clicked.connect(self.run)
                        
    def checkPosition(self, position):
        table = {
            self.frame_AA: (145, 55),
            self.frame_AB: (165, 55),
            self.frame_AC: (185, 55),
            self.frame_AD: (205, 55),
            self.frame_BA: (145, 55),
            self.frame_BB: (145, 55),
            self.frame_BC: (145, 55),
            self.frame_BD: (145, 55),
            self.frame_CA: (145, 55),
            self.frame_CB: (145, 55),
            self.frame_CC: (145, 55),
            self.frame_CD: (145, 55),
            self.frame_DA: (145, 55),
            self.frame_DB: (145, 55),
            self.frame_DC: (145, 55),
            self.frame_DD: (145, 55)
            }
        
        return table[position]

    def run(self):  
        try:
            status = self.startBtn.text()
            if status == "Iniciar o jogo":
                _translate = QtCore.QCoreApplication.translate
                self.startBtn.setText(_translate(status, "Desistir do jogo"))
            else:
                _translate = QtCore.QCoreApplication.translate
                self.startBtn.setText(_translate(status, "Iniciar o jogo"))
                
                
        except Exception as e:
            print(e)
            

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    app.exec_()
   
if __name__ == '__main__':
    main()

