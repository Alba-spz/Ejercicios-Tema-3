""" Al ejecutar el codigo se abre una ventana con la Torre de Hanói, donde se muestran las piedras y las torres.
Puede que la ventana no se abra de inmediato, pero en la barra de tareas sí se verá la ventana."""

import tkinter as tk
import time

# ==========================
# Pedir al jugador el número de piedras
# ==========================

while True:
    try:
        n = int(input("🧱 ¿Cuántas piedras quieres mover? (3 a 8 recomendado): "))
        if n >= 1:
            break
        else:
            print("⚠️ Por favor ingresa un número mayor a 0.")
    except ValueError:
        print("⚠️ Eso no es un número válido. Intenta de nuevo.")


# ==========================
# Juego con interfaz gráfica
# ==========================

class TorreDeHanoi:
    def __init__(self, master, num_piedras):
        self.master = master
        self.num_piedras = num_piedras
        self.canvas = tk.Canvas(master, width=600, height=300, bg="white")
        self.canvas.pack()

        self.movimientos = 0  # ← inicializamos el contador de movimientos

        self.torres = {"A": [], "B": [], "C": []}
        self.posiciones = {"A": 100, "B": 300, "C": 500}

        for i in range(num_piedras, 0, -1):
            self.torres["A"].append(i)

        self.dibujar_torres()
        self.master.after(1000, lambda: self.mover_piedras(num_piedras, "A", "B", "C"))

    def dibujar_torres(self):
        self.canvas.delete("all")

        # Dibujar bases y postes
        for x in self.posiciones.values():
            self.canvas.create_rectangle(x - 50, 250, x + 50, 260, fill="black")
            self.canvas.create_line(x, 50, x, 250, fill="gray", width=4)

        # Dibujar piedras
        colores = ["#E57373", "#81C784", "#64B5F6", "#FFD54F", "#BA68C8", "#FF8A65", "#A1887F", "#4DB6AC"]
        for torre, piedras in self.torres.items():
            x_base = self.posiciones[torre]
            for nivel, piedra in enumerate(piedras):  # Dibuja desde la base (nivel 0)
                width = piedra * 20
                x0 = x_base - width // 2
                y0 = 240 - nivel * 20
                x1 = x_base + width // 2
                y1 = y0 + 15
                color = colores[(piedra - 1) % len(colores)]
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
                self.canvas.create_text((x0 + x1) / 2, y0 + 7, text=str(piedra), fill="white")

        self.master.update()
        time.sleep(0.4)

    def mover_piedras(self, n, origen, auxiliar, destino):
        if n == 1:
            piedra = self.torres[origen].pop()
            self.torres[destino].append(piedra)
            self.movimientos += 1  # ← sumamos movimiento
            print(f"📦 Movimiento {self.movimientos}: Mover piedra {piedra} de {origen} a {destino}")
            self.dibujar_torres()
            if len(self.torres[destino]) == self.num_piedras:
                print(f"\n🎉 ¡Puzzle resuelto en {self.movimientos} movimientos!")
                print(f"📍 Columna final ({destino}): {self.torres[destino]}")
        else:
            self.mover_piedras(n - 1, origen, destino, auxiliar)
            self.mover_piedras(1, origen, auxiliar, destino)
            self.mover_piedras(n - 1, auxiliar, origen, destino)



# ==========================
# Iniciar interfaz gráfica
# ==========================

if __name__ == "__main__":
    root = tk.Tk()
    root.title(f"Torre de Hanói 🏺 | Piedras: {n}")
    app = TorreDeHanoi(root, num_piedras=n)
    root.mainloop()
