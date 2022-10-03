"""Main module to run application."""

from typing import Dict

from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivymd.theming import ThemeManager

Config.set("kivy", "keyboard_mode", "system")


def get_dosages(mass) -> Dict[str, str]:
    """Function which calculate dosage depending on weight in grams.

    :param mass: mass of children in grams
    :return: Dictionary
    """

    paracetamol_240 = str(round(15 * mass / 1000 * 5 / 240, 2))
    paracetamol_120 = str(round(15 * mass / 1000 * 5 / 120, 2))
    ibuprofen_200 = str(round(10 * mass / 1000 * 5 / 200, 2))
    ibuprofen_100 = str(round(10 * mass / 1000 * 5 / 100, 2))
    return {"paracetamol_240": paracetamol_240,
            "paracetamol_120": paracetamol_120,
            "ibuprofen_200": ibuprofen_200,
            "ibuprofen_100": ibuprofen_100}


class Container(GridLayout):
    """Class which collect all Layout."""

    def calculate(self):
        """Function which call when end-user click on button 'Calculate'."""
        try:
            mass = int(self.text_input.text)
        except ValueError:
            mass = 0

        dosages = get_dosages(mass)

        self.paracetamol_240.text = dosages.get("paracetamol_240")
        self.paracetamol_120.text = dosages.get("paracetamol_120")
        self.ibuprofen_200.text = dosages.get("ibuprofen_200")
        self.ibuprofen_100.text = dosages.get("ibuprofen_100")


class DosageApp(MDApp):
    """Application class"""

    theme_cls = ThemeManager()
    title = "Dosage"

    def build(self):
        """Initializes the application"""
        self.theme_cls.theme_style = "Dark"
        return Container()


if __name__ == '__main__':
    DosageApp().run()
