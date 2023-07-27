import numpy
import kivymd
import pandas
import kivy


from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.selectioncontrol import MDCheckbox

from kivy.lang import Builder

class MainApp(MDApp):
    #constructure
    screen = MDScreen()
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("login.kv")

    def show_password(self, checkbox, value):
        if value:
            self.root.ids.password_field.password = False
            self.root.ids.password_text.text = "Hide Password"
        else:
            self.root.ids.password_field.password = True
            self.root.ids.password_text.text = "Show Password"


    
if __name__ == "__main__":
    MainApp().run()
