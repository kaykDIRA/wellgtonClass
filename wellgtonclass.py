class Transporte:
    def mover(self):
        return "O transporte está se movendo..."

class Carro(Transporte):
    def mover(self):
        return "O carro está rodando pela estrada."
        
class Jetski(Transporte):
    def mover(self):
        return "O Jetski esta navegando."


class Moto(Transporte):
    def mover(self):
        return "A moto está acelerando."


class Bicicleta(Transporte):
    def mover(self):
        return "A bicicleta está pedalando."
        
        
class avião(Transporte):
    def mover(self):
        return "o avião esta rodando pelo céu."
def main():
    transportes = [Carro(), Moto(), Bicicleta(), Jetski(), avião()]
    for t in transportes:
        mensagem = t.mover()
        print(mensagem)

if __name__ == "__main__":
    main()