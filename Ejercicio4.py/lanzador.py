from polinomio import Polinomio

def main():
    # Ejemplo de uso
    p1 = Polinomio({2: 3, 1: 4, 0: -5})  # 3x^2 + 4x - 5
    p2 = Polinomio({1: 2, 0: 1})         # 2x + 1

    print("Polinomio 1:", p1)
    print("Polinomio 2:", p2)

    # Restar
    resta = p1.restar(p2)
    print("Resta:", resta)

    # Dividir
    division = p1.dividir(p2)
    print("División:", division)

    # Eliminar término
    p1.eliminar_termino(1)
    print("Polinomio 1 después de eliminar término x^1:", p1)

    # Verificar si existe un término
    existe = p1.existe_termino(2)
    print("¿Existe el término x^2 en Polinomio 1?", existe)
