"""
Author: FENG YUAN
Time: 30 minutes

Pseudo Code:
1. Import Kivy modules and StringProperty.
2. Create MilesConverterApp class.
3. Build the UI.
4. Implement mile-to-km conversion.
5. Increment miles.
6. Validate miles.

"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

__author__ = 'Lindsay Ward'
MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    output_km = StringProperty()  # Declare output_km as a StringProperty

    def build(self):
        """Build the Kivy app from the kv file and initialize output."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.handle_calculate()
        return self.root

    def handle_calculate(self):
        """Convert miles to km and update the output label."""
        miles = self.get_validated_miles()
        km = miles * MILES_TO_KM
        self.output_km = str(km)

    def handle_increment(self, change):
        """Increment miles and update the UI."""
        miles = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(miles)
        self.handle_calculate()

    def get_validated_miles(self):
        """Validate and return the miles input as a float."""
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0


if __name__ == "__main__":
    MilesConverterApp().run()
