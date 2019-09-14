from PizzaCalculatorApp import PizzaCalculatorApp
import kivy
kivy.require("1.11.1")
from kivy.core.window import Window
class PizzaCalculatorMain:
    print("Kivy Version: " kivy.version)
    
    if(__name__ == "__main__"):
        Window.fullscreen = True
        PizzaCalculatorApp().run()