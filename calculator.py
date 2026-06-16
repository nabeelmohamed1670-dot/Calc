from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.lang import Builder
Builder.load_file("calculator.kv")
Window.clearcolor=(0,0,0,1)
class Calculator(FloatLayout):
    def clear(self):
        content=self.ids.textarea.text
        if content=="0":
            pass
        else:
            self.ids.textarea.text="0"
    def button(self,button_content):
        content=self.ids.textarea.text
        if content=="0" or content=="Error":
            self.ids.textarea.text=""
            self.ids.textarea.text=button_content
        else:
            self.ids.textarea.text+=button_content
    def remove_last(self):
        content=self.ids.textarea.text
        if content=="0":
            pass
        else:
            self.ids.textarea.text=content[:-1]
            if self.ids.textarea.text=="":
                self.ids.textarea.text="0"
    def equal(self):
        content=self.ids.textarea.text
        answer=0.0
        try:
            answer=eval(content)
            self.ids.textarea.text=f"{answer:.4f}".rstrip("0").rstrip(".")
        except Exception:
            self.ids.textarea.text="Error"
class MainApp(App):
    def build(self):
        return Calculator()
if __name__=="__main__":
    app=MainApp()
    app.run()