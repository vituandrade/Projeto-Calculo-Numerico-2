def trapezio(x, y):
    """
    Regra do Trapézio Composta
    """
    n = len(x) - 1
    h = (x[-1] - x[0]) / n
    soma = y[0] + y[-1] + 2 * sum(y[1:-1])
    return (h / 2) * soma    

def simpson(x, y):
    """
    Aplica Simpson quando possível (n par) 
    Caso contrário aplica Simpson até o penultimo e Trapézio no ultimo para complementar
    """
    n = len(x) - 1

    if n % 2 == 0:
        
        h = (x[-1] - x[0]) / n
        soma = y[0] + y[-1] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-2:2])
        return (h / 3) * soma 
    
    else:
        # simpson até o penúltimo
        area_simpson = simpson(x[:-1], y[:-1])

        # trapézio no último intervalo
        h = x[-1] - x[-2]
        area_trap = (h / 2) * (y[-2] + y[-1])
        return area_simpson + area_trap