import kivy
from kivy.app import App
from kivy.uix.label import Label

class BioCareApp(App):

    def build(self):
        return Label(text='Sample text')
