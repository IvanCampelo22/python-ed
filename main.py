from array import array

from listas import lista_ligada
from vetores import vetor
from listas import lista_ligada, lista_duplamente_ligada
from pilhas import pilha
from filas import fila

print(30 * '-', 'MENU', 30 * '-')
print("1. Vetores")
print("2. Listas Ligadas")
print("3. Lista Duplamente Ligada")
print("4. Pilha")
print("5. Fila")

menu = int(input("Digite uma opção desejada: "))

if menu == 1:
    vetor_teste = vetor.Vetor(0)
    vetor_teste.inserir_elemento_posicao(1, 0)
    vetor_teste.inserir_elemento_posicao(2, 1)
    vetor_teste.inserir_elemento_posicao(3, 2)
    vetor_teste.inserir_elemento_posicao(4, 2)
    vetor_teste.inserir_elemento_posicao(5, 2)
    vetor_teste.inserir_elemento_final(1)
    print(vetor_teste.tamanho_vetor())
    print(vetor_teste)
    #print(vetor_teste.contem(4))
    print(vetor_teste.indece(4))
    vetor_teste.remover_elemento_indice(3)
    print(vetor_teste)
    vetor_teste.remover_elemento(5)
    print(vetor_teste)

elif menu == 2:
    lista_teste = lista_ligada.ListaLigada()
    lista_teste.inserir(1)
    lista_teste.inserir(4)
    lista_teste.inserir(5)
    lista_teste.inserir_posicao(1, 10)
    print(lista_teste)
    lista_teste.remover_elemento(4)
    print(lista_teste)
    #print(lista_teste.contem(5))
    #print(lista_teste.indice(5))
    #print(lista_teste.recuperar_no(3))

elif menu == 3:
    lista_teste = lista_duplamente_ligada.ListaDuplamenteLigada()
    lista_teste.inserir(1)
    lista_teste.inserir(4)
    lista_teste.inserir(5)
    lista_teste.inserir_posicao(1, 10)
    print(lista_teste)
    lista_teste.remover_elemento(4)
    lista_teste.remover_posicao(1)
    print(lista_teste)
    #print(lista_teste.contem(5))
    #print(lista_teste.indice(5))
    #print(lista_teste.recuperar_no(3))

elif menu == 4:
    pilha_teste = pilha.Pilha()
    pilha_teste.empilhar(5)
    pilha_teste.empilhar(6)
    pilha_teste.empilhar(7)
    print(pilha_teste.desempilhar())

elif menu == 5:
    fila_teste = fila.Fila()
    fila_teste.enfileirar(1)
    fila_teste.enfileirar(2)
    fila_teste.enfileirar(3)
    fila_teste.enfileirar(4)
    print(fila_teste) # 1 2 3 4
    print(fila_teste.desenfileirar())
    print(fila_teste) # 2 3 4
    print(fila_teste.desenfileirar())
    print(fila_teste) # 3 4
    fila_teste.enfileirar(6)
    print(fila_teste)
else:
    print("Opção inválida")

