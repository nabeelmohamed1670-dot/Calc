from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class CalcApp(App):
    def build(self):
        return BoxLayout() # loads calculator.kv automatically

if __name__ == '__main__':
    CalcApp().run()
