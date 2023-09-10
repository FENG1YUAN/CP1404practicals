"""
Author: FENG YUAN
Time: 2023-09-10

Pseud Code:
1. Import Kivy modules and Label widget.
2. Create DynamicLabelsApp class.
3. Initialize names list.
4. Build the UI.
5. Create and add labels dynamically.

"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        """Initialize DynamicLabelsApp with a list of names."""
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Dave", "Eve"]

    def build(self):
        """Load the Kivy file and populate labels."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create and add label widgets for each name."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


if __name__ == '__main__':
    DynamicLabelsApp().run()
