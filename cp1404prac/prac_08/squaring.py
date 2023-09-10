"""
Author:FENG YUAN
Time: 28 minutes

Pseudo Code:
1. Import Kivy modules.
2. Create SquareNumberApp class.
3. Build UI from 'squaring.kv'.
4. Handle square calculations.

"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Lindsay Ward'


class SquareNumberApp(App):
    """SquareNumberApp is a Kivy App for squaring a number."""
    def build(self):
        """Build the Kivy app from the kv file and set window size and title."""
        Window.size = (400, 200)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """Handle the calculation and output the result to the label widget."""
        try:
            result = float(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "Invalid input"


if __name__ == "__main__":
    SquareNumberApp().run()
