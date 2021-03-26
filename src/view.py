from IPython.external.qt_for_kernel import QtGui, QtCore
from PyQt5.QtWidgets import QInputDialog


class View:
    letters = ['A', 'B', 'C', 'D']

    @staticmethod
    def askmaocampo(window, mao=True, tabuleiro=True):
        msgBox = QtGui.QMessageBox()
        msgBox.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        msgBox.setWindowTitle('Jogada')
        msgBox.setText('De onde você quer jogar?')
        if mao:
            msgBox.addButton(QtGui.QPushButton('Mão'), 0)
        if tabuleiro:
            msgBox.addButton(QtGui.QPushButton('Tabuleiro'), 1)
        msgBox.addButton(QtGui.QPushButton('Cancelar'), 2)
        ret = msgBox.exec_()
        return ret

    @staticmethod
    def askPieceBoard(window, pecas):
        mapPieces = list(map(lambda x: str(View.letters[x.x]) + str(x.y + 1), pecas))
        item, ok = QInputDialog.getItem(window, "Jogada",
                                        "Qual peça você quer jogar?",
                                        mapPieces, 0, False)
        if ok:
            index = mapPieces.index(item)
            peca = pecas[index]
            return index, peca
        else:
            return

    @staticmethod
    def askPieceHand(self, window, pecas):
        mapTipo = list(map(lambda x: x.tipo.capitalize(), pecas))
        item, ok = QInputDialog.getItem(window, "Jogada",
                                        "Qual peça você quer jogar?",
                                        mapTipo, 0, False)
        if ok:
            index = mapTipo.index(item)
            peca = pecas[index]
            return index, peca
        else:
            return

    @staticmethod
    def askWhere(window, possibles):

        mapPieces = list(map(lambda x: str(View.letters[x[0]]) + str(x[1] + 1), possibles))
        item, ok = QInputDialog.getItem(window, "Jogada",
                                        "Qual peça você quer jogar?",
                                        mapPieces, 0, False)
        if ok:
            index = mapPieces.index(item)
            coordenada = possibles[index]
            return coordenada
        else:
            return

    @staticmethod
    def askWhereBoard(window, possibles):
        mapPieces = list(map(lambda x: str(View.letters[x[0]]) + str(x[1] + 1), possibles))
        item, ok = QInputDialog.getItem(window, "Jogada",
                                        "Onde você quer jogar?",
                                        mapPieces, 0, False)
        if ok:
            index = mapPieces.index(item)
            coordenada = possibles[index]
            return coordenada
        else:
            return
