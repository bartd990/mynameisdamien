from PizzaCalculatorApp import PizzaCalculatorApp
import kivy
kivy.require("1.11.1")
class PizzaCalculatorMain:
    print("Kivy Version: " kivy.version)
    if(__name__ == "__main__"):
        PizzaCalculatorApp().run()