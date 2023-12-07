"""
str="textos"
int=10
float=10.5
boolean=true

# nomes para variavel
nome = "yasmin"
print(nome)
#mostrando o tipo
print (type(nome))
#função length (espaços tambem contam)
print(len(nome))
#função Uper case
print(nome.upper())
for x in nome:
    print(x)

print(nome[4::])
"""
#print(a)
#print(b)
#print(c)
#a,b,c=10,3,5
#print(type(a))
#print(a,b,c)
#a="yasmin"
#print(type(a))
#print(a,b,c)
#a=100
#print(type(a))
#print(a,b,c)

nomeCompleto= "Yasmin Gabrielle dos Santos Thereza"

print(nomeCompleto[0:10]) # primeiros caracteres
print(nomeCompleto[-1]) # útimo caracter
print(nomeCompleto[3:10])
print(nomeCompleto[5::])
print(nomeCompleto[-6:-1])
print(nomeCompleto[-6::])

cpf= "46075223843"
print(cpf[0:3]+"."+cpf[3:6]+"."+cpf[6:9]+"-"+cpf[-2::])  #sempre que for converter o cpf sempre usar o sinal de soma

