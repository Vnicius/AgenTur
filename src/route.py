
class Route():

    def __init__(self, distancia):
        self.distancia = distancia
        self.delay_calculator = None
    
    def set_delay_calculator(self, delay_calculator):
        self.delay_calculator = delay_calculator
        self.delay_calculator.treinar()

    def prever(self, dia, hora, fluxo):
        return self.delay_calculator.prever(dia, hora, fluxo)

    def __repr__(self):
        return "Distancia: " + str(self.distancia) + "\n" \
                + "Delay: " + str(self.delay_calculator) + "\n"