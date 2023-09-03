while True: 
    try:
        velo = float(input("Digite a velocidade do carro: "))
        if(velo > 80):
            print("Ultrapassou o limite de velocidade!")
            amais = velo - 80
            multa = amais * 7
            print("Valor da multa : ",multa)
        else:
            print("Carro passou dentro do limite de velocidade")
        break
    except ValueError:
        print("velocidade Inválida")