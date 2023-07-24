import numpy
import kivymd
import pandas
import kivy


from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel



# class MainApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         self.theme_cls.primary_palette = "Orange"

#         return (
#             MDScreen(
#                 MDRectangleFlatButton(
#                     text="Hello, World",
#                     pos_hint={"center_x": 0.5, "center_y": 0.5},
#                 )
#             )
#         )


# MainApp().run()


class MainApp(MDApp):
    #constructure
    def build(self):
        return MDLabel(text="Hello", halign="center")
    
# if __name__ == "__main__":
MainApp().run()