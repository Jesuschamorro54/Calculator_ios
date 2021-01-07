# coding; utf-8

__autor__ = "Jesus Chamorro"

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
import math
import re


class WindowSimple(GridLayout):

    def on_press_bt(self):

        ventana.root_window.remove_widget(ventana.root)
        ventana.root = OtherFunction()
        ventana.root_window.add_widget(ventana.root)


class OtherFunction(GridLayout):

    def on_press_bt(self):
        ventana.root_window.remove_widget(ventana.root)
        ventana.root = WindowSimple()
        ventana.root_window.add_widget(ventana.root)


class CalculadoraApp(App):
    icon = 'calculator_41.ico'
    title = "..."

    def build(self):
        return WindowSimple()

    # El método evaluate se utiliza para evaluar la operacion en caso que presente errores
    @staticmethod
    def evaluate(parameter):
        try:
            try:
                print ("Resolviendo Operación...")
                parameter = re.sub(u"\u00F7", "/", parameter)
                parameter = re.sub(u"\u00D7", "*", parameter)
                parameter = str(eval(parameter))
            except:
                print("Analizando raíz...")
                parameter = re.sub(u"\u221A", " ", parameter)
                parameter = math.sqrt(int(parameter))
        except:
            print ("¡ERROR!")
            return parameter
        else:
            print("¡Resuelto!")
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


if __name__ == "__main__":
    ventana = CalculadoraApp()
    Window.size = 300, 450
    ventana.run()
