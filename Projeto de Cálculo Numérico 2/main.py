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
from topico4 import problemas_topico4 as t4

def main():
    while True:
        print("\n===================================")
        print("     PROJETO UNIDADE 2 - 2025.2")
        print("===================================")
        print("Selecione o TÓPICO a executar:")
        print("1 - Tópico 1 | Questão 2 - Métodos Diretos (Produção de Componentes)")
        print("2 - Tópico 2 | Questão 2 - Métodos Iterativos (Treliça Estática)")
        print("3 - Tópico 3 | Questão 3 - Mínimos Quadrados (Ajuste de Curvas)")
        print("4 - Tópico 4 | Questão 3 - Integração Numérica (Área da Seção de um Navio)")
        print("0 - Sair")

        opcao = input("Escolha: ").strip()

        if opcao == '1':
            print("\n>>> Executando Tópico 1 - Questão 2 (Método Direto: Eliminação de Gauss)")
            t1.problema2()  # já implementado
        elif opcao == '2':
            print("\n>>> Executando Tópico 2 - Questão 2 (Método Iterativo: Gauss-Seidel)")
            t2.problema2()  # Treliça
        elif opcao == '3':
            print("\n>>> Executando Tópico 3 - Questão 3 (Mínimos Quadrados: Ajuste de Curvas)")
            t3.problema3()  # Ajuste de curvas
        elif opcao == '4':
            print("\n>>> Executando Tópico 4 - Questão 3 (Integração Numérica: Seção de Navio)")
            t4.problema3()  # Área do navio
        elif opcao == '0':
            print("\nEncerrando o projeto. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
