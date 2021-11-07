from array import array

from listas import lista_ligada
from vetores import vetor
from listas import lista_ligada

print(30 * '-', 'MENU', 30 * '-')
print("1. Vetores")
print("2. Listas Ligadas")

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
    #print(lista_teste.recuperar_no(3))
