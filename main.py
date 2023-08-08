from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.selectioncontrol import MDCheckbox
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder


#definie the screens

class Data(Screen):
    pass

class Education(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class MainApp(MDApp):
    
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"            
        return Builder.load_file("main2.kv")

    def logger(self):
        screen = self.root.get_screen("data")
        screen.ids.report.text = f"Issue reported!"
    
    def clear(self):
        screen = self.root.get_screen("data")
        screen.ids.report.text = f"Report an issue"
        screen.ids.name.text = ""
        screen.ids.last_name.text = ""
        screen.ids.email.text = ""
        screen.ids.location.text = ""
        screen.ids.description.text = ""

if __name__ == "__main__":
    MainApp().run()


