vetor = [4, 5, 9, 19, 34, 35, 56, 71, 80]
chave = 9


def busca_binaria(vetor, chave):
    esquerda = 0
    direita = len(vetor) - 1
    num_divisoes = 0
    num_comparacoes = 0

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        num_divisoes += 1

        if chave == vetor[meio]:
            print("Chave %d encontrada em [%d]" % (chave, meio))
            print("Número de divisões:", num_divisoes)
            print("Número de comparações:", num_comparacoes)
            return meio
        else:
            num_comparacoes += 1
            if chave < vetor[meio]:
                direita = meio - 1
            else:
                esquerda = meio + 1

    print("Chave %d não encontrada" % chave)


busca_binaria(vetor, chave)
