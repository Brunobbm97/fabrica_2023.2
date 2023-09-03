num = int(input("Digite um número: "))
print("Sucessor: ",num + 1 )
print("Antecessor: ",num - 1 )

while True:
    try:
        num = int(input("Digite um número: "))
        print("Sucessor: ",num + 1 )
        print("Antecessor: ",num - 1 )
        break
    except ValueError:
        #raise ValueError("Digite um número válido")
        print("digite um numero valido")