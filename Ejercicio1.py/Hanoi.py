class Hanoi:
    def __init__(self, num_piedras):
        # Inicializa la clase con el número de piedras (discos) que tendrá el problema.
        self.num_piedras = num_piedras
        # Lista para registrar los movimientos realizados.
        self.movimientos = []
        # Diccionario que representa las torres A, B y C. 
        # La torre "A" comienza con todas las piedras apiladas en orden descendente (de mayor a menor).
        self.torres = {"A": list(range(num_piedras, 0, -1)), "B": [], "C": []}

    def resolver(self):
        # Método principal para resolver el problema de las Torres de Hanoi.
        # Llama al método recursivo _mover_piedras para mover todas las piedras de "A" a "C".
        self._mover_piedras(self.num_piedras, "A", "B", "C")
        # Devuelve la lista de movimientos realizados.
        return self.movimientos

    def _mover_piedras(self, n, origen, auxiliar, destino):
        # Método recursivo para mover 'n' piedras de una torre a otra.
        if n == 1:
            # Caso base: si solo hay una piedra, se mueve directamente de la torre de origen a la torre destino.
            piedra = self.torres[origen].pop()              # Saca la piedra de la torre de origen.
            self.torres[destino].append(piedra)             # Coloca la piedra en la torre destino.
            # Registra el movimiento realizado (piedra, torre origen, torre destino).
            self.movimientos.append((piedra, origen, destino))
        else:
            # Paso 1: Mueve las 'n-1' piedras de la torre de origen a la torre auxiliar.
            self._mover_piedras(n - 1, origen, destino, auxiliar)
            # Paso 2: Mueve la piedra más grande (la número 'n') de la torre de origen a la torre destino.
            self._mover_piedras(1, origen, auxiliar, destino)
            # Paso 3: Mueve las 'n-1' piedras de la torre auxiliar a la torre destino.
            self._mover_piedras(n - 1, auxiliar, origen, destino)

    def estado_final(self):
        # Devuelve el estado actual de las torres (A, B, C) después de resolver el problema.
        return self.torres


