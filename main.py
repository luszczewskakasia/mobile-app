from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.selectioncontrol import MDCheckbox
from kivy.uix.textinput import TextInput


from kivy.lang import Builder

class MainApp(MDApp):
    print(kivymd.__version__)
    #constructure
    screen = MDScreen()
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"            
        return Builder.load_file("main.kv")

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
