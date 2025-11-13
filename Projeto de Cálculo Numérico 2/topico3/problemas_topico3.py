# problemas_topico3.py
# Define os três problemas do Tópico 3 (Interpolação Polinomial / Mínimos Quadrados)

from .interpolacao_polinomial import (
    lagrange_interpolation,
    newton_interpolation,
    print_newton_differences_table,
    least_squares_line,
    least_squares_parabola,
    least_squares_exponential,
    evaluate_line,
    evaluate_parabola,
    evaluate_exponential,
    root_mean_squared_error,
    mean_absolute_error,
    coefficient_of_determination,
    calculate_residuals
)


# ========== PROBLEMA 1: LEI DE MOORE ==========
def problema1():
    """
    Lei de Moore: Número de transistores em chips ao longo dos anos.
    Dados: dados de transistores de 1971 a 2011
    Objetivo: Interpolar e ajustar a lei de Moore com exponencial.
    """
    print("\n" + "="*70)
    print("PROBLEMA 1: LEI DE MOORE")
    print("="*70)
    
    # Dados históricos: (ano, número de transistores em milhões)
    anos = [1971, 1974, 1978, 1982, 1985, 1989, 1993, 1997, 2000, 2003, 2007, 2011]
    transistores = [2.3, 5, 29, 120, 275, 1180, 3100, 7500, 42000, 220000, 1720000, 4600000]
    
    print("\nDados historicos da Lei de Moore:")
    print("-" * 50)
    print(f"{'Ano':<10} {'Transistores (milhoes)':<20}")
    print("-" * 50)
    for ano, trans in zip(anos, transistores):
        print(f"{ano:<10} {trans:<20}")
    
    # Teste: interpolação em um ano intermediário
    ano_teste = 1980
    print(f"\n--- Interpolacao para o ano {ano_teste} ---")
    
    # Lagrange
    resultado_lagrange = lagrange_interpolation(anos, transistores, ano_teste)
    print(f"Lagrange:  {resultado_lagrange:.2f} milhoes de transistores")
    
    # Newton
    resultado_newton = newton_interpolation(anos, transistores, ano_teste)
    print(f"Newton:    {resultado_newton:.2f} milhoes de transistores")
    
    # Mostrar tabela de diferenças divididas
    print_newton_differences_table(anos, transistores)
    
    # Ajuste exponencial (normalizado para evitar overflow)
    print(f"\n--- Ajuste Exponencial y = a * e^(b*x) ---")
    try:
        # Normaliza anos para evitar números muito grandes
        anos_norm = [ano - 1970 for ano in anos]  # Começar de 0
        a, b = least_squares_exponential(anos_norm, transistores)
        print(f"Coeficientes encontrados:")
        print(f"  a = {a:.6e}")
        print(f"  b = {b:.6f}")
        print(f"  (Nota: anos normalizados com base 1970)")
        
        # Calcula valores preditos
        try:
            y_predicted = [evaluate_exponential(ano_n, a, b) for ano_n in anos_norm]
            
            # Análise de erro
            residuals = calculate_residuals(anos_norm, transistores, y_predicted)
            rmse = root_mean_squared_error(residuals)
            mae = mean_absolute_error(residuals)
            r2 = coefficient_of_determination(transistores, y_predicted)
            
            print(f"\nMetricas de erro:")
            print(f"  RMSE (Erro Quadratico Medio): {rmse:.6e}")
            print(f"  MAE  (Erro Medio Absoluto):   {mae:.6e}")
            print(f"  R^2   (Coeficiente de Determinacao): {r2:.6f}")
            
            # Predição para um ano futuro
            ano_futuro = 2020
            ano_futuro_norm = ano_futuro - 1970
            pred_futuro = evaluate_exponential(ano_futuro_norm, a, b)
            print(f"\nPredicao para {ano_futuro}: {pred_futuro:.2e} transistores")
        except OverflowError:
            print("Aviso: A exponencial produz valores muito grandes (overflow).")
            print("Este e esperado para a Lei de Moore, indicando crescimento exponencial acelerado.")
        
    except ValueError as e:
        print(f"Erro: {e}")


# ========== PROBLEMA 2: QUEDA DE VOLTAGEM ==========
def problema2():
    """
    Queda de Voltagem em um resistor.
    Dados: Medições de voltagem em diferentes pontos
    Objetivo: Interpolar usando Lagrange e Newton
    """
    print("\n" + "="*70)
    print("PROBLEMA 2: QUEDA DE VOLTAGEM")
    print("="*70)
    
    # Dados: (distância em metros, voltagem em volts)
    distancia = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    voltagem = [10.0, 8.7, 7.2, 5.5, 4.0, 2.3]
    
    print("\nMedicoes de voltagem vs distancia:")
    print("-" * 50)
    print(f"{'Distancia (m)':<15} {'Voltagem (V)':<15}")
    print("-" * 50)
    for dist, volt in zip(distancia, voltagem):
        print(f"{dist:<15.2f} {volt:<15.2f}")
    
    # Ponto de teste
    dist_teste = 2.5
    print(f"\n--- Interpolacao na distancia de {dist_teste} m ---")
    
    # Lagrange
    resultado_lagrange = lagrange_interpolation(distancia, voltagem, dist_teste)
    print(f"Lagrange:  {resultado_lagrange:.4f} V")
    
    # Newton
    resultado_newton = newton_interpolation(distancia, voltagem, dist_teste)
    print(f"Newton:    {resultado_newton:.4f} V")
    
    # Tabela de diferenças divididas
    print_newton_differences_table(distancia, voltagem)
    
    # Outro ponto
    dist_teste2 = 1.5
    print(f"\n--- Interpolacao na distancia de {dist_teste2} m ---")
    resultado_lagrange2 = lagrange_interpolation(distancia, voltagem, dist_teste2)
    resultado_newton2 = newton_interpolation(distancia, voltagem, dist_teste2)
    print(f"Lagrange:  {resultado_lagrange2:.4f} V")
    print(f"Newton:    {resultado_newton2:.4f} V")


# ========== PROBLEMA 3: AJUSTE DE CURVAS ==========
def problema3():
    """
    Ajuste de curvas com reta, parábola e exponencial.
    Dados: Dados de um experimento científico
    Objetivo: Encontrar o melhor ajuste para os dados
    """
    print("\n" + "="*70)
    print("PROBLEMA 3: AJUSTE DE CURVAS (RETA, PARABOLA, EXPONENCIAL)")
    print("="*70)
    
    # Dados experimentais
    x_dados = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
    y_dados = [2.1, 4.9, 8.2, 14.3, 20.8, 30.5, 42.1, 57.0]
    
    print("\nDados experimentais:")
    print("-" * 50)
    print(f"{'x':<10} {'y':<10}")
    print("-" * 50)
    for x, y in zip(x_dados, y_dados):
        print(f"{x:<10.2f} {y:<10.2f}")
    
    # === AJUSTE LINEAR: y = a + b*x ===
    print(f"\n{'='*70}")
    print("1. AJUSTE LINEAR: y = a + b*x")
    print('='*70)
    
    try:
        a_lin, b_lin = least_squares_line(x_dados, y_dados)
        print(f"Coeficientes:")
        print(f"  a (intercepto) = {a_lin:.6f}")
        print(f"  b (inclinacao) = {b_lin:.6f}")
        print(f"\nEquacao: y = {a_lin:.6f} + {b_lin:.6f}*x")
        
        # Valores preditos
        y_pred_lin = [evaluate_line(x, a_lin, b_lin) for x in x_dados]
        
        # Estatísticas
        residuals_lin = calculate_residuals(x_dados, y_dados, y_pred_lin)
        rmse_lin = root_mean_squared_error(residuals_lin)
        mae_lin = mean_absolute_error(residuals_lin)
        r2_lin = coefficient_of_determination(y_dados, y_pred_lin)
        
        print(f"\nMetricas de erro:")
        print(f"  RMSE: {rmse_lin:.6f}")
        print(f"  MAE:  {mae_lin:.6f}")
        print(f"  R^2:   {r2_lin:.6f}")
        
    except Exception as e:
        print(f"Erro no ajuste linear: {e}")
    
    # === AJUSTE PARABOLICO: y = a + b*x + c*x^2 ===
    print(f"\n{'='*70}")
    print("2. AJUSTE PARABOLICO: y = a + b*x + c*x^2")
    print('='*70)
    
    try:
        a_par, b_par, c_par = least_squares_parabola(x_dados, y_dados)
        print(f"Coeficientes:")
        print(f"  a = {a_par:.6f}")
        print(f"  b = {b_par:.6f}")
        print(f"  c = {c_par:.6f}")
        print(f"\nEquacao: y = {a_par:.6f} + {b_par:.6f}*x + {c_par:.6f}*x^2")
        
        # Valores preditos
        y_pred_par = [evaluate_parabola(x, a_par, b_par, c_par) for x in x_dados]
        
        # Estatísticas
        residuals_par = calculate_residuals(x_dados, y_dados, y_pred_par)
        rmse_par = root_mean_squared_error(residuals_par)
        mae_par = mean_absolute_error(residuals_par)
        r2_par = coefficient_of_determination(y_dados, y_pred_par)
        
        print(f"\nMetricas de erro:")
        print(f"  RMSE: {rmse_par:.6f}")
        print(f"  MAE:  {mae_par:.6f}")
        print(f"  R^2:   {r2_par:.6f}")
        
    except Exception as e:
        print(f"Erro no ajuste parabólico: {e}")
    
    # === AJUSTE EXPONENCIAL: y = a * e^(b*x) ===
    print(f"\n{'='*70}")
    print("3. AJUSTE EXPONENCIAL: y = a * e^(b*x)")
    print('='*70)
    
    try:
        a_exp, b_exp = least_squares_exponential(x_dados, y_dados)
        print(f"Coeficientes:")
        print(f"  a = {a_exp:.6f}")
        print(f"  b = {b_exp:.6f}")
        print(f"\nEquacao: y = {a_exp:.6f} * e^({b_exp:.6f}*x)")
        
        # Valores preditos
        y_pred_exp = [evaluate_exponential(x, a_exp, b_exp) for x in x_dados]
        
        # Estatísticas
        residuals_exp = calculate_residuals(x_dados, y_dados, y_pred_exp)
        rmse_exp = root_mean_squared_error(residuals_exp)
        mae_exp = mean_absolute_error(residuals_exp)
        r2_exp = coefficient_of_determination(y_dados, y_pred_exp)
        
        print(f"\nMetricas de erro:")
        print(f"  RMSE: {rmse_exp:.6f}")
        print(f"  MAE:  {mae_exp:.6f}")
        print(f"  R^2:   {r2_exp:.6f}")
        
    except Exception as e:
        print(f"Erro no ajuste exponencial: {e}")
    
    # === COMPARACAO ===
    print(f"\n{'='*70}")
    print("RESUMO COMPARATIVO")
    print('='*70)
    print(f"{'Modelo':<15} {'RMSE':<15} {'MAE':<15} {'R^2':<15}")
    print('-'*70)
    print(f"{'Linear':<15} {rmse_lin:<15.6f} {mae_lin:<15.6f} {r2_lin:<15.6f}")
    print(f"{'Parabolico':<15} {rmse_par:<15.6f} {mae_par:<15.6f} {r2_par:<15.6f}")
    print(f"{'Exponencial':<15} {rmse_exp:<15.6f} {mae_exp:<15.6f} {r2_exp:<15.6f}")
    
    # Identificar melhor modelo
    models = {
        'Linear': r2_lin,
        'Parabolico': r2_par,
        'Exponencial': r2_exp
    }
    best_model = max(models, key=models.get)
    print(f"\nMelhor modelo (maior R^2): {best_model}")
