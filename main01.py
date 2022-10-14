import kivy   
#from kivy.app import App  
import kivy 
from kivy.app import App
from kivy.uix.gridlayout import GridLayout 
from kivy.config import Config



class CalcGridLayout(GridLayout):

    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = 'Erro não pode dividir com 0'

class CalculatorApp(App):

    def build(self):

        return CalcGridLayout()


calcApp =CalculatorApp()
calcApp.run()