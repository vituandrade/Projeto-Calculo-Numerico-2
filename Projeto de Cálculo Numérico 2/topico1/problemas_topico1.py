# problemas_topico1.py
# Define os três problemas do Tópico 1 (Sistemas de Equações Lineares - Métodos Diretos)

from metodos_diretos import gauss_elimination, calcular_residuo, norma_infinito

# ========== PROBLEMA 1 ==========
def problema1():
    """
    Produção de transistores, resistores e chips.
    Materiais: cobre, zinco e vidro.
    """
    A = [
        [4, 3, 2],
        [1, 3, 1],
        [2, 1, 3]
    ]
    b = [960, 510, 610]
    print("\n=== Problema 1: Produção de componentes ===")
    print("Sistema:")
    for i in range(3):
        print(f"{A[i]} = {b[i]}")

    x = gauss_elimination(A, b)
    print("\nSoluções encontradas:")
    print(f"Transistores = {x[0]:.2f}")
    print(f"Resistores   = {x[1]:.2f}")
    print(f"Chips        = {x[2]:.2f}")

    r = calcular_residuo(A, x, b)
    print("\nResíduo (A·x - b):", [f"{ri:.2e}" for ri in r])
    print("Norma infinito do resíduo:", f"{norma_infinito(r):.2e}")


# ========== PROBLEMA 2 ==========
def problema2():
    """
    Produção de três componentes elétricos usando metal, plástico e borracha.
    """
    A = [
        [0.5, 0.25, 0.1],
        [0.4, 0.5, 0.3],
        [0.3, 0.25, 0.2]
    ]
    b = [3.89, 0.095, 0.282]
    print("\n=== Problema 2: Componentes elétricos ===")

    x = gauss_elimination(A, b)
    print("\nComponentes produzidos por dia:")
    for i, val in enumerate(x, start=1):
        print(f"Componente {i} = {val:.4f}")

    r = calcular_residuo(A, x, b)
    print("\nNorma infinito do resíduo:", f"{norma_infinito(r):.2e}")


# ========== PROBLEMA 3 ==========
def problema3():
    """
    Mineração: areia, cascalho fino e grosso obtidos em 3 minas.
    """
    A = [
        [0.4, 0.3, 0.2],
        [0.3, 0.5, 0.4],
        [0.3, 0.2, 0.4]
    ]
    b = [4800, 5800, 5700]
    print("\n=== Problema 3: Mineração ===")

    x = gauss_elimination(A, b)
    print("\nMetros cúbicos extraídos de cada mina:")
    for i, val in enumerate(x, start=1):
        print(f"Mina {i} = {val:.2f} m³")

    r = calcular_residuo(A, x, b)
    print("\nNorma infinito do resíduo:", f"{norma_infinito(r):.2e}")
