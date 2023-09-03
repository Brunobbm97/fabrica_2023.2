"""counter = 0
while counter <= 10:
    if counter == 5:
        print("Valor 5")
        counter+=1
        continue
    print(counter)
    counter+=1"""
while True: 
    try:
        idade = int(input("Digite sua idade: "))
        if(idade > 18):
            print("pode obter carteira de habilitação")
        else:
            print("Idade não permitida para habilitação ")
        break
    except ValueError:
        print("Valor informado não é um número válido")