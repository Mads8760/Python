#Questão: Imagine um array que armazena os nomes de três cores: “Azul”, “Vermelho” e “Amarelo”.
#Como você adicionaria a cor “Verde” ao início da lista e como removeria a segunda cor?

#adicionando o array
cores = ["Azul", "Vermelho", "Amarelo"]
print(cores)

#adicionando a cor verde ao inicio da lista
cores.insert(0,"Verde")
print(cores)

#removendo a segunda cor
print(cores[1])
cores.remove("Azul")
print(cores)