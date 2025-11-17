# problemas_topico1.py
# Tópico 1 - Questão 2: Produção de Componentes Elétricos
# Método Direto: Eliminação de Gauss com pivoteamento parcial

"""
Dados Questao 2
n: 3

Coluna 1: 15 17 19
Coluna 2: 0.3 0.4 0.55
Coluna 3: 1  1.2  1.5

b1: 3890
b2: 95
b3: 282
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

def problema2():
    """
    Tópico 1 - Questão 2
    Determinar quantos componentes de cada tipo podem ser produzidos por dia
    usando o método direto de Eliminação de Gauss com pivoteamento parcial.
    """

    print("\n=== Tópico 1 - Questão 2: Produção de Componentes Elétricos ===")
    print("Método: Eliminação de Gauss com pivoteamento parcial\n")

    # ----------------------------------------------------------------------
    # Sistema baseado nos dados do enunciado (todas as massas convertidas para gramas)
    # ----------------------------------------------------------------------
    A = [
        [15.0, 17.0, 19.0],   # consumo de METAL (g por componente)
        [0.30, 0.40, 0.55],   # consumo de PLÁSTICO (g por componente)
        [1.00, 1.20, 1.50]    # consumo de BORRACHA (g por componente)
    ]

    b = [3890.0, 95.0, 282.0]  # materiais disponíveis por dia (em g)
    # ----------------------------------------------------------------------

    # --- PONTO A: Apresentar o sistema linear ---
    imprimir_sistema_topico1(A, b)

    # --- PONTOS B e C: Resolver com método direto ---
    try:
        # Ponto B (gauss_elimination) e Ponto C (obter x)
        x = gauss_elimination(A, b) 
    except ValueError as e:
        print("Erro ao resolver o sistema:", e)
        return

    # ----------------------------------------------------------------------
    # Impressão da solução
    # ----------------------------------------------------------------------
    print("Soluções encontradas (quantidade de componentes por dia):")
    for i, xi in enumerate(x, start=1):
        if abs(xi - round(xi)) < 1e-8:
            print(f"Componente {i}: {int(round(xi))} unidades/dia")
        else:
            print(f"Componente {i}: {xi:.6f} unidades/dia")

    # ----------------------------------------------------------------------
    # Cálculo do resíduo numérico
    # ----------------------------------------------------------------------
    r = calcular_residuo(A, x, b)
    r_display = [0.0 if abs(ri) < 1e-10 else ri for ri in r]

    print("\nResíduo (A·x - b):", [f"{ri:.10e}" for ri in r_display])
    print("Norma infinito do resíduo:", f"{norma_infinito(r):.10e}")

    # ----------------------------------------------------------------------
    # Verificação de viabilidade física
    # ----------------------------------------------------------------------
    if any(xi < -1e-12 for xi in x):
        print("\nAVISO: Há componentes com quantidade negativa — verifique os dados do sistema.")
    else:
        print("\nTodas as quantidades são não-negativas (viáveis fisicamente).")

    # ----------------------------------------------------------------------
    # Interpretação textual
    # ----------------------------------------------------------------------
    print("\nInterpretação:")
    print("Cada valor indica quantos componentes de cada tipo podem ser produzidos")
    print("respeitando os limites diários de metal, plástico e borracha disponíveis.")
    print("O resíduo praticamente nulo confirma que a solução é numericamente exata.")






def ler_sistema_usuario():
    n = int(input("Informe o tamanho do sistema (n): ").strip())

    A = []
    print("\nInforme os coeficientes da matriz A:")
    for i in range(n):
        linha = input(f"  Coluna {i+1} (separe por espaço): ").strip().split()
        linha = [float(x) for x in linha]
        if len(linha) != n:
            raise ValueError("Número de coeficientes inválido.")
        A.append(linha)

    print("\nInforme os valores do vetor b:")
    b = []
    for i in range(n):
        bi = float(input(f"  b{i+1}: ").strip())
        b.append(bi)

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





