# main.py
# Projeto Unidade 2 - 2025.2
# Grupo responsável pelos problemas:
#   Tópico 1 - Questão 2
#   Tópico 2 - Questão 2
#   Tópico 3 - Questão 3
#   Tópico 4 - Questão 3

from topico1 import problemas_topico1 as t1
from topico2 import problemas_topico2 as t2
from topico3 import problemas_topico3 as t3
from topico4 import problema_topico4 as t4

def main():
    while True:
        print("\n===================================")
        print("     PROJETO UNIDADE 2 - 2025.2")
        print("===================================")
        print("Selecione o TOPICO a executar:")
        print("1 - Topico 1 | Questao 2 - Metodos Diretos (Producao de Componentes)")
        print("2 - Topico 2 | Questao 2 - Metodos Iterativos (Trelia Estatica)")
        print("3 - Topico 3 | Questao 3 - Minimos Quadrados (Ajuste de Curvas)")
        print("4 - Topico 4 | Questao 3 - Integracao Numerica (Area da Secao de um Navio)")
        print("0 - Sair")

        opcao = input("Escolha: ").strip()

        if opcao == '1':
            print("\n>>> Executando Topico 1 - Questao 2 (Metodo Direto: Eliminacao de Gauss)")
            t1.problema2()  # já implementado
        elif opcao == '2':
            print("\n>>> Executando Topico 2 - Questao 2 (Metodo Iterativo: Gauss-Seidel)")
            t2.problema2()  # Treliça
        elif opcao == '3':
            print("\n>>> Executando Topico 3 - Questao 3 (Minimos Quadrados: Ajuste de Curvas)")
            t3.problema3()  # Ajuste de curvas
        elif opcao == '4':
            print("\n>>> Executando Topico 4 - Questao 3 (Integracao Numerica: Secao de Navio)")
            t4.problema3()  # Área do navio
        elif opcao == '0':
            print("\nEncerrando o projeto. Ate mais!")
            break
        else:
            print("Opcao invalida. Tente novamente.")

if __name__ == "__main__":
    main()
