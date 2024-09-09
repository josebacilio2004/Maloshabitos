# Función para calcular el área de un rectángulo
def CalcularAreaRectangulo(Altura, Base):
    areaRectangulo = Altura * Base
    return areaRectangulo


# Función para calcular el área de un triángulo
def CalcularAreaTriangulo(Base, Altura):
    areaTriangulo = 0.5 * Base * Altura
    return areaTriangulo


# Función principal
if __name__ == "__main__":
    dimension1Rect = float(input("Dimensión 1 Rectángulo: "))
    dimension2Rect = float(input("Dimensión 2 Rectángulo: "))
    dimension3Tri = float(input("Dimensión 1 Triángulo: "))
    dimension4Tri = float(input("Dimensión 2 Triángulo: "))

    rect_area = CalcularAreaRectangulo(dimension1Rect, dimension2Rect)
    print("Área del rectángulo:", rect_area)

    tri_area = CalcularAreaTriangulo(dimension3Tri, dimension4Tri)
    print("Área del triángulo:", tri_area)
