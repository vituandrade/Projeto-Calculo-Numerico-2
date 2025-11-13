# main.py
# Projeto Unidade 2 - Cálculo Numérico
# Menu principal que permite selecionar o Tópico (1 a 4) e o Problema (1 a 3)
# Cada tópico é modular e independente

from topico1 import problemas_topico1 as t1
from topico2 import problemas_topico2 as t2
from topico3 import problemas_topico3 as t3
from topico4 import problemas_topico4 as t4

def menu_topico1():
    while True:
        print("\n===== TÓPICO 1 - MÉTODOS DIRETOS =====")
        print("1 - Problema 1: Produção de componentes")
        print("2 - Problema 2: Componentes elétricos")
        print("3 - Problema 3: Mineração")
        print("0 - Voltar")
        op = input("Escolha: ").strip()
        if op == '1': t1.problema1()
        elif op == '2': t1.problema2()
        elif op == '3': t1.problema3()
        elif op == '0': break
        else: print("Opção inválida.")

def menu_topico2():
    while True:
        print("\n===== TÓPICO 2 - MÉTODOS ITERATIVOS =====")
        print("1 - Problema 1: Ponte de Wheatstone (Gauss-Seidel)")
        print("2 - Problema 2: Treliça (Gauss-Seidel)")
        print("3 - Problema 3: Circuito elétrico (Gauss-Seidel)")
        print("0 - Voltar")
        op = input("Escolha: ").strip()
        if op == '1': t2.problema1()
        elif op == '2': t2.problema2()
        elif op == '3': t2.problema3()
        elif op == '0': break
        else: print("Opção inválida.")

def menu_topico3():
    while True:
        print("\n===== TÓPICO 3 - INTERPOLAÇÃO / MÍNIMOS QUADRADOS =====")
        print("1 - Problema 1: Lei de Moore")
        print("2 - Problema 2: Queda de voltagem (Lagrange / Newton)")
        print("3 - Problema 3: Ajuste de curvas (reta, parábola, exponencial)")
        print("0 - Voltar")
        op = input("Escolha: ").strip()
        if op == '1': t3.problema1()
        elif op == '2': t3.problema2()
        elif op == '3': t3.problema3()
        elif op == '0': break
        else: print("Opção inválida.")

def menu_topico4():
    while True:
        print("\n===== TÓPICO 4 - INTEGRAÇÃO NUMÉRICA =====")
        print("1 - Problema 1: Área da seção de rio (Trapézio / Simpson)")
        print("2 - Problema 2: Área da superfície de rio")
        print("3 - Problema 3: Área da seção de um navio")
        print("0 - Voltar")
        op = input("Escolha: ").strip()
        if op == '1': t4.problema1()
        elif op == '2': t4.problema2()
        elif op == '3': t4.problema3()
        elif op == '0': break
        else: print("Opção inválida.")

def main():
    while True:
        print("\n===================================")
        print("     PROJETO UNIDADE 2 - 2025.2")
        print("===================================")
        print("Selecione o TÓPICO:")
        print("1 - Sistemas Lineares (Métodos Diretos)")
        print("2 - Sistemas Lineares (Métodos Iterativos)")
        print("3 - Interpolação / Mínimos Quadrados")
        print("4 - Integração Numérica")
        print("0 - Sair")
        opcao = input("Escolha: ").strip()

        if opcao == '1':
            menu_topico1()
        elif opcao == '2':
            menu_topico2()
        elif opcao == '3':
            menu_topico3()
        elif opcao == '4':
            menu_topico4()
        elif opcao == '0':
            print("\nEncerrando o projeto. Até mais!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
