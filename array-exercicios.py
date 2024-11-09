#Questão: Suponha que você tem um array que armazena os nomes de cinco frutas: [“Maçã”, “Banana”, “Cereja”, “Damasco”, “Uva”].
#Como você adicionaria uma nova fruta ao final do array e como removeria a fruta da terceira posição?

#adicionando o array

frutas = ["Maça", "Banana","Cereja","Damasco","Uva"]
print(frutas)

#adicionando um nova fruta ao final do array
frutas.append("Melancia")
print(frutas)

#removendo a fruta na terceira posição
print(frutas[3])
frutas.remove('Damasco')
print(frutas)