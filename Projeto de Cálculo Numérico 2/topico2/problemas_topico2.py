# problemas_topico2.py
# Contém a Questão 2 do Tópico 2 - Métodos Iterativos (Gauss-Seidel)

from .metodos_iterativos import gauss_seidel
import math

# Constantes trigonométricas para os ângulos
s45 = math.sin(math.pi / 4)  # 45 graus
c45 = math.cos(math.pi / 4)  # 45 graus
s60 = math.sin(math.pi / 3)  # 60 graus
c60 = math.cos(math.pi / 3)  # 60 graus
s30 = math.sin(math.pi / 6)  # 30 graus
c30 = math.cos(math.pi / 6)  # 30 graus

def imprimir_sistema_linear(A, b, nomes_vars):
    """
    Imprime o sistema linear A·x = b de forma legível,
    mostrando apenas os termos não-nulos de A.
    """
    print("\n--- Sistema Linear (A·x = b) ---")
    n = len(A)
    for i in range(n):
        linha_eq = f"Eq {i+1:02d}: ["
        termos = []
        for j in range(n):
            if abs(A[i][j]) > 1e-10: # Se o termo não for zero
                termos.append(f"({A[i][j]:+8.4f} * {nomes_vars[j]})")
        
        linha_eq += " + ".join(termos)
        linha_eq += f" ] = {b[i]:.4f}"
        print(linha_eq)
    print("----------------------------------\n")


def problema2():
    """
    Tópico 2 - Questão 2
    Treliça estaticamente determinada (juntas articuladas)
    Método: Gauss-Seidel com precisão de 0.0001
    """

    print("\n=== Topico 2 - Questao 2: Trelia Estatica ===")
    print("Usando o metodo iterativo de Gauss-Seidel (precisao = 0.0001)\n")

    # --------------------------------------------------------------------------
    # Sistema de 10 equações e 10 incógnitas (7 forças internas + 3 reações)
    #
    # As 10 incógnitas (vetor x) são:
    nomes_variaveis = [
        "F_12", "F_13", "F_23", "F_24", "F_34", 
        "F_45", "F_35", "R_1x", "R_1y", "R_5y"
    ]
    # --------------------------------------------------------------------------

    # Matriz A (10x10), reordenada para ter diagonal não-nula
    A = [
        # Eq 4 (pivô em x[0]=F_12): -s45*x[0] - s45*x[2] = 500
        [-s45,   0,   -s45,   0,     0,     0,    0,   0,   0,   0],
        # Eq 5 (pivô em x[1]=F_13): -x[1] - c45*x[2] + c60*x[4] + x[6] = 0
        [  0,  -1,   -c45,   0,   c60,     0,    1,   0,   0,   0],
        # Eq 6 (pivô em x[2]=F_23): s45*x[2] + s60*x[4] = 0
        [  0,   0,    s45,   0,   s60,     0,    0,   0,   0,   0],
        # Eq 3 (pivô em x[3]=F_24): -c45*x[0] + c45*x[2] + x[3] = 0
        [-c45,   0,    c45,   1,     0,     0,    0,   0,   0,   0],
        # Eq 8 (pivô em x[4]=F_34): -s60*x[4] - s30*x[5] = 100
        [  0,   0,      0,   0,  -s60,  -s30,    0,   0,   0,   0],
        # Eq 7 (pivô em x[5]=F_45): -x[3] - c60*x[4] + c30*x[5] = 0
        [  0,   0,      0,  -1,  -c60,   c30,    0,   0,   0,   0],
        # Eq 9 (pivô em x[6]=F_35): -c30*x[5] - x[6] = 0
        [  0,   0,      0,   0,     0,  -c30,   -1,   0,   0,   0],
        # Eq 1 (pivô em x[7]=R_1x): c45*x[0] + x[1] + x[7] = 0
        [ c45,   1,      0,   0,     0,     0,    0,   1,   0,   0],
        # Eq 2 (pivô em x[8]=R_1y): s45*x[0] + x[8] = 0
        [ s45,   0,      0,   0,     0,     0,    0,   0,   1,   0],
        # Eq 10 (pivô em x[9]=R_5y): s30*x[5] + x[9] = 0
        [  0,   0,      0,   0,     0,   s30,    0,   0,   0,   1]
    ]

    # Vetor b (10x1)
    b = [
        500,  # Eq 4
        0,    # Eq 5
        0,    # Eq 6
        0,    # Eq 3
        100,  # Eq 8
        0,    # Eq 7
        0,    # Eq 9
        0,    # Eq 1
        0,    # Eq 2
        0     # Eq 10
    ]

    # --- PONTO A: Apresentar o sistema linear ---
    imprimir_sistema_linear(A, b, nomes_variaveis)

    # Aproximação inicial
    x0 = [0.0] * 10
    precisao = 1e-4

    try:
        x, it = gauss_seidel(A, b, x0, tol=precisao)
        
        print("Solucao encontrada (Forcas em N ou kN, dependendo das cargas):")
        for nome, val in zip(nomes_variaveis, x):
            # Mudei o nome aqui para ficar igual ao da lista
            print(f"{nome:<4} = {val:10.4f}")
        
        print(f"\nConcluido em {it} iteracoes.")
        print("\nInterpretacao:")
        print("Valores positivos indicam tracao (barra 'puxada').")
        print("Valores negativos indicam compressao (barra 'comprimida').")

    except ValueError as e:
        print("Erro:", e)