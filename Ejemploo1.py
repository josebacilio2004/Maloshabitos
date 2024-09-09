def Multiplicacion(multiplicando, multiplicador):
    producto = multiplicando * multiplicador
    return producto


if __name__ == "__main__":
    multiplicando = float(input("Multiplicando: "))
    multiplicador = float(input("Multiplicador: "))
    resultado = Multiplicacion(multiplicando, multiplicador)
    print(f"RESULTADO: {multiplicando}  *  {multiplicador}= {resultado} ")
