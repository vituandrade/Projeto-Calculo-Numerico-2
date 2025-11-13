# metodos_iterativos.py
# Implementa o método iterativo de Gauss-Seidel para sistemas lineares

def gauss_seidel(A, b, x0=None, tol=1e-4, max_iter=1000):
    """
    Resolve o sistema A x = b pelo método de Gauss-Seidel.
    Retorna o vetor solução x e o número de iterações.
    """
    n = len(A)
    x = [0.0] * n if x0 is None else x0[:]

    for k in range(1, max_iter + 1):
        x_ant = x[:]
        for i in range(n):
            soma1 = sum(A[i][j] * x[j] for j in range(i))
            soma2 = sum(A[i][j] * x_ant[j] for j in range(i + 1, n))
            x[i] = (b[i] - soma1 - soma2) / A[i][i]

        # Critério de parada: norma infinito da diferença
        erro = max(abs(x[i] - x_ant[i]) for i in range(n))
        if erro < tol:
            return x, k

    raise ValueError("Gauss-Seidel nao convergiu apos %d iteracoes" % max_iter)


def imprimir_resultado(x, iteracoes):
    """Mostra as soluções formatadas."""
    print("\nSolucao encontrada:")
    for i, xi in enumerate(x, start=1):
        print(f"x{i} = {xi:.6f}")
    print(f"Iteracoes: {iteracoes}")
