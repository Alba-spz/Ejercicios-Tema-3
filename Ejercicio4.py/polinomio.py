class Polinomio:

    def __init__(self, terminos=None):
        self.terminos = terminos if terminos else {}

    def __str__(self):
        if not self.terminos:
            return "0"
        partes = []
        for exp in sorted(self.terminos, reverse=True):
            coef = self.terminos[exp]
            if coef == 0:
                continue
            if exp == 0:
                partes.append(f"{coef}")
            elif exp == 1:
                partes.append(f"{coef}x")
            else:
                partes.append(f"{coef}x^{exp}")
        return " + ".join(partes).replace("+ -", "- ")

    def restar(self, otro):
        resultado = Polinomio(self.terminos.copy())
        for exp, coef in otro.terminos.items():
            resultado.terminos[exp] = resultado.terminos.get(exp, 0) - coef
            if resultado.terminos[exp] == 0:
                del resultado.terminos[exp]
        return resultado

    def dividir(self, otro):
        if not otro.terminos:
            raise ValueError("No se puede dividir entre un polinomio vacío.")
        resultado = Polinomio()
        dividendo = self.terminos.copy()

        while dividendo and max(dividendo) >= max(otro.terminos):
            exp_dividendo = max(dividendo)
            exp_divisor = max(otro.terminos)
            coef_dividendo = dividendo[exp_dividendo]
            coef_divisor = otro.terminos[exp_divisor]
            nuevo_exp = exp_dividendo - exp_divisor
            nuevo_coef = coef_dividendo / coef_divisor
            resultado.terminos[nuevo_exp] = nuevo_coef
            for exp, coef in otro.terminos.items():
                exp_actual = exp + nuevo_exp
                dividendo[exp_actual] = dividendo.get(exp_actual, 0) - coef * nuevo_coef
                if dividendo[exp_actual] == 0:
                    del dividendo[exp_actual]
        return resultado

    def eliminar_termino(self, exponente):
        if exponente in self.terminos:
            del self.terminos[exponente]

    def existe_termino(self, exponente):
        return exponente in self.terminos


    


