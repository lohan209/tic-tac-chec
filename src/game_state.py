tabuleiro = [
            [PosicaoTabuleiro(), PosicaoTabuleiro(), PosicaoTabuleiro(), PosicaoTabuleiro()],
            [PosicaoTabuleiro(), PosicaoTabuleiro(), PosicaoTabuleiro(), PosicaoTabuleiro()],
            [PosicaoTabuleiro(), PosicaoTabuleiro(), PosicaoTabuleiro(), PosicaoTabuleiro()],
            [PosicaoTabuleiro(), PosicaoTabuleiro(), PosicaoTabuleiro(), PosicaoTabuleiro()],
        ]

jogadores = [ Jogador('lohan', 'preto'), Jogador('brenno', 'branco') ]

class PosicaoTabuleiro: 
    def __init__(self):
        self.peca = None     
        
class Peca:
    def __init__(self, tipo, cor):
         self.tipo = tipo
         self.cor = cor
         
class Jogador:
     def __init__(self, name, cor):
         self.name = name
         self.cor = cor
         self.inventarioPecas = [Peca('Peao', cor),Peca('Torre', cor),Peca('Cavalo', cor), Peca('Bispo', cor)]