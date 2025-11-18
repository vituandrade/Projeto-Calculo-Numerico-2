📘 Projeto – Cálculo Numérico (2025.2)

Este repositório reúne as implementações desenvolvidas para o projeto da
disciplina Cálculo Numérico – 2025.2, envolvendo métodos numéricos
aplicados a problemas reais.
O objetivo geral é criar soluções computacionais reutilizáveis,
permitindo novas entradas e adaptabilidade para problemas semelhantes
aos apresentados no enunciado.

🧩 Estrutura Geral do Projeto

O projeto está dividido em quatro tópicos principais:

1.  Sistemas Lineares – Métodos Diretos
2.  Sistemas Lineares – Métodos Iterativos
3.  Interpolação Polinomial e Regressão por Mínimos Quadrados
4.  Integração Numérica

As explicações abaixo descrevem somente o escopo geral e os métodos
abordados, sem entrar em respostas específicas dos problemas.

📌 Tópico 01 — Sistemas de Equações Lineares (Métodos Diretos)

Os problemas deste tópico envolvem modelagem de situações reais por meio
de sistemas lineares, como:

-   planejamento de produção,
-   alocação de recursos,
-   mistura de materiais.

Métodos Diretos Utilizados

-   Eliminação de Gauss
-   Gauss-Jordan
-   Fatoração LU

Cada método foi implementado visando clareza, robustez e a possibilidade
de inserir novos dados arbitrários.

📌 Tópico 02 — Sistemas Lineares (Métodos Iterativos)

Neste tópico lidamos com sistemas provenientes de:

-   circuitos elétricos,
-   treliças mecânicas,
-   sistemas esparsos.

Método Iterativo Utilizado

-   Método de Gauss–Seidel

As implementações permitem entrada do sistema, definição de tolerância e
chute inicial.

📌 Tópico 03 — Interpolação Polinomial e Mínimos Quadrados

Trabalhamos com aproximação de funções a partir de dados experimentais.

Métodos Implementados

-   Interpolação de Lagrange
-   Interpolação de Newton
-   Regressão por Mínimos Quadrados (reta, parábola, exponencial)

Também é calculado o erro quadrático de cada ajuste.

📌 Tópico 04 — Integração Numérica

Usado para calcular áreas aproximadas a partir de dados discretos.

Métodos Implementados

-   Regra dos Trapézios
-   Regra de Simpson 1/3 Repetida

🛠️ Requisitos Gerais

-   Entrada de novos dados
-   Interface clara com o usuário
-   Opção de repetir cálculos
-   Relatório com contribuição de cada membro da equipe

📁 Organização Sugerida do Repositório

/ ├── topico01_metodos_diretos/ ├── topico02_metodos_iterativos/ ├──
topico03_interpolacao_regressao/ ├── topico04_integracao/ └── README.md
