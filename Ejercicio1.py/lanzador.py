import tkinter as tk
import time
from Hanoi import Hanoi

class TorreDeHanoiVisual:
    def __init__(self, master, num_piedras):
        self.master = master  # Referencia a la ventana principal.
        self.canvas = tk.Canvas(master, width=600, height=300, bg="white")  # Crea un lienzo para dibujar.
        self.canvas.pack()  # Muestra el lienzo en la ventana.

        self.hanoi = Hanoi(num_piedras)  # Instancia de la lógica del juego (no incluida en el código mostrado).
        # Inicializa las torres con las piedras en la torre "A".
        self.torres = {"A": list(range(num_piedras, 0, -1)), "B": [], "C": []}
        self.movimientos = self.hanoi.resolver()  # Obtiene la lista de movimientos para resolver el puzzle.
        self.mov_index = 0  # Índice del movimiento actual.
        # Posiciones en el lienzo para las torres.
        self.posiciones = {"A": 100, "B": 300, "C": 500}
        # Colores para las piedras.
        self.colores = ["#E57373", "#81C784", "#64B5F6", "#FFD54F", "#BA68C8", "#FF8A65", "#A1887F", "#4DB6AC"]

        self.dibujar_torres()  # Dibuja las torres iniciales.
        self.master.after(1000, self.animar)  # Inicia la animación después de 1 segundo.

    def dibujar_torres(self):
        self.canvas.delete("all")  # Limpia el lienzo.
        # Dibuja las bases y postes de las torres.
        for x in self.posiciones.values():
            self.canvas.create_rectangle(x - 50, 250, x + 50, 260, fill="black")  # Base de la torre.
            self.canvas.create_line(x, 50, x, 250, fill="gray", width=4)  # Poste de la torre.

        # Dibuja las piedras en cada torre.
        for torre, piedras in self.torres.items():
            x_base = self.posiciones[torre]  # Posición de la torre en el lienzo.
            for nivel, piedra in enumerate(piedras):
                width = piedra * 20  # Ancho de la piedra proporcional a su tamaño.
                x0 = x_base - width // 2  # Coordenada izquierda.
                y0 = 240 - nivel * 20  # Coordenada superior.
                x1 = x_base + width // 2  # Coordenada derecha.
                y1 = y0 + 15  # Coordenada inferior.
                color = self.colores[(piedra - 1) % len(self.colores)]  # Color de la piedra.
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)  # Dibuja la piedra.
                self.canvas.create_text((x0 + x1) / 2, y0 + 7, text=str(piedra), fill="white")  # Etiqueta con el número.
        self.master.update()  # Actualiza la ventana.

    def animar(self):
        if self.mov_index < len(self.movimientos):  # Si quedan movimientos por realizar.
            # Obtiene el movimiento actual.
            piedra, origen, destino = self.movimientos[self.mov_index]
            print(f"📦 Movimiento {self.mov_index + 1}: Piedra {piedra} de {origen} a {destino}")
            self.torres[origen].pop()  # Quita la piedra de la torre de origen.
            self.torres[destino].append(piedra)  # Añade la piedra a la torre de destino.
            self.mov_index += 1  # Avanza al siguiente movimiento.
            self.dibujar_torres()  # Redibuja las torres.
            self.master.after(500, self.animar)  # Espera 500 ms antes de realizar el siguiente movimiento.
        else:
            # Cuando se completan todos los movimientos.
            print("\n🎉 ¡Puzzle resuelto!")
            print(f"📍 Columna final: {list(self.torres['C'])}")  # Muestra las piedras en la torre final.
            print(f"🧮 Total de movimientos: {len(self.movimientos)}")  # Muestra el total de movimientos realizados.