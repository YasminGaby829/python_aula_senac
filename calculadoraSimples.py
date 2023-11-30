#pegar dois números e efetuar mostrando na tela
# a soma, divisão, multipliação e subtração da seguinte maneira
# exemplo:
# A soma dos dois números é :SOMA
n1=10
print("O número é :", n1)
n1= int(input("Qual é o primeiro número"))
n2=int(input("qual o segundo número"))
soma=n1+n2
print("o resultado da soma é :" ,soma)
subtração=n1-n2
print("o resultado da subtração é:" , subtração)
multiplicação=n1*n2
print("o valor da multiplicação é", multiplicação)
divisão=n1/n2
print("o valor final da divisão é", divisão)

n1= int(input("Digite o primeiro número: "))
n2= int(input("Digite o segundo número: "))
soma=n1+n2
divisão=n1/n2
#multiplicação=n1*n2
#subtração=n1-n2
print("O resultado da soma é: ", soma)
#print("O resultado da soma é:", n1+n2)
print("O resultado da subtração é:", n1-n2)
print("O resultado da divisão é:", n1/n2)
print(type(divisão))
print("O resultado da multiplicação é:", n1*n2)


