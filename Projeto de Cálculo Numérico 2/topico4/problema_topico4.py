from .metodos_integracao import trapezio, simpson

"""

Dados Questão 3
larguras: 3 2.92 2.75 2.52 2.3 1.84 0.92 0
Δx = 0.4

"""

def ler_lista_float(msg):
    return list(map(float, input("\n" + msg).strip().split()))

def IntegracaoNumerica():
    print("\n======================================================================")
    print("INTEGRACAO NUMERICA GENERICA (TRAPEZIOS / SIMPSON)")
    print("======================================================================\n")

    print("Você deseja fornecer:")
    print("1 - Alturas e larguras manualmente")
    print("2 - Apenas larguras (alturas fixas Δx)")
    opc = input("Opcao: ").strip()

    # Caso 1: usuário informa x e y
    if opc == "1":
        x = ler_lista_float("Digite os valores das alturas separados por espaço: ")
        y = ler_lista_float("Digite os valores das larguras separados por espaço: ")

        if len(x) != len(y):
            print("Erro: As quantidades de alturas e larguras devem ser iguais!")
            return
        
    # Caso 2: usuário informa apenas y e Δx
    elif opc == "2":
        y = ler_lista_float("Digite os valores das larguras separados por espaço: ")
        dx = float(input("Digite o valor do espacamento Δx: "))
        x = [i * dx for i in range(len(y))]
    else:
        print("Opcao inválida.")
        return

    print("\n--------------------------------------------------")
    print("Pontos informados:")
    print("alturas       larguras")
    print("--------------------------------------------------")
    for xi, yi in zip(x, y):
        print(f"{xi:>6.3f}     {yi:>8.3f}")
    print()

    # -------------------------- Trapézio --------------------------
    print("======================================================================")
    print("REGRA DOS TRAPEZIOS (COMPOSTA)")
    print("======================================================================")

    area_trap = trapezio(x, y)
    print(f"Area (Trapezios): {area_trap:.6f}\n")

    # -------------------------- Simpson --------------------------
    print("======================================================================")
    print("REGRA DE SIMPSON (COMPOSTA)")
    print("======================================================================")

    area_simp = simpson(x, y)
    print(f"Area (Simpson):   {area_simp:.6f}\n")

    print("======================================================================")
    print("RESULTADOS FINAIS")
    print("======================================================================")
    print(f"Trapezios: {area_trap:.6f}")
    print(f"Simpson:   {area_simp:.6f}\n")
    

    
