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
    Regra de Simpson Composta (1/3)
    """
    n = len(x) - 1
    if n % 2 != 0:
        raise ValueError("O numero de subintervalos deve ser par para a Regra de Simpson.")
    h = (x[-1] - x[0]) / n
    soma = y[0] + y[-1] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-2:2])
    return (h / 3) * soma
