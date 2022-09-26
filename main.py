from kivy.app import App
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout

Config.set("kivy", "keyboard_mode", "system")


def get_dosages(mass):
    paracetamol = str(round(15 * mass / 1000 * 5 / 240, 2))
    ibuprofen = str(round(10 * mass / 1000 * 5 / 100, 2))
    return {"paracetamol": paracetamol, "ibuprofen": ibuprofen}


class Container(GridLayout):
    def calculate(self):
        try:
            mass = int(self.text_input.text)
        except:
            mass = 0

        dosages = get_dosages(mass)

        self.paracetamol.text = dosages.get("paracetamol")
        self.ibuprofen.text = dosages.get("ibuprofen")


class DosageApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    DosageApp().run()
