import random

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGame(App):

    def build(self):

        # إنشاء الرقم السري
        self.secret_number = random.randint(1, 100)

        # التخطيط الرئيسي
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        # العنوان
        title = Label(
            text="لعبة تخمين الأرقام",
            font_size=30
        )

        layout.add_widget(title)

        # إدخال الاسم
        self.name_input = TextInput(
            hint_text="اكتب اسمك هنا",
            multiline=False
        )

        layout.add_widget(self.name_input)

        # إدخال العمر
        self.age_input = TextInput(
            hint_text="كم عمرك؟",
            multiline=False,
            input_filter="int"
        )

        layout.add_widget(self.age_input)

        # زر بدء اللعبة
        start = Button(
            text="ابدأ اللعبة",
            font_size=22
        )

        start.bind(on_press=self.start_game)

        layout.add_widget(start)

        # تعليمات اللعبة
        self.message = Label(
            text="اضغط ابدأ اللعبة",
            font_size=20
        )

        layout.add_widget(self.message)

        # مكان كتابة التخمين
        self.guess_input = TextInput(
            hint_text="خمن رقمًا من 1 إلى 100",
            multiline=False,
            input_filter="int",
            disabled=True
        )

        layout.add_widget(self.guess_input)

        # زر التخمين
        guess_button = Button(
            text="خمن",
            font_size=22,
            disabled=True
        )

        guess_button.bind(on_press=self.check_guess)

        self.guess_button = guess_button

        layout.add_widget(guess_button)

        return layout


    def start_game(self, instance):

        name = self.name_input.text

        if name == "":
            self.message.text = "اكتب اسمك أولاً"
            return

        # إنشاء رقم جديد
        self.secret_number = random.randint(1, 100)

        # تشغيل مربع التخمين
        self.guess_input.disabled = False
        self.guess_button.disabled = False

        self.guess_input.text = ""

        self.message.text = (
            "مرحبًا " + name +
            "! خمن رقمًا من 1 إلى 100"
        )


    def check_guess(self, instance):

        guess_text = self.guess_input.text

        if guess_text == "":
            self.message.text = "اكتب رقمًا أولاً"
            return

        guess = int(guess_text)

        if guess < self.secret_number:
            self.message.text = "الرقم أكبر ⬆"

        elif guess > self.secret_number:
            self.message.text = "الرقم أصغر ⬇"

        else:
            self.message.text = "🎉 أحسنت! لقد خمنت الرقم الصحيح!"

            self.guess_input.disabled = True
            self.guess_button.disabled = True


MyGame().run()
