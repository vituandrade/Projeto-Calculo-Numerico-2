import numpy as np
from metodos_integracao import trapezio, simpson

def problema3():
    print("\n=== TOPICO 4 - PROBLEMA 3 ===")
    print("Calculo da area da secao do trecho mais largo de um navio\n")

    # Distâncias verticais (iguais: 0.4 m)
    y = np.array([3.00, 2.92, 2.75, 2.52, 2.30, 1.84, 0.92, 0.00])
    x = np.arange(0, len(y)) * 0.4  # espaçamento constante de 0.4 m

    area_trap = trapezio(x, y)
    # Para simpson, usar número par de subintervalos -> len(y)-1 = 7 (ímpar), remover último ponto se necessário
    area_simp = simpson(x[:-1], y[:-1])

    print(f"Area aproximada pela Regra dos Trapezios: {area_trap:.4f} m2")
    print(f"Area aproximada pela Regra de Simpson: {area_simp:.4f} m2")

    print("\nObs.: As regras foram aplicadas com dx = 0,4 m e dados da figura do navio.")
