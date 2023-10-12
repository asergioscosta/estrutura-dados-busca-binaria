import random
from array import array

def busca(vetor, chave):
    num_comparacoes = 0
    for i in range(len(vetor)):
        num_comparacoes += 1
        if vetor[i] == chave:
            print("Chave %d encontrada em: [%d]" % (chave, i))
            print("Número de comparações:", num_comparacoes)
            return i

    print("Chave %d não encontrada." % chave)


vetor = array('i')
for _ in range(100):
    numero_aleatorio = random.randint(1, 100)
    vetor.append(numero_aleatorio)

chave = int(input("Digite o valor da chave: "))
busca(vetor, chave)

for numero in vetor:
    print(numero, end=' ')