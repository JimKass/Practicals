"""

"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button

class PeopleAndAges(App):
    def __init__(self):
        super().__init__()
        self.people_file_name = "people.csv"
        self.people = {}


    def build(self):
        self.root = Builder.load_file("people_and_ages.kv")

    def create_widgets(self):
        in_file = open(self.people_file_name)
        in_file_content = in_file.readlines()
        for person in in_file_content:
            name, age = person.strip().split(",")
            self.people[name] = age
        for name in self.people.keys():
            temp_button = Button(text=name)
            temp_button.bind(on_release=self.output_age)
            self.root.ids.widget_field.add_widget(temp_button)

    def clear_widgets(self):
        pass

    def output_age(self, instance):
        name = instance.text
        self.root.ids.output_label.text = self.people[name]

PeopleAndAges().run()