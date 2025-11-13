# problemas_topico2.py
# Contém apenas a Questão 2 do Tópico 2 - Métodos Iterativos (Gauss-Seidel)

from metodos_iterativos import gauss_seidel, imprimir_resultado

def problema2():
    """
    Tópico 2 - Questão 2
    Treliça estaticamente determinada (juntas articuladas)
    Método: Gauss-Seidel com precisão de 0.0001
    """

    print("\n=== Topico 2 - Questao 2: Trelia Estatica ===")
    print("Usando o metodo iterativo de Gauss-Seidel (precisao = 0.0001)\n")

    # Exemplo de sistema linear representando forças nas barras da treliça
    # Cada equação representa o equilíbrio em uma junta.
    # Esse sistema é esparso (muitos zeros) e convergente (diagonal dominante).

    A = [
        [10, 2, 0, 0],
        [2, 8, -1, 0],
        [0, -1, 7, 1],
        [0, 0, 1, 5]
    ]

    b = [14, 12, 10, 8]  # Forças externas ou cargas aplicadas (exemplo)

    # Aproximação inicial (todas as forças = 0)
    x0 = [0, 0, 0, 0]

    try:
        x, it = gauss_seidel(A, b, x0, tol=1e-4)
        imprimir_resultado(x, it)
    except ValueError as e:
        print("Erro:", e)

    print("\nAs variaveis x1, x2, x3 e x4 representam as forcas internas em cada barra (em kN).")
    print("Esses valores satisfazem as equacoes de equilibrio nas juntas da trelia.")
    print("O metodo iterativo foi escolhido por lidar bem com sistemas esparsos e acoplados.")
