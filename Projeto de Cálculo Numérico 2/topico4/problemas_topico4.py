from .metodos_integracao import trapezio, simpson

"""

Dados Questão 3
larguras: 3 2.92 2.75 2.52 2.3 1.84 0.92 0
Δy = 0.4

"""

def ler_lista_float(msg):
    return list(map(float, input("\n" + msg).strip().split()))

def IntegracaoNumerica():
    print("\n======================================================================")
    print("INTEGRACAO NUMERICA GENERICA (TRAPEZIOS / SIMPSON)")
    print("======================================================================\n")

    print("Você deseja fornecer:")
    print("1 - Alturas e larguras")
    print("2 - Larguras e altura fixa Δy")
    opc = input("Opcao: ").strip()

    # Caso 1: usuário informa x e y
    if opc == "1":
        x = ler_lista_float("Digite os valores das larguras separados por espaço: ")
        y = ler_lista_float("Digite os valores das alturas separados por espaço: ")

        if len(x) != len(y):
            print("Erro: A quantidade de alturas e larguras devem ser iguais!")
            return
        
    # Caso 2: usuário informa apenas x e Δy
    elif opc == "2":
        x = ler_lista_float("Digite os valores das larguras separados por espaço: ")
        dy = float(input("Digite o valor do espacamento Δy: "))
        y = [i * dy for i in range(len(x))]
    else:
        print("Opcao inválida.")
        return

    print("\n--------------------------------------------------")
    print("Pontos informados:")
    print("larguras       altura")
    print("--------------------------------------------------")
    for xi, yi in zip(y, x):
        print(f"{yi:>6.3f}     {xi:>8.3f}")
    print()

    # -------------------------- Trapézio --------------------------
    print("======================================================================\n")
    print("REGRA DOS TRAPEZIOS (COMPOSTA)")
    area_trap = trapezio(y, x)
    print(f"Area (Trapezios): {area_trap:.6f}\n")

    # -------------------------- Simpson --------------------------
    print("REGRA DE SIMPSON (COMPOSTA)")
    area_simp = simpson(y, x)
    print(f"Area (Simpson):   {area_simp:.6f}\n")
    print("======================================================================")
    

    
