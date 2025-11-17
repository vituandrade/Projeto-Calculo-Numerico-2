# problemas_topico1.py
# Tópico 1 - Questão 2: Produção de Componentes Elétricos
# Método Direto: Eliminação de Gauss com pivoteamento parcial

"""
Dados Questao 2
n: 3

Matriz:
15 17 19
0.3 0.4 0.55
1  1.2  1.5

Vetor:
3890 95 282
 
b : 3890 95 282
"""
from .metodos_diretos import gauss_elimination, calcular_residuo, norma_infinito

def imprimir_sistema_topico1(A, b):
    """Imprime o sistema 3x3 do Tópico 1, Questão 2."""
    print("\n--- Sistema Linear (A·x = b) ---")
    nomes_eq = ["Metal (g)", "Plastico (g)", "Borracha (g)"]
    
    for i in range(len(A)):
        linha = f"Eq {i+1} ({nomes_eq[i]:<12}): ["
        linha += f" ({A[i][0]:.2f} * x1) + ({A[i][1]:.2f} * x2) + ({A[i][2]:.2f} * x3) ]"
        linha += f" = {b[i]:.1f}"
        print(linha)
    print("----------------------------------\n")


def ler_sistema_usuario():
    n = int(input("Informe o tamanho do sistema (n): ").strip())

    A = []
    print("\nInforme os coeficientes da matriz A:")
    for i in range(n):
        linha = input(f"  Linha {i+1} (separe por espaço): ").strip().split()
        linha = [float(x) for x in linha]
        if len(linha) != n:
            raise ValueError("Número de coeficientes inválido.")
        A.append(linha)

    print("\nInforme todos os valores do vetor b (separados por espaço):")
    b = input("  b: ").strip().split()
    b = [float(x) for x in b]

    if len(b) != n:
        raise ValueError("Quantidade de valores do vetor b incorreta.")

    return A, b


def imprimir_sistema(A, b):
    print("\n=== Sistema Linear ===")
    n = len(A)
    for i in range(n):
        linha = "  "
        for j in range(n):
            linha += f"({A[i][j]:.2f}) x{j+1}  "
        linha += f" = {b[i]:.2f}"
        print(linha)
    print("----------------------------------------------\n")


def SistemaLinearDireto():
    print("\n==============================================")
    print("   RESOLUÇÃO DE SISTEMA LINEAR (METODO DIRETO)")
    print("==============================================\n")

    # Entrada de dados:
    A, b = ler_sistema_usuario()

    # Exibir o sistema:
    imprimir_sistema(A, b)

    # Resolver:
    try:
        x = gauss_elimination(A, b)
    except ValueError as e:
        print("Erro ao resolver o sistema:", e)
        return

    # Mostrar solução:
    print("\n=== Solução do Sistema ===")
    for i, xi in enumerate(x, start=1):
        print(f"x{i} = {xi:.2f}")

    # Calcular resíduo:
    r = calcular_residuo(A, x, b)
    print("\nResíduo (A·x - b):")
    for i, ri in enumerate(r, start=1):
        print(f"  r{i} = {ri:.6e}")

    print("\nNorma infinito do resíduo:", norma_infinito(r))

    print("\n==============================================")
    print("Sistema resolvido com sucesso.")
    print("==============================================\n")





