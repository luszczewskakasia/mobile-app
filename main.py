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
        self.root.ids.report.text = f"Issue reported!"
    
    def clear(self):
        self.root.ids.report.text = f"Report an issue"
        self.root.ids.name.text = ""
        self.root.ids.last_name.text = ""
        self.root.ids.email.text = ""
        self.root.ids.location.text = ""
        self.root.ids.description.text = ""

if __name__ == "__main__":
    MainApp().run()


