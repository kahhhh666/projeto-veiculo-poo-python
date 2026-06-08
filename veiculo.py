from datetime import date
ano_atual = date.today().year

class Veiculo:
    def __init__(self, Modelo, Marca, Placa, Anofabricacao, Valor, Combustivel):
        self.Modelo = Modelo
        self.Marca = Marca
        self.Placa = Placa
        self.Anofabricacao = Anofabricacao
        self.Valor = Valor
        self.Combustivel = Combustivel
    
    def Seguro (self ):
        self.seguro = self.Valor * 0.1  
        return self.seguro
    
    def Ipva (self):
        if ano_atual - self.Anofabricacao > 20:  
            self.ipva = 0
        elif self.Combustivel == "Gasolina":
            self.ipva = self.Valor * 0.2
        elif self.Combustivel == "Etanol":
            self.ipva = self.Valor * 0.15
        elif self.Combustivel == "Bicombustivel":
            self.ipva = self.Valor * 0.1
        elif self.Combustivel == "Hibrido":
            self.ipva = self.Valor * 0.08
        elif self.Combustivel == "Eletrico":
            self.ipva = self.Valor * 0.02
        elif self.Anofabricacao :
            self.ipva = self.Valor * 0.02