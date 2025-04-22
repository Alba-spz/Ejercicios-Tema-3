""" Al ejecutar el código se abre una ventana gráfica en tkinter que muestra la Torre de Hanói y permite visualizar el movimiento de las piedras.
Puede que no se te abra directamente. Se puede ver si pinchas en la pagina que se abre en la vbarra de herramientas de abajo en el ordenador """

from lanzador import TorreDeHanoiVisual  # Importa la clase TorreDeHanoiVisual desde el módulo lanzador.
import tkinter as tk  # Importa la biblioteca tkinter para crear interfaces gráficas.

# Función para pedir al usuario el número de piedras que desea mover.
def pedir_piedras():
    while True:  # Bucle infinito para seguir pidiendo un valor válido.
        try:
            # Solicita al usuario un número entero.
            n = int(input("🧱 ¿Cuántas piedras quieres mover? (3 a 8 recomendado): "))
            if n >= 1:  # Verifica que el número sea mayor o igual a 1.
                return n  # Devuelve el número válido.
            else:
                print("⚠️ Por favor ingresa un número mayor a 0.")  # Mensaje de error si el número es menor a 1.
        except ValueError:
            # Captura errores si el usuario ingresa algo que no sea un número.
            print("⚠️ Eso no es un número válido. Intenta de nuevo.")

# Punto de entrada principal del programa.
if __name__ == "__main__":
    num_piedras = pedir_piedras()  # Llama a la función para obtener el número de piedras.
    root = tk.Tk()  # Crea la ventana principal de la interfaz gráfica.
    root.title(f"Torre de Hanói 🏺 | Piedras: {num_piedras}")  # Establece el título de la ventana.
    app = TorreDeHanoiVisual(root, num_piedras)  # Crea una instancia de la clase TorreDeHanoiVisual.
    root.mainloop()  # Inicia el bucle principal de la interfaz gráfica.