"""

"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesToKiloMetres(App):
    def build(self):
        Window.size = (200, 100)
        self.root = Builder.load_file("convert_m_to_km.kv")
        return self.root

    def handle_increment(self, increment):
        try:
            number = int(self.root.ids.input_field.text)
            number += increment
            self.root.ids.input_field.text = str(number)
        except ValueError:
            self.root.ids.output_label.text = "Invalid Entry"

    def convert_m_to_km(self):
        try:
            kilometres = int(self.root.ids.input_field.text) * 1.60934
            self.root.ids.output_label.text = str(kilometres)
        except ValueError:
            self.root.ids.output_label.text = "Invalid Entry"


ConvertMilesToKiloMetres().run()