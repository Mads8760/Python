#Questão: Considere uma pilha utilizada para gerenciar uma sequência de livros.
#Se você adicionar três livros à pilha e depois remover o livro no topo, qual livro será o próximo no topo da pilha?
# Dê um exemplo com os livros “Livro A”, “Livro B” e “Livro C”.

#criando a pilha
livros = []

#operção push (adicionanado elementos a pilha)
livros.append("livro A")
livros.append("livro B")
livros.append("livro C")
print("Pilhas após a operação push : ", livros)

#removendo o livro do topo
topo = livros.pop()
print(livros)
print("O proximo elemento do topo da filha será: ", livros[-1])

# o proximo elemento do topo sera o livro B