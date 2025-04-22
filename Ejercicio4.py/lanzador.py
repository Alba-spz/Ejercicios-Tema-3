from polinomio import Polinomio  # Importa la clase Polinomio desde el archivo polinomio.py

def main():
    # Ejemplo de uso de la clase Polinomio
    p1 = Polinomio({2: 3, 1: 4, 0: -5})  # Crea un polinomio 3x^2 + 4x - 5
    p2 = Polinomio({1: 2, 0: 1})         # Crea un polinomio 2x + 1

    # Imprime los polinomios creados
    print("Polinomio 1:", p1)  # Muestra "3x^2 + 4x - 5"
    print("Polinomio 2:", p2)  # Muestra "2x + 1"

    # Realiza la resta de los dos polinomios
    resta = p1.restar(p2)  # Resta p2 de p1
    print("Resta:", resta)  # Muestra el resultado de la resta

    # Realiza la división de los dos polinomios
    division = p1.dividir(p2)  # Divide p1 entre p2
    print("División:", division)  # Muestra el cociente de la división

    # Elimina un término del polinomio p1
    p1.eliminar_termino(1)  # Elimina el término con exponente 1 (4x)
    print("Polinomio 1 después de eliminar término x^1:", p1)  # Muestra el polinomio actualizado

    # Verifica si existe un término con exponente 2 en p1
    existe = p1.existe_termino(2)  # Comprueba si el término x^2 está presente
    print("¿Existe el término x^2 en Polinomio 1?", existe)  # Muestra True o False según el caso