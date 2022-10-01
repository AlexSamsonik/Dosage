from kivy.app import App
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout

Config.set("kivy", "keyboard_mode", "system")


def get_dosages(mass):
    paracetamol_240 = str(round(15 * mass / 1000 * 5 / 240, 2))
    paracetamol_120 = str(round(15 * mass / 1000 * 5 / 120, 2))
    ibuprofen_200 = str(round(10 * mass / 1000 * 5 / 200, 2))
    ibuprofen_100 = str(round(10 * mass / 1000 * 5 / 100, 2))
    return {"paracetamol_240": paracetamol_240,
            "paracetamol_120": paracetamol_120,
            "ibuprofen_200": ibuprofen_200,
            "ibuprofen_100": ibuprofen_100}


class Container(GridLayout):
    def calculate(self):
        try:
            mass = int(self.text_input.text)
        except:
            mass = 0

        dosages = get_dosages(mass)

        self.paracetamol_240.text = dosages.get("paracetamol_240")
        self.paracetamol_120.text = dosages.get("paracetamol_120")
        self.ibuprofen_200.text = dosages.get("ibuprofen_200")
        self.ibuprofen_100.text = dosages.get("ibuprofen_100")


class DosageApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    DosageApp().run()
