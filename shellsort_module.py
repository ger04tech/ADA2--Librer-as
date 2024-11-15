def shellsort(lista):
    incremento = len(lista) // 2
    while incremento > 0:
        for i in range(incremento, len(lista)):
            j = i
            temporal = lista[i]
            while j >= incremento and lista[j - incremento] > temporal:
                lista[j] = lista[j - incremento]
                j -= incremento
            lista[j] = temporal
        incremento = 1 if incremento == 2 else int(incremento / 2.2)
    return lista
