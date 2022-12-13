import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image
import os
import sys
import pyautogui

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    width = 1920
    height = 1080

    screenwidth, screenheight = pyautogui.size()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # configure window
        self.title("Vapor")
        self.geometry(f"{self.screenwidth}x{self.screenheight}")
        # self.attributes('-fullscreen', True)

        # create navbar
        self.sidebar_frame = customtkinter.CTkFrame(self, width=self.screenwidth, height=70, corner_radius=0)
        self.sidebar_frame.place(x=0, y=0)

        # load logo
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.vapor_logo = customtkinter.CTkImage(Image.open(current_path + "/assets/logos/vapor_logo.png"), size=(50, 50))
        self.vapor_logo_label = customtkinter.CTkLabel(self.sidebar_frame, image=self.vapor_logo, text=" ")
        self.vapor_logo_label.place(x=10, y=10)
        self.vapor_label = customtkinter.CTkLabel(self.sidebar_frame, text="Vapor TM", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.vapor_label.place(x=70, y=20)

        # Game Browser
        content_width = self.screenwidth - 100
        self.coming_soon_frame = customtkinter.CTkFrame(self, width=content_width, height=400)
        self.coming_soon_frame.place(x=50, y=100)


if __name__ == "__main__":
    app = App()
    app.mainloop()
