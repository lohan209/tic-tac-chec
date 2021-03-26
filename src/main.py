import sys

from IPython.external.qt_for_kernel import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel, QPushButton, QInputDialog

from src.game_state import State
from src.view import View


def main():
    startapp(None, None)


class GameScreen(QWidget):
    w, h = 800, 600

    def __init__(self):
        super().__init__()
        self.widgets = []
        self.initUI()

    def initUI(self):
        self.resize(self.w, self.h)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(83, 47, 35))
        self.setPalette(p)
        self.center()
        self.show()

    def paintEvent(self, e):

        painter = QPainter(self)
        # painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))

        boardSize = int(self.h * 0.6)

        sizeSquare = boardSize // 4
        centerW = self.w // 2
        centerH = self.h // 2

        # draw tabuleiro
        for i in range(4):
            for u in range(4):
                tab = State.tabuleiro
                positionW = (i - 2) * sizeSquare + centerW
                positionH = (u - 2) * sizeSquare + centerH
                painter.setBrush(
                    QBrush(QColor(115, 65, 29) if (u + i) % 2 == 0 else QColor(232, 193, 119), Qt.SolidPattern))
                painter.drawRect(positionW, positionH, sizeSquare, sizeSquare)
                # draw piece
                posicaoTabuleiro = tab[i][3 - u]
                peca = posicaoTabuleiro.peca
                if peca:
                    label = QLabel(self)
                    label.setAlignment(Qt.AlignCenter)
                    label.setGeometry(QtCore.QRect(positionW, positionH, sizeSquare, sizeSquare))
                    label.setText('')
                    cor = peca.cor
                    piece = peca.tipo
                    label.setPixmap(QtGui.QPixmap("images_tic-tac-chec/{}-{}.png".format(cor, piece)))
                    label.setObjectName(cor + piece)
                    self.widgets.append(label)
                    label.show()

        letterW = 2 * sizeSquare + centerW
        letterH = 2 * sizeSquare + centerH

        painter.setPen(Qt.white)

        # draw coordenas
        letters = ['A', 'B', 'C', 'D']
        numbers = range(4)
        for index in range(4):
            positionW = (index - 2) * sizeSquare + centerW
            positionH = (index - 2) * sizeSquare + centerH

            # do lado
            painter.drawText(letterW + 5, positionH + sizeSquare // 2, str(numbers[-index - 1] + 1))
            # em baixo
            painter.drawText(positionW + sizeSquare // 2, letterH + 17, letters[index])

        for index, player in enumerate(State.jogadores):
            # draw player names
            maxSize = (self.w - boardSize) // 2
            title = QLabel(player.name.title(), self)
            title.setStyleSheet("color: white;")
            font = QtGui.QFont("Times", 18, QtGui.QFont.Bold)
            title.setFont(font)
            w = title.size().width()
            # h = title.size().height()
            if index == 0:
                x = maxSize // 2 - w // 2
            else:
                x = self.w - (maxSize // 2) - w // 4
            title.move(x, self.h // 20)
            title.show()

            # draw pecas
            for indexPiece, peca in enumerate(player.inventarioPecas):
                size = int(maxSize * 0.6)
                pieceSize = int(maxSize * 0.4)
                border = (size - pieceSize) // 2
                label = QLabel(self)
                label.setAlignment(Qt.AlignCenter)
                if index == 0:
                    label.setGeometry(QtCore.QRect(border, (indexPiece) * size + border + 50, pieceSize, pieceSize))
                else:
                    label.setGeometry(
                        QtCore.QRect(self.w - border - pieceSize, (indexPiece) * size + border + 50, pieceSize,
                                     pieceSize))
                label.setText('')
                cor = peca.cor
                piece = peca.tipo
                label.setPixmap(QtGui.QPixmap("images_tic-tac-chec/{}-{}.png".format(cor, piece)))
                label.setObjectName(cor + piece)
                self.widgets.append(label)
                label.show()

        # label jogador que tem que jogar

        currentPlayer = State.jogadores[State.jogadorAtual]
        title = QLabel('Jogador atual: ' + currentPlayer.name.title(), self)
        title.setStyleSheet("color: white;")
        font = QtGui.QFont("Times", 18, QtGui.QFont.Bold)
        title.setFont(font)
        w = title.size().width()
        title.move(self.w // 2 - w, self.h // 20)
        self.widgets.append(title)
        title.show()

        # button jogar

        inicioBtn = QPushButton(self)
        inicioBtn.setGeometry(QtCore.QRect(self.w // 2 - 55, int(self.h * 0.9), 110, 30))
        inicioBtn.setStyleSheet("background-color: rgb(204, 204, 204);")
        inicioBtn.setObjectName("jogar")
        _translate = QtCore.QCoreApplication.translate
        inicioBtn.setText('Jogar')
        inicioBtn.clicked.connect(self.choosePiece)
        inicioBtn.show()

    def choosePiece(self):

        pecasTabuleiro = []
        for i in State.tabuleiro:
            for posicao in i:
                if posicao.peca and posicao.peca.jogador.cor == State.jogadores[State.jogadorAtual].cor:
                    pecasTabuleiro.append(posicao.peca)

        mao = len(State.jogadores[State.jogadorAtual].inventarioPecas) != 0
        tabuleiro = len(pecasTabuleiro) != 0
        onde = View.askmaocampo(self, mao=mao, tabuleiro=tabuleiro)
        if onde == 2:
            return
        elif onde == 1 or (not mao and onde == 0):
            index, peca = View.askPieceBoard(self, pecasTabuleiro)
            if peca:
                possibles = self.getPossibleMoviments(peca, State.tabuleiro)
                coordenada = View.askWhereBoard(self, possibles)
                if coordenada:
                    self.movePieceOnBoard(peca, coordenada[0], coordenada[1])
        else:
            pecas = State.jogadores[State.jogadorAtual].inventarioPecas
            indexPieceHand, peca = View.askPieceHand(self, self, pecas)
            if peca:
                coordenadas = self.getFreeCoordenadas(State.tabuleiro)
                coordenada = View.askWhere(self, coordenadas)
                if coordenada:
                    self.putpiece(State.jogadorAtual, indexPieceHand, coordenada[0], coordenada[1])

    def movePieceOnBoard(self, piece, x, y):
        pecaTabuleiro = State.tabuleiro[x][y].peca
        if pecaTabuleiro:
            pecaTabuleiro.x = None
            pecaTabuleiro.y = None
            State.jogadores[pecaTabuleiro.jogador.id].inventarioPecas.append(pecaTabuleiro)

        State.tabuleiro[x][y].peca = piece
        State.tabuleiro[piece.x][piece.y].peca = None
        piece.x = x
        piece.y = y
        State.jogadorAtual = abs(State.jogadorAtual - 1)

        self.clear()

    def putpiece(self, indexPlayer, indexPiece, indexX, indexY):
        player = State.jogadores[indexPlayer]
        if len(player.inventarioPecas) > 0:
            peca = player.inventarioPecas.pop(indexPiece)
            peca.x = indexX
            peca.y = indexY
            peca.jogador = State.jogadores[State.jogadorAtual]
            State.tabuleiro[indexX][indexY].peca = peca
            State.jogadorAtual = abs(State.jogadorAtual - 1)
            self.clear()

    def getPossibleMoviments(self, peca, tabuleiro):
        # TODO
        possibles = []
        for i in range(4):
            for u in range(4):
                if not (i == peca.x and u == peca.y):
                    possibles.append((i, u))
        return possibles

    def clear(self):
        for i in self.widgets:
            i.deleteLater()
        self.widgets = []

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def getFreeCoordenadas(self, tabuleiro):
        coordenadas = []
        for i in range(4):
            for u in range(4):
                if not tabuleiro[i][u].peca:
                    coordenadas.append((i, u))
        return coordenadas


def startapp(tabuleiro, jogadores):
    app = QApplication(sys.argv)
    game = GameScreen()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
