from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from ManagerScreen import ManagerScreen
from WelcomeScreen import WelcomeScreen
from CostomerScreen import CostomerScreen

class PizzaCalculatorApp(App):
    screen_manager = ScreenManager()
    def build(self):
        self.title = "Bart's Pizzeria"
        Window.size = (1200, 600)
        