"""
Author: FENG YUAN
Time: 20 minutes

Pseudo Code:
1. Import required Kivy modules.
2. Define BoxLayoutDemo class inheriting from App.
3. Implement build method to load the UI and set the title.
4. Implement handle_greet to change the output_label based on input_name.
5. Implement handle_clear to clear input_name and output_label.
6. Run the app.

"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """Load the UI from 'box_layout.kv' and set the title."""
        self.title = "FENG YUAN's Box Layout Demo"
        self.root = Builder.load_file('box_layout_demo.kv')
        return self.root

    def handle_greet(self):
        """Handle the greet action by updating the output_label."""
        print("greet")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Handle the clear action by clearing input_name and output_label."""
        print("clear")
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''


if __name__ == "__main__":
    BoxLayoutDemo().run()
