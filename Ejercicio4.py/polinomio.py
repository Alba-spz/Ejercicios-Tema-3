class Polinomio:

    # Constructor de la clase. Inicializa un polinomio con un diccionario de términos.
    # El diccionario tiene como clave el exponente y como valor el coeficiente.
    def __init__(self, terminos=None):
        self.terminos = terminos if terminos else {}  # Si no se pasan términos, inicializa un diccionario vacío.

    # Método especial para convertir el polinomio en una representación en cadena.
    def __str__(self):
        if not self.terminos:  # Si no hay términos, el polinomio es 0.
            return "0"
        partes = []  # Lista para almacenar las partes del polinomio como cadenas.
        for exp in sorted(self.terminos, reverse=True):  # Ordena los exponentes de mayor a menor.
            coef = self.terminos[exp]  # Obtiene el coeficiente del término.
            if coef == 0:  # Si el coeficiente es 0, lo omite.
                continue
            if exp == 0:  # Si el exponente es 0, solo muestra el coeficiente.
                partes.append(f"{coef}")
            elif exp == 1:  # Si el exponente es 1, muestra coeficiente seguido de "x".
                partes.append(f"{coef}x")
            else:  # Para exponentes mayores a 1, muestra coeficiente seguido de "x^exponente".
                partes.append(f"{coef}x^{exp}")
        # Une las partes con " + " y reemplaza "+ -" por "- " para manejar signos negativos.
        return " + ".join(partes).replace("+ -", "- ")

    # Método para restar otro polinomio.
    def restar(self, otro):
        # Crea un nuevo polinomio copiando los términos del actual.
        resultado = Polinomio(self.terminos.copy())
        for exp, coef in otro.terminos.items():  # Itera sobre los términos del polinomio a restar.
            # Resta los coeficientes de los términos con el mismo exponente.
            resultado.terminos[exp] = resultado.terminos.get(exp, 0) - coef
            if resultado.terminos[exp] == 0:  # Si el coeficiente resultante es 0, elimina el término.
                del resultado.terminos[exp]
        return resultado  # Devuelve el polinomio resultante.

    # Método para dividir el polinomio actual entre otro polinomio.
    def dividir(self, otro):
        if not otro.terminos:  # Verifica que el divisor no sea un polinomio vacío.
            raise ValueError("No se puede dividir entre un polinomio vacío.")
        resultado = Polinomio()  # Polinomio para almacenar el cociente.
        dividendo = self.terminos.copy()  # Copia los términos del dividendo.

        # Mientras el dividendo no esté vacío y el mayor exponente del dividendo sea mayor o igual al del divisor.
        while dividendo and max(dividendo) >= max(otro.terminos):
            exp_dividendo = max(dividendo)  # Mayor exponente del dividendo.
            exp_divisor = max(otro.terminos)  # Mayor exponente del divisor.
            coef_dividendo = dividendo[exp_dividendo]  # Coeficiente del término con mayor exponente en el dividendo.
            coef_divisor = otro.terminos[exp_divisor]  # Coeficiente del término con mayor exponente en el divisor.
            nuevo_exp = exp_dividendo - exp_divisor  # Calcula el nuevo exponente.
            nuevo_coef = coef_dividendo / coef_divisor  # Calcula el nuevo coeficiente.
            resultado.terminos[nuevo_exp] = nuevo_coef  # Agrega el término al cociente.

            # Actualiza el dividendo restando el producto del divisor por el término recién calculado.
            for exp, coef in otro.terminos.items():
                exp_actual = exp + nuevo_exp  # Ajusta el exponente.
                dividendo[exp_actual] = dividendo.get(exp_actual, 0) - coef * nuevo_coef
                if dividendo[exp_actual] == 0:  # Si el coeficiente resultante es 0, elimina el término.
                    del dividendo[exp_actual]
        return resultado  # Devuelve el cociente.

    # Método para eliminar un término del polinomio dado su exponente.
    def eliminar_termino(self, exponente):
        if exponente in self.terminos:  # Verifica si el término existe.
            del self.terminos[exponente]  # Elimina el término.

    # Método para verificar si existe un término con un exponente dado.
    def existe_termino(self, exponente):
        return exponente in self.terminos  # Devuelve True si el término existe, False en caso contrario.

