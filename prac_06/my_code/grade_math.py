
from kivy.app import App
from kivy.lang import Builder

class GradeMath(App):
    def build(self):
        self.root = Builder.load_file("grade_math.kv")

    def calculate_grade(self):
        try:
            score = int(self.root.ids.input_field.text)
            if score >= 85:
                grade = 'High Distinction'
            if score >= 75:
                grade = 'Distinction'
            if score >= 65:
                grade = 'Credit'
            if score >= 50:
                grade = 'Pass'
            else:
                grade = 'Fail'
            self.root.ids.output_label.text = str(grade)
        except ValueError:
            self.root.ids.output_label.text = 'Invalid Entry'

    def clear_fields(self):
        self.root.ids.output_label.text = ''
        self.root.ids.input_field.text = ''

GradeMath().run()