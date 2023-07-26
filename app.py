import tkinter as tk
from tkinter import messagebox

class InteriorApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Interior Destiny風水!!!!")
        self.current_screen = None
        self.layout = None
        self.destiny = None

    def start(self):
        self.show_title()

    def show_title(self):
        self.clear_screen()
        self.current_screen = "Title"
        title_label = tk.Label(self.window, text="Interior Destiny", font=("Arial", 24))
        title_label.pack(pady=20)
        select_layout_button = tk.Button(self.window, text="Select Layout", command=self.select_layout)
        select_layout_button.pack()

    def select_layout(self):
        self.clear_screen()
        self.current_screen = "SelectLayout"
        instruction_label = tk.Label(self.window, text="Select a layout:")
        instruction_label.pack(pady=10)
        layout_options = ["1K", "2DK", "3LDK"]
        for layout in layout_options:
            layout_button = tk.Button(self.window, text=layout, command=lambda l=layout: self.show_layout_details(l))
            layout_button.pack(pady=5)

    def show_layout_details(self, selected_layout):
        self.clear_screen()
        self.current_screen = "LayoutDetails"
        self.layout = selected_layout
        layout_label = tk.Label(self.window, text=f"Selected Layout: {selected_layout}", font=("Arial", 16))
        layout_label.pack(pady=20)
        select_destiny_button = tk.Button(self.window, text="Select Destiny", command=self.select_destiny)
        select_destiny_button.pack()

    def select_destiny(self):
        self.clear_screen()
        self.current_screen = "SelectDestiny"
        instruction_label = tk.Label(self.window, text="Select a destiny:")
        instruction_label.pack(pady=10)
        destiny_options = ["金運", "恋愛運", "仕事運"]
        for destiny in destiny_options:
            destiny_button = tk.Button(self.window, text=destiny, command=lambda d=destiny: self.show_confirmation(d))
            destiny_button.pack(pady=5)

    def show_confirmation(self, selected_destiny):
        self.clear_screen()
        self.current_screen = "Confirmation"
        self.destiny = selected_destiny
        confirmation_label = tk.Label(self.window, text=f"Are you sure you want to improve {selected_destiny}?", font=("Arial", 16))
        confirmation_label.pack(pady=20)
        ok_button = tk.Button(self.window, text="OK", command=self.draw_fortune)
        ok_button.pack(side=tk.LEFT, padx=10)
        return_button = tk.Button(self.window, text="Return", command=self.return_to_previous_screen)
        return_button.pack(side=tk.RIGHT, padx=10)

    def draw_fortune(self):
        self.clear_screen()
        self.current_screen = "DrawFortune"
        # Implement fortune drawing logic here (omikuji)

        # For this example, we'll display a simple message
        fortune_label = tk.Label(self.window, text="You drew a fortune!", font=("Arial", 20))
        fortune_label.pack(pady=20)
        fortune_details_button = tk.Button(self.window, text="View Fortune Details", command=self.show_fortune_details)
        fortune_details_button.pack()

    def show_fortune_details(self):
        self.clear_screen()
        self.current_screen = "FortuneDetails"
        # Implement fortune details display logic here

        # For this example, we'll display a simple message
        fortune_details_label = tk.Label(self.window, text="Fortune details will be shown here.", font=("Arial", 16))
        fortune_details_label.pack(pady=20)
        return_button = tk.Button(self.window, text="Return", command=self.return_to_previous_screen)
        return_button.pack()

    def return_to_previous_screen(self):
        if self.current_screen == "Title":
            # Do nothing as there is no previous screen
            pass
        elif self.current_screen == "SelectLayout":
            self.show_title()
        elif self.current_screen == "LayoutDetails":
            self.select_layout()
        elif self.current_screen == "SelectDestiny":
            self.show_layout_details(self.layout)
        elif self.current_screen == "Confirmation":
            self.select_destiny()
        elif self.current_screen == "DrawFortune":
            self.show_confirmation(self.destiny)
        elif self.current_screen == "FortuneDetails":
            self.draw_fortune()

    def clear_screen(self):
        for widget in self.window.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = InteriorApp()
    app.start()
    app.window.mainloop()
