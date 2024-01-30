# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
# Crie uma instância da classe carro.
# Faça o carro "andar" utilizando os métodos da sua classe.
# Faça o carro "parar" utilizando os métodos da sua classe.

class Carro:
    def __init__(self):
        self.ligado = False
        self.cor = 'branco'
        self.modelo = 'corsa'
        self.velocidade = 0
        self.velocidade_min = 0
        self.velocidade_max = 120

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def acelerar(self):
        if not self.ligado:
            return
        
        if self.velocidade < self.velocidade_max:
            self.velocidade += 10

    def desacelerar(self):
        if not self.ligado:
            return
        
        if self.velocidade > self.velocidade_min:
            self.velocidade -= 10

    def parar(self):
        if not self.ligado:
            return
        
        if self.velocidade <= self.velocidade_min:
            return
        
        while self.velocidade > self.velocidade_min:
            self.velocidade -= 10

carro = Carro()

carro.ligar()
print('carro está ligado? {}'.format(carro.ligado))

for _ in range(4):
    carro.acelerar()
print('velocidade do carro: {}'.format(carro.velocidade))

carro.desacelerar()
print('velocidade do carro: {}'.format(carro.velocidade))

carro.parar()
print('velocidade do carro: {}'.format(carro.velocidade))