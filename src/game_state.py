class Peca:
    def __init__(self, tipo, cor, jogador):
        self.tipo = tipo
        self.cor = cor
        self.jogador = jogador
        self.x = None
        self.y = None

    def movimentacao(self, tabuleiro):
        opts = []
        if self.tipo == 'bishop':
            opt1should = True
            opt2should = True
            opt3should = True
            opt4should = True
            for i in range(1, 4):
                opt1 = (self.x + i, self.y + i)
                if opt1should and 0 <= opt1[0] < 4 and 0 <= opt1[1] < 4:
                    tablePeca = tabuleiro[opt1[0]][opt1[1]].peca
                    if tablePeca:
                        opt1should = False
                        if tablePeca.cor != self.cor:
                            opts.append(opt1)
                    else:
                        opts.append(opt1)
                opt2 = (self.x + i, self.y - i)
                if opt2should and 0 <= opt2[0] < 4 and 0 <= opt2[1] < 4:
                    tablePeca = tabuleiro[opt2[0]][opt2[1]].peca
                    if tablePeca:
                        opt2should = False
                        if tablePeca.cor != self.cor:
                            opts.append(opt2)
                    else:
                        opts.append(opt2)
                opt3 = (self.x - i, self.y - i)
                if opt3should and 0 <= opt3[0] < 4 and 0 <= opt3[1] < 4:
                    tablePeca = tabuleiro[opt3[0]][opt3[1]].peca
                    if tablePeca:
                        opt3should = False
                        if tablePeca.cor != self.cor:
                            opts.append(opt3)
                    else:
                        opts.append(opt3)
                opt4 = (self.x - i, self.y + i)
                if opt4should and 0 <= opt4[0] < 4 and 0 <= opt4[1] < 4:
                    tablePeca = tabuleiro[opt4[0]][opt4[1]].peca
                    if tablePeca:
                        opt4should = False
                        if tablePeca.cor != self.cor:
                            opts.append(opt4)
                    else:
                        opts.append(opt4)

        if self.tipo == 'tower':
            opt1should = True
            opt2should = True
            opt3should = True
            opt4should = True
            for i in range(1, 4):
                opt1 = (self.x, self.y + i)
                if opt1should and 0 <= opt1[0] < 4 and 0 <= opt1[1] < 4:
                    tablePeca = tabuleiro[opt1[0]][opt1[1]].peca
                    if tablePeca:
                        opt1should = False
                        if tablePeca.cor != self.cor:
                            opts.append(opt1)
                    else:
                        opts.append(opt1)
                opt2 = (self.x, self.y - i)
                if opt2should and 0 <= opt2[0] < 4 and 0 <= opt2[1] < 4:
                    tablePeca = tabuleiro[opt2[0]][opt2[1]].peca
                    if tablePeca:
                        opt2should = False
                        if tablePeca.cor != self.cor:
                            opts.append(opt2)
                    else:
                        opts.append(opt2)
                opt3 = (self.x + i, self.y)
                if opt3should and 0 <= opt3[0] < 4 and 0 <= opt3[1] < 4:
                    tablePeca = tabuleiro[opt3[0]][opt3[1]].peca
                    if tablePeca:
                        opt3should = False
                        if tablePeca.cor != self.cor:
                            opts.append(opt3)
                    else:
                        opts.append(opt3)
                opt4 = (self.x - i, self.y)
                if opt4should and 0 <= opt4[0] < 4 and 0 <= opt4[1] < 4:
                    tablePeca = tabuleiro[opt4[0]][opt4[1]].peca
                    if tablePeca:
                        opt4should = False
                        if tablePeca.cor != self.cor:
                            opts.append(opt4)
                    else:
                        opts.append(opt4)
        if self.tipo == 'horse':
            paths = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
            for i in paths:
                xt = self.x + i[0]
                yt = self.y + i[1]
                if 0 <= xt < 4 and 0 <= yt < 4:
                    tablePeca = tabuleiro[xt][yt].peca
                    if not tablePeca or tablePeca.cor != self.cor:
                        opts.append((xt, yt))
        if self.tipo == 'pawn':
            if self.cor == 'white':
                yt = self.y + 1
                can = yt < 4
            else:
                yt = self.y - 1
                can = yt >= 0
            if can:
                if self.x - 1 >= 0:
                    leftpeca = tabuleiro[self.x - 1][yt].peca
                    if leftpeca and leftpeca.cor != self.cor:
                        opts.append((self.x - 1, yt))
                centerpeca = tabuleiro[self.x][yt].peca
                if not centerpeca:
                    opts.append((self.x, yt))
                if self.x + 1 < 4:
                    rightpeca = tabuleiro[self.x + 1][yt].peca
                    if rightpeca and rightpeca.cor != self.cor:
                        opts.append((self.x + 1, yt))

        return opts


class PosicaoTabuleiro:
    def __init__(self, peca=None):
        self.peca = peca


class Jogador:
    def __init__(self, name, cor, id):
        self.name = name
        self.cor = cor
        self.id = id
        self.inventarioPecas = [Peca('pawn', cor, id), Peca('tower', cor, id), Peca('horse', cor, id),
                                Peca('bishop', cor, id)]


class State:
    tabuleiro = [
        [PosicaoTabuleiro(), PosicaoTabuleiro(), PosicaoTabuleiro(), PosicaoTabuleiro()],
        [PosicaoTabuleiro(), PosicaoTabuleiro(), PosicaoTabuleiro(), PosicaoTabuleiro()],
        [PosicaoTabuleiro(), PosicaoTabuleiro(), PosicaoTabuleiro(), PosicaoTabuleiro()],
        [PosicaoTabuleiro(), PosicaoTabuleiro(), PosicaoTabuleiro(), PosicaoTabuleiro()],
    ]

    jogadores = [Jogador('lohan', 'white', 0), Jogador('brenno', 'black', 1)]

    jogadorAtual = 0

    @staticmethod
    def setPlayerName(name, n):
        State.jogadores[n].name = name
