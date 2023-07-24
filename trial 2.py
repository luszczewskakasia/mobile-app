import numpy
import kivymd
import pandas
import kivy


from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder

class MainApp(MDApp):
    #constructure
    screen = MDScreen()
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("login.kv")

    # def show_password(self, touch):
    #     password_field = self.root.ids.password_field
    #     if password_field.password:
    #         password_field.password = False
    #         password_field.password_mask = ""
    #     else:
    #         password_field.password = True 
        
    #     return 
    
if __name__ == "__main__":
    MainApp().run()



# #kod ze stacka
# class MyMDTextField(MDTextField):
#     password_mode = BooleanProperty(True)

#     def on_touch_down(self, touch):
#         if self.collide_point(*touch.pos):
#             if self.icon_right:
#                 # icon position based on the KV code for MDTextField
#                 icon_x = (self.width + self.x) - (self._lbl_icon_right.texture_size[1]) - dp(8)
#                 icon_y = self.center[1] - self._lbl_icon_right.texture_size[1] / 2
#                 if self.mode == "rectangle":
#                     icon_y -= dp(4)
#                 elif self.mode != 'fill':
#                     icon_y += dp(8)

#                 # not a complete bounding box test, but should be sufficient
#                 if touch.pos[0] > icon_x and touch.pos[1] > icon_y:
#                     if self.password_mode:
#                         self.icon_right = 'eye'
#                         self.password_mode = False
#                         self.password = self.password_mode
#                     else:
#                         self.icon_right = 'eye-off'
#                         self.password_mode = True
#                         self.password = self.password_mode

#                     # try to adjust cursor position
#                     cursor = self.cursor
#                     self.cursor = (0,0)
#                     Clock.schedule_once(partial(self.set_cursor, cursor))
#         return super(MyMDTextField, self).on_touch_down(touch)

#     def set_cursor(self, pos, dt):
#         self.cursor = pos