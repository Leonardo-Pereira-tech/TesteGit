def criarMatriz(n):
    matriz = []
    for _ in range(n):
        num = input().split()
        linha = []
        for k in num:
            linha.append(int(k))
        matriz.append(linha)
    return matriz

def criarVisitados(n):
    visitados = []
    for _ in range(n):
        linha = []
        for _ in range(n):
            linha.append(False)
        visitados.append(linha)
    return visitados

def buscar(matriz, i, j, visitados):
    if i < 0 or i >= len(matriz) or j < 0 or j >= len(matriz):
        return False
    if visitados[i][j] == True:
        return False
    if matriz[i][j] == 0:
        return False
    if i == len(matriz) - 1 and j == len(matriz) - 1:
        return True
    visitados[i][j] = True
    if buscar(matriz, i + 1, j, visitados):
        return True
    if buscar(matriz, i - 1, j, visitados):
        return True
    if buscar(matriz, i, j + 1, visitados):
        return True
    if buscar(matriz, i, j - 1, visitados):
        return True
    return False

ordem = int(input())
matriz = criarMatriz(ordem)
visitados = criarVisitados(ordem)
if matriz[0][0] == 0 and matriz[ordem - 1][ordem - 1] == 0:
    print('NOT OK')
else:
    resultado = buscar(matriz, 0, 0, visitados)
    if resultado == True:
        print('OK')
    else:
        print('NOT OK')
