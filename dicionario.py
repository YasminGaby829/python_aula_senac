# dict
"""
usuario= {
    "nome" : "Yasmin",
    "sobrenome" : "Gabrielle",
    "fone" : 12992056858,
    "email" : "yasmin.gaby829@gmail.com"
}

print(usuario['nome'].upper(), usuario['fone'])

nome= "yasmin"
print(nome.upper())
"""
'''
produto= {
    "nome" : "camiseta",
    "cor" : ["branca", "preto", "cinza"],
    "tamanho" : ["P", "M", "G", "XG"]
    }
#print(type(produto))

produto.update({"cor" : "preta"})
print(produto)
produto["cor"]= "branca"
print(produto)
produto["cor"]= "branca", "preta", "azul"
print(produto)
produto["tamanho"]= "P", "M", "G"
print(produto)
'''
"""
produto= {
    "nome" : "camiseta",
    "cor" : ["branca", "preto", "cinza"],
    "tamanho" : ["P", "M", "G", "XG"]
    }

print(produto["cor"][1])
print(produto["tamanho"][2])

#produto["nome"]= "blusa"
produto.update({"nome": "shorts"})     #"nome".update é utilizado para adicionar ou trocar o nome de certa variavel
produto.update({"marca": ["HD", "SAMSUNG"]})
produto["marca"][0]= "OAKLEY"
produto["tamanho"].append("XXG")
produto["cor"].pop(1)
print(produto["nome"])
print(produto["cor"])
print(produto["tamanho"])
print(produto["marca"])
"""

produtos= {
    "cocalata": {
        "quantidade" : "250ml",
        "valor" : 5.00
    },
    "cocacolalata" : {
        "quantidade" : "350ml",
        "valor" : 6.00
    },
    "coxinha" : {
        "tamanho" : "medio",
        "valor" : 5.00
    }
}
print(produtos)
for x in produtos:
    print(x)

produtos["cocacolalata"]["valor"]=6.6
produtos["cocalata"]["valor"]=5.9
produtos["coxinha"]["valor"]=7.00
print(produtos)
