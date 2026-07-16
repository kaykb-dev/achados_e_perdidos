from codigo import SistemaAchadosPerdidos
from interface import Interface

def main():
    sistema = SistemaAchadosPerdidos()
    app = Interface(sistema)
    app.executar()
    
if __name__ == "__main__":
    main()