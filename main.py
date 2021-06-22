from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import Object

class MyGridLayout(Widget):
    pass

class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()