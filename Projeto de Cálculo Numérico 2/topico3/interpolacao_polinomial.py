# interpolacao_polinomial.py
# Implementa métodos de interpolação: Lagrange, Newton e Mínimos Quadrados

import math
from topico1.metodos_diretos import gauss_elimination


# ============= MÉTODO DE LAGRANGE =============
def lagrange_interpolation(x_points, y_points, x):
    """
    Interpola um ponto x usando o polinômio de Lagrange.
    
    Args:
        x_points: lista de pontos x conhecidos
        y_points: lista de pontos y conhecidos
        x: valor de x para interpolação
    
    Returns:
        valor interpolado em x
    """
    n = len(x_points)
    resultado = 0.0
    
    for i in range(n):
        # Calcula L_i(x) - base de Lagrange
        Li = 1.0
        for j in range(n):
            if i != j:
                Li *= (x - x_points[j]) / (x_points[i] - x_points[j])
        resultado += y_points[i] * Li
    
    return resultado


# ============= MÉTODO DE NEWTON (DIFERENÇAS DIVIDIDAS) =============
def newton_divided_differences(x_points, y_points):
    """
    Calcula a tabela de diferenças divididas de Newton.
    
    Returns:
        matriz de diferenças divididas
    """
    n = len(x_points)
    # Cria tabela de diferenças divididas
    dd = [[0.0 for _ in range(n)] for _ in range(n)]
    
    # Preenche primeira coluna com y_points
    for i in range(n):
        dd[i][0] = y_points[i]
    
    # Calcula as diferenças divididas
    for j in range(1, n):
        for i in range(j, n):
            dd[i][j] = (dd[i][j-1] - dd[i-1][j-1]) / (x_points[i] - x_points[i-j])
    
    return dd


def newton_interpolation(x_points, y_points, x):
    """
    Interpola um ponto x usando o polinômio de Newton (diferenças divididas).
    
    Args:
        x_points: lista de pontos x conhecidos
        y_points: lista de pontos y conhecidos
        x: valor de x para interpolação
    
    Returns:
        valor interpolado em x
    """
    n = len(x_points)
    dd = newton_divided_differences(x_points, y_points)
    
    resultado = dd[0][0]
    produto = 1.0
    
    for i in range(1, n):
        produto *= (x - x_points[i-1])
        resultado += dd[i][i] * produto
    
    return resultado


def print_newton_differences_table(x_points, y_points):
    """
    Imprime a tabela de diferenças divididas de Newton de forma formatada.
    """
    n = len(x_points)
    dd = newton_divided_differences(x_points, y_points)
    
    print("\nTabela de Diferenças Divididas:")
    print("-" * 80)
    
    for i in range(n):
        print(f"x[{i}] = {x_points[i]:10.4f}  ", end="")
        for j in range(i + 1):
            print(f"{dd[i][j]:12.6f}  ", end="")
        print()


# ============= MÉTODO DOS MÍNIMOS QUADRADOS =============
def least_squares_line(x_points, y_points):
    """
    Ajusta uma reta y = a + b*x aos pontos usando mínimos quadrados.
    
    Returns:
        tupla (a, b) onde y = a + b*x
    """
    n = len(x_points)
    
    # Somas necessárias
    sum_x = sum(x_points)
    sum_y = sum(y_points)
    sum_xy = sum(x_points[i] * y_points[i] for i in range(n))
    sum_x2 = sum(x_points[i] ** 2 for i in range(n))
    
    # Determinante do sistema
    denom = n * sum_x2 - sum_x ** 2
    
    if abs(denom) < 1e-12:
        raise ValueError("Sistema singular: nao e possivel ajustar uma reta.")
    
    # Coeficientes
    b = (n * sum_xy - sum_x * sum_y) / denom
    a = (sum_y - b * sum_x) / n
    
    return a, b


def least_squares_parabola(x_points, y_points):
    """
    Ajusta uma parábola y = a + b*x + c*x² aos pontos usando mínimos quadrados.
    
    Returns:
        tupla (a, b, c) onde y = a + b*x + c*x²
    """
    n = len(x_points)
    
    # Somas necessárias
    sum_x = sum(x_points)
    sum_y = sum(y_points)
    sum_x2 = sum(x_points[i] ** 2 for i in range(n))
    sum_x3 = sum(x_points[i] ** 3 for i in range(n))
    sum_x4 = sum(x_points[i] ** 4 for i in range(n))
    sum_xy = sum(x_points[i] * y_points[i] for i in range(n))
    sum_x2y = sum(x_points[i] ** 2 * y_points[i] for i in range(n))
    
    # Sistema linear: A * coeff = b
    A = [
        [n, sum_x, sum_x2],
        [sum_x, sum_x2, sum_x3],
        [sum_x2, sum_x3, sum_x4]
    ]
    
    b = [sum_y, sum_xy, sum_x2y]
    
    # Resolve o sistema
    coeffs = gauss_elimination(A, b)
    
    return tuple(coeffs)  # (a, b, c)


def least_squares_exponential(x_points, y_points):
    """
    Ajusta uma exponencial y = a * e^(b*x) aos pontos usando mínimos quadrados.
    Lineariza através de logaritmo: ln(y) = ln(a) + b*x
    
    Returns:
        tupla (a, b) onde y = a * e^(b*x)
    """
    n = len(x_points)
    
    # Verifica se todos os y_points são positivos
    if any(y <= 0 for y in y_points):
        raise ValueError("Todos os pontos y devem ser positivos para ajuste exponencial.")
    
    # Lineariza: z = ln(y), então z = ln(a) + b*x
    z_points = [math.log(y) for y in y_points]
    
    # Ajusta reta para z vs x
    ln_a, b = least_squares_line(x_points, z_points)
    a = math.exp(ln_a)
    
    return a, b


# ============= FUNÇÕES DE AVALIAÇÃO =============
def evaluate_line(x, a, b):
    """Avalia a reta y = a + b*x em um ponto x."""
    return a + b * x


def evaluate_parabola(x, a, b, c):
    """Avalia a parábola y = a + b*x + c*x² em um ponto x."""
    return a + b * x + c * x ** 2


def evaluate_exponential(x, a, b):
    """Avalia a exponencial y = a * e^(b*x) em um ponto x."""
    return a * math.exp(b * x)


# ============= FUNÇÕES DE ERRO =============
def calculate_residuals(x_points, y_points, y_predicted):
    """Calcula os resíduos: y_real - y_predito."""
    return [y_points[i] - y_predicted[i] for i in range(len(x_points))]


def sum_squared_error(residuals):
    """Calcula a soma dos quadrados dos resíduos (SSE)."""
    return sum(r ** 2 for r in residuals)


def root_mean_squared_error(residuals):
    """Calcula o erro quadrático médio (RMSE)."""
    n = len(residuals)
    if n == 0:
        return 0.0
    return math.sqrt(sum_squared_error(residuals) / n)


def mean_absolute_error(residuals):
    """Calcula o erro médio absoluto (MAE)."""
    n = len(residuals)
    if n == 0:
        return 0.0
    return sum(abs(r) for r in residuals) / n


def coefficient_of_determination(y_points, y_predicted):
    """
    Calcula o coeficiente de determinação (R²).
    R² = 1 - (SS_res / SS_tot)
    """
    y_mean = sum(y_points) / len(y_points)
    ss_res = sum((y_points[i] - y_predicted[i]) ** 2 for i in range(len(y_points)))
    ss_tot = sum((y_points[i] - y_mean) ** 2 for i in range(len(y_points)))
    
    if abs(ss_tot) < 1e-12:
        return 0.0
    
    return 1.0 - (ss_res / ss_tot)
