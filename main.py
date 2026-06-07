from veiculo import Veiculo

while True :
    Modelo = input("Qual o modelo do seu carro ? ")
    Marca = input("Qual a marca do seu carro ? ")
    Placa = input("Qual a placa do seu carro ? ")
    Anofabricacao = int(input("Qual o ano de fabricação do seu carro ? "))
    Valor = float(input("Qual o valor do seu carro ? "))
    Combustivel = int(input("Digite o número do seu combustivel \n 1.Gasolina \n 2.Etanol \n 3.Bicombustível \n 4.Híbrido \n 5.Elétrico \nDigite aqui sua escolha: "))

    match Combustivel:
        case 1:
            Combustivel = "Gasolina"
        case 2:
            Combustivel = "Etanol"
        case 3:
            Combustivel = "Bicombustível"
        case 4:
            Combustivel = "Híbrido"
        case 5:
            Combustivel = "Elétrico"
        
    objVeiculo = {
        "Modelo": Modelo,
        "Marca": Marca,
        "Placa": Placa,
        "Anofabricacao": Anofabricacao,
        "Valor": Valor,
        "Combustivel": Combustivel
        
        }
    veiculo = Veiculo(**objVeiculo)
    
    opcao = input("Deseja finalizar cadastro ? (s/n) ")
    if opcao == "s":
        break
   
                    
    
    