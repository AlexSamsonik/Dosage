from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class Container(GridLayout):
    pass


class DosageApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    DosageApp().run()
