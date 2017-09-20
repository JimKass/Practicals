"""

"""

from kivy.app import App
from kivy.lang import Builder
from prac_03.temperatures_v2 import fahrenheit_to_celsius
from prac_03.temperatures_v2 import celsius_to_fahrenheit

class ConvertTemperature(App):
    def build(self):
        self.root = Builder.load_file("convert_temperature.kv")

    def convert_celsius_to_fahrenheit(self):
        fahrenheit = int(self.root.ids.input_field.text)
        celsius = fahrenheit * 1.8 - 32
        self.root.ids.output_label.text = "{:.2f}".format(celsius)

    def convert_fahrenheit_to_celsius(self):
        celsius = int(self.root.ids.input_field.text)
        fahrenheit = celsius - 32 * (5 / 9)
        self.root.ids.output_label.text = "{:.2f}".format(fahrenheit)

ConvertTemperature().run()