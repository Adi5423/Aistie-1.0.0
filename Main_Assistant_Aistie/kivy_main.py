from kivymd.app import MDApp
from kivy.uix.label import Label


class AI_App(MDApp):
    def build(self):
        return Label(text="Welcome to AI_App",halign = "center")
    
if __name__ == "__main__":
    AI_App().run()