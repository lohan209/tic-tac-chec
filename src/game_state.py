class Peca:
    def __init__(self, tipo, cor, jogador):
        self.tipo = tipo
        self.cor = cor
        self.jogador = jogador
        self.x = None
        self.y = None


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

    jogadores = [Jogador('lohan', 'black', 0), Jogador('brenno', 'white', 1)]

    jogadorAtual = 0
