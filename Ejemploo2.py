def OperCombinadas(Factor1, Factor2, Sumando):
    Resultado = Factor1 * Factor2 + Sumando
    return Resultado

if __name__ == "__main__":
    factor1 = float(input("Factor 1: "))
    factor2 = float(input("Factor 2: "))
    sumando = float(input("Sumando: "))
    resultado = OperCombinadas(factor1, factor2, sumando)
    print(f" {factor1} * {factor2} + {sumando} = {resultado}")

