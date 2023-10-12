vetor = [4, 5, 9, 19, 34, 35, 56, 71, 80]
chave = 9


def busca_recursiva(vetor, chave):
    if len(chave) == 0:
        return False
    else:
        meio = len(chave) // 2
        if chave[meio] == vetor:
            return True
        elif chave[meio] < vetor:
            return busca_recursiva(vetor, chave[meio + 1:])
        else:
            return busca_recursiva(vetor, chave[:meio])


if busca_recursiva(chave, vetor):
    indice = vetor.index(chave)
    print("A chave %d está presente no vetor na posição %d." % (chave, indice))
else:
    print("A chave %d não está presente no vetor." % chave)
