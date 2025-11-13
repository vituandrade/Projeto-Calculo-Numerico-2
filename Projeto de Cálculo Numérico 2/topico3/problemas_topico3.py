# problemas_topico3.py
# Define o trê problema do Tópico 3 (Interpolação Polinomial / Mínimos Quadrados)

from .interpolacao_polinomial import (
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
        print(f"Erro no ajuste parabolico: {e}")
    
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
