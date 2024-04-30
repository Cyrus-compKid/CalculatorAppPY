#Cyrus McCormick
#4-29-24
#This is my updated calculator app, it includes some more math functions as youd see on a more advanced calculator.

from kivy.app import App
from kivy.uix.widget import Widget 
from kivy.lang import Builder
from kivy.core.window import Window
import math

# Sets the window size
Window.size = (750, 800)

# Loads the kivy file
Builder.load_file('calc.kv')

class MyLayout(Widget):
    def clear(self):
        # Clears the output and sets it back to 0
        self.ids.calc_input.text = '0'

    def remove(self):
        # Handles backspacing on the calculator UI
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        self.ids.calc_input.text = prior
        
    def pos_neg(self):
        # Changes the calc input to positive or negative if clicked on
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{prior}'
            
    def button_press(self, button):
        # Will handle the button presses
        prior = self.ids.calc_input.text
        
        if "Error" in prior:
            prior = ''

        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'
            
    def dot(self):
        # Places a decimal point if clicked on
        prior = self.ids.calc_input.text
        num_list = prior.split("+")
        num_list[-1]
        if "+" in prior and "." not in num_list[-1]:
            pass
        else:
            prior = f'{prior}.'
        self.ids.calc_input.text = prior
        
    def math_sign(self, sign):
        # Will do the math calculations given the sign; + x /
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}{sign}'
    
    def equals(self):
        # Will calculate the expression on the calculator
        prior = self.ids.calc_input.text
        try:
            answer = eval(prior)
            self.ids.calc_input.text = str(answer)
        except:   
            self.ids.calc_input.text = "Error"
        
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0.0
            for number in num_list:
                answer = answer + float(number)
                
            self.ids.calc_input.text = str(answer)
    
    def square_root(self):
        # Calculates the square root of the number
        prior = self.ids.calc_input.text
        try:
            result = math.sqrt(float(prior))
            self.ids.calc_input.text = str(result)
        except ValueError:
            self.ids.calc_input.text = "Error"

    def sine(self):
        # Calculates the sine of the number
        prior = self.ids.calc_input.text
        try:
            result = math.sin(math.radians(float(prior)))
            self.ids.calc_input.text = str(result)
        except ValueError:
            self.ids.calc_input.text = "Error"

    def cosine(self):
        # Calculates the cosine of the number
        prior = self.ids.calc_input.text
        try:
            result = math.cos(math.radians(float(prior)))
            self.ids.calc_input.text = str(result)
        except ValueError:
            self.ids.calc_input.text = "Error"

    def tangent(self):
        # Calculates the tangent of the number
        prior = self.ids.calc_input.text
        try:
            result = math.tan(math.radians(float(prior)))
            self.ids.calc_input.text = str(result)
        except ValueError:
            self.ids.calc_input.text = "Error"

    def exponentiation(self):
        # Calculates the exponentiation
        prior = self.ids.calc_input.text
        try:
            result = math.exp(float(prior))
            self.ids.calc_input.text = str(result)
        except ValueError:
            self.ids.calc_input.text = "Error"

class CalculatorApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    CalculatorApp().run()
