""""""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class ListFriendsNames(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.friends = ["Michael", "Adam", "Lauren", "Alison", "The Abdominal Snowman", "The Man on the Moon"]

    def build(self):
        self.root = Builder.load_file("my_names.kv")
        return self.root

    def create_widgets(self):
        for friend in self.friends:
            temp_label = Label(text=friend)
            self.root.ids.friends_list.add_widget(temp_label)

ListFriendsNames().run()
# ListFriendsNames.create_widgets()
