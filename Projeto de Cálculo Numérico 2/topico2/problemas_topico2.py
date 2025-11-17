# problemas_topico2.py
# Contém a Questão 2 do Tópico 2 - Métodos Iterativos (Gauss-Seidel)
from topico1 import problemas_topico1 as t1
from .metodos_iterativos import gauss_seidel
import math

"""
Dados Questão 2:
n = 10

MATRIZ:
-0.7071 0 -0.7071 0 0 0 0 0 0 0
0 -1 -0.7071 0 0.5 0 1 0 0 0
0 0 0.7071 0 0.8660 0 0 0 0 0
-0.7071 0 0.7071 1 0 0 0 0 0 0
0 0 0 0 -0.8660 -0.5 0 0 0 0
0 0 0 -1 -0.5 0.8660 0 0 0 0
0 0 0 0 0 -0.8660 -1 0 0 0
0.7071 1 0 0 0 0 0 1 0 0
0.7071 0 0 0 0 0 0 0 1 0
0 0 0 0 0 0.5 0 0 0 1

VETOR:
b: 500 0 0 0 100 0 0 0 0 0 

"""

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



def SistemaLinearIterativo():
    print("\n==============================================")
    print("   RESOLUÇÃO DE SISTEMA LINEAR (METODO ITERATIVO)")
    print("==============================================\n")

    # recepção de dados do usuario
    A, b = t1.ler_sistema_usuario()

    # imprime o sistema linear
    t1.imprimir_sistema(A, b)

    # aproximação inicial 
    x0 = [0.0] * 10
    precisao = 1e-4

    try:
        x, it = gauss_seidel(A, b, x0, tol=precisao)
    except ValueError as e:
        print("Erro:", e)

    # Mostrar solução:
    print("\n=== Solução do Sistema ===")
    for i, xi in enumerate(x, start=1):
        print(f"x{i} = {xi:.2f}")

    print(f"\nConcluido em {it} iteracoes.")
    print("\n==============================================")
    print("Sistema resolvido com sucesso.")
    print("==============================================\n")       

    
