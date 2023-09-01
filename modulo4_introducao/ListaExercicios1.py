# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)

for i in lista:
    print(i)


# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
lista2 = ["objeto1", "objeto2", "objeto3", "objeto4", "objeto5"]
print(lista2)


# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
string1 = "Maria"
string2 = "Eduarda"
string3 = string1 + " " + string2
print(string3)


# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla
tupla4 = (1, 2, 2, 3, 4, 4, 4, 5)
print(tupla4.count(4));


# Exercício 5 - Crie um dicionário vazio e imprima na tela
dicionario5 = {}
print(dicionario5)


# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dicionario6 = {"chave1": "valor1", "chave2": "valor2", "chave3": "valor3"}
print(dicionario6)


# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
dicionario6["chave4"] = "valor4"
print(dicionario6)


# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. 
# Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.
dicionario8 = {"chave1": "valor1", "chave2": [1, 2], "chave3": "valor3"}
print(dicionario8)


# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista.
lista9 = ["string", (1,2) ,{"id1":1, "id2": 2} , 4.3]
print(lista9)


# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
print(frase[1:18])

