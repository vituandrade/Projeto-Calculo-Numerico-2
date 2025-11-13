# metodos_diretos.py
# Implementa o método direto: Eliminação de Gauss com pivoteamento parcial

def gauss_elimination(A, b):
    """
    Resolve o sistema A x = b usando Eliminação de Gauss com pivoteamento parcial.
    Retorna a lista x com as soluções.
    """
    n = len(A)
    M = [row[:] for row in A]
    y = b[:]

    for k in range(n):
        # pivoteamento parcial
        pivot_row = max(range(k, n), key=lambda i: abs(M[i][k]))
        if abs(M[pivot_row][k]) < 1e-12:
            raise ValueError("Matriz singular ou quase singular.")

        if pivot_row != k:
            M[k], M[pivot_row] = M[pivot_row], M[k]
            y[k], y[pivot_row] = y[pivot_row], y[k]

        # Eliminação
        for i in range(k + 1, n):
            fator = M[i][k] / M[k][k]
            for j in range(k, n):
                M[i][j] -= fator * M[k][j]
            y[i] -= fator * y[k]

    # Substituição regressiva
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        soma = y[i] - sum(M[i][j] * x[j] for j in range(i + 1, n))
        x[i] = soma / M[i][i]
    return x


def calcular_residuo(A, x, b):
    """Calcula o vetor resíduo r = A·x - b."""
    n = len(A)
    r = [0.0] * n
    for i in range(n):
        r[i] = sum(A[i][j] * x[j] for j in range(n)) - b[i]
    return r


def norma_infinito(v):
    """Retorna a norma infinito (máximo valor absoluto) de um vetor."""
    return max(abs(vi) for vi in v)
