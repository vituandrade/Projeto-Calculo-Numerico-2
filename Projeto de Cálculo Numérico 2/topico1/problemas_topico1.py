# problemas_topico1.py
# Contém apenas a Questão 2 do Tópico 1 - Métodos Diretos

from .metodos_diretos import gauss_elimination, calcular_residuo, norma_infinito

def problema2():
    """
    Tópico 1 - Questão 2
    Produção de três componentes elétricos.
    Materiais: metal, plástico e borracha.
    Método: Eliminação de Gauss com pivoteamento parcial.
    """

    print("\n=== Topico 1 - Questao 2: Producao de Componentes Eletricos ===")
    print("Resolvendo o sistema linear pelo metodo direto (Eliminacao de Gauss)\n")

    # Sistema hipotético baseado na descrição do enunciado
    # Cada linha representa o consumo de materiais por tipo de componente
    # Cada coluna representa o componente (x1, x2, x3)
    #
    # Exemplo:
    #   0.5x1 + 0.25x2 + 0.10x3 = 3.89   (metal)
    #   0.40x1 + 0.50x2 + 0.30x3 = 0.095 (plastico)
    #   0.30x1 + 0.25x2 + 0.20x3 = 0.282 (borracha)
    #
    A = [
        [0.5, 0.25, 0.10],
        [0.4, 0.50, 0.30],
        [0.3, 0.25, 0.20]
    ]
    b = [3.89, 0.095, 0.282]

    try:
        x = gauss_elimination(A, b)
    except ValueError as e:
        print("Erro ao resolver o sistema:", e)
        return

    print("Solucoes encontradas (quantidade de componentes por dia):")
    for i, xi in enumerate(x, start=1):
        print(f"Componente {i}: {xi:.6f}")

    r = calcular_residuo(A, x, b)
    print("\nResiduo (A·x - b):", [f"{ri:.2e}" for ri in r])
    print("Norma infinito do residuo:", f"{norma_infinito(r):.2e}")

    print("\nInterpretacao:")
    print("Cada valor indica a quantidade diaria de cada componente possivel")
    print("com base nas limitacoes de metal, plastico e borracha disponiveis.")
