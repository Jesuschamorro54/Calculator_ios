from kivy.app import App
from kivy.core.window import Window
import re


class CalculadoraApp(App):
    icon = 'calculator_41.ico'
    title = "..."

    # El método evaluate se utiliza para evaluar la operacion en caso que presente errores
    @staticmethod
    def evaluate(parameter):
        try:
            parameter = re.sub(u"\u00F7", "/", parameter)
            parameter = str(eval(parameter))
        except:
            return parameter
        else:
            return parameter

    # el método ini se utiliza para saber cuando colocar en la pantalla el numero cero (nada digitado)
    @staticmethod
    def ini(parameter, sing):
        if parameter == "0":
            if sing is not None:
                parameter = "0"
                return parameter
            else:
                parameter = ""
                return parameter
        else:
            if sing is not None:
                if len(parameter) == 1:
                    parameter = "0"
                    return parameter
                else:
                    parameter = parameter[:-1]
                    return parameter
            else:
                return parameter

    def build(self):
        pass


ventana = CalculadoraApp()
Window.size = 300, 450
ventana.run()
