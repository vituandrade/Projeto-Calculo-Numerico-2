# problemas_topico3.py
# Define o trê problema do Tópico 3 (Interpolação Polinomial / Mínimos Quadrados)

# Teste da questão 3
# x:    0      1.5     2.6     4.2     6   8.2  10      11.4
# f(x): 18      13      11      9      6    4    2       1

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
    Dados: Inseridos pelo usuário
    Objetivo: Encontrar o melhor ajuste para os dados
    """
    print("\n" + "="*70)
    print("PROBLEMA 3: AJUSTE DE CURVAS (RETA, PARABOLA, EXPONENCIAL)")
    print("="*70)
    
    # Entrada de dados do usuário
    print("\n--- ENTRADA DE DADOS ---")
    print("Digite os pares (x, f(x)) para análise de regressão.")
    print("Quando terminar, deixe x em branco e pressione ENTER.\n")
    
    x_dados = []
    y_dados = []
    contador = 1
    
    while True:
        try:
            x_input = input(f"Ponto {contador} - Digite x (ou ENTER para terminar): ").strip()
            if x_input == "":
                break
            
            x_val = float(x_input)
            y_input = input(f"Ponto {contador} - Digite f(x): ").strip()
            y_val = float(y_input)
            
            x_dados.append(x_val)
            y_dados.append(y_val)
            contador += 1
        except ValueError:
            print("Erro: Digite valores numericos validos!\n")
            continue
    
    if len(x_dados) < 2:
        print("Erro: É necessário pelo menos 2 pontos para fazer regressão!")
        return
    
    print("\nDados experimentais:")
    print("-" * 50)
    print(f"{'x':<10} {'y':<10}")
    print("-" * 50)
    for x, y in zip(x_dados, y_dados):
        print(f"{x:<10.2f} {y:<10.2f}")
    
    # Inicializar variáveis para evitar UnboundLocalError
    rmse_lin = mae_lin = r2_lin = None
    rmse_par = mae_par = r2_par = None
    rmse_exp = mae_exp = r2_exp = None
    
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
        print(f"  Raiz quadrada do erro medio (RMSE): {rmse_lin:.6f}")
        print(f"  Erro absoluto medio (MAE):  {mae_lin:.6f}")
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
        print(f"  Raiz quadrada do erro medio (RMSE): {rmse_par:.6f}")
        print(f"  Erro absoluto medio (MAE):  {mae_par:.6f}")
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
        print(f"  Raiz quadrada do erro medio (RMSE): {rmse_exp:.6f}")
        print(f"  Erro absoluto medio (MAE):  {mae_exp:.6f}")
        print(f"  R^2:   {r2_exp:.6f}")
        
    except Exception as e:
        print(f"Erro no ajuste exponencial: {e}")
    
    # === COMPARACAO ===
    print(f"\n{'='*70}")
    print("RESUMO COMPARATIVO")
    print('='*70)
    print(f"{'Modelo':<15} {'RMSE (EMQ)':<15} {'MAE (EAM)':<15} {'R^2':<15}")
    print('-'*70)
    
    # Exibir resultados apenas se foram calculados
    if rmse_lin is not None:
        print(f"{'Linear':<15} {rmse_lin:<15.6f} {mae_lin:<15.6f} {r2_lin:<15.6f}")
    else:
        print(f"{'Linear':<15} {'(falhou)':<15} {'(falhou)':<15} {'(falhou)':<15}")
    
    if rmse_par is not None:
        print(f"{'Parabolico':<15} {rmse_par:<15.6f} {mae_par:<15.6f} {r2_par:<15.6f}")
    else:
        print(f"{'Parabolico':<15} {'(falhou)':<15} {'(falhou)':<15} {'(falhou)':<15}")
    
    if rmse_exp is not None:
        print(f"{'Exponencial':<15} {rmse_exp:<15.6f} {mae_exp:<15.6f} {r2_exp:<15.6f}")
    else:
        print(f"{'Exponencial':<15} {'(falhou)':<15} {'(falhou)':<15} {'(falhou)':<15}")
    
    # Identificar melhor modelo (apenas entre os que convergiram)
    models = {}
    if r2_lin is not None:
        models['Linear'] = r2_lin
    if r2_par is not None:
        models['Parabolico'] = r2_par
    if r2_exp is not None:
        models['Exponencial'] = r2_exp
    
    if models:
        best_model = max(models, key=models.get)
        print(f"\nMelhor modelo (maior R^2): {best_model}")
    else:
        print("\nNenhum modelo convergiu com sucesso!")
