import random

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGame(App):

    def build(self):

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        title = Label(
            text="لعبة تخمين الأرقام",
            font_size=30
        )

        layout.add_widget(title)

        name = TextInput(
            hint_text="اكتب اسمك هنا",
            multiline=False
        )

        layout.add_widget(name)

        age = TextInput(
            hint_text="كم عمرك؟",
            multiline=False
        )

        layout.add_widget(age)

        start = Button(
            text="ابدأ اللعب",
            font_size=22
        )
        start.bind(on_press=self.start_game)

        layout.add_widget(start)

        return layout

def start_game(self, instance):
    print("بدأت اللعبة")


MyGame().run()
