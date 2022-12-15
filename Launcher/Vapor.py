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

    current_path = os.path.dirname(os.path.realpath(__file__))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # configure window
        self.title("Vapor")
        self.geometry(f"{self.width}x{self.height}")
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure(3, weight=1)
        # self.attributes('-fullscreen', True)

        # create navbar
        self.sidebar_frame = customtkinter.CTkFrame(self, height=70, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.sidebar_frame.grid_columnconfigure(2, weight=1)

        # load logo
        self.vapor_logo = customtkinter.CTkImage(Image.open(self.current_path + "/assets/logos/vapor_logo.png"), size=(50, 50))
        self.vapor_logo_label = customtkinter.CTkLabel(self.sidebar_frame, image=self.vapor_logo, text=" ")
        self.vapor_logo_label.grid(row=0, column=0, padx=10, pady=10)
        self.vapor_label = customtkinter.CTkLabel(self.sidebar_frame, text="Vapor TM", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.vapor_label.grid(row=0, column=1, padx=20, pady=20)

        # Coming Soon
        self.coming_soon_frame = customtkinter.CTkFrame(self, height=400)
        self.coming_soon_frame.grid(row=1, column=0, columnspan=2, padx=50, pady=50, sticky="nsew")
        self.coming_soon_frame.grid_columnconfigure((1,2,3,4), weight=0)
        self.coming_soon_frame.grid_columnconfigure(5, weight=1)
        self.coming_soon_frame.grid_rowconfigure((1,2), weight=1)

        self.coming_soon_label = customtkinter.CTkLabel(self.coming_soon_frame, text="Coming Soon", font=customtkinter.CTkFont(size=16, weight="bold"))
        self.coming_soon_label.grid(row=0, column=0, padx=10, pady=10)

        self.grand_theft_horse = customtkinter.CTkImage(Image.open(self.current_path + "/assets/Game_Preview/grand_theft_horse.jpg"), size=(140, 140))
        self.grand_theft_horse_label = customtkinter.CTkLabel(self.coming_soon_frame, image=self.grand_theft_horse, text=" ")
        self.grand_theft_horse_label.grid(row=1, column=0, padx=10, pady=10)

        self.halo = customtkinter.CTkImage(Image.open(self.current_path + "/assets/Game_Preview/halo.jpg"), size=(140, 140))
        self.halo_label = customtkinter.CTkLabel(self.coming_soon_frame, image=self.halo, text=" ")
        self.halo_label.grid(row=1, column=1, padx=10, pady=10)

        self.retail_manager_13 = customtkinter.CTkImage(Image.open(self.current_path + "/assets/Game_Preview/retail_manager_13.jpg"), size=(140, 140))
        self.retail_manager_13_label = customtkinter.CTkLabel(self.coming_soon_frame, image=self.retail_manager_13, text=" ")
        self.retail_manager_13_label.grid(row=1, column=2, padx=10, pady=10)

        self.ruined_friendship = customtkinter.CTkImage(Image.open(self.current_path + "/assets/Game_Preview/ruined_friendship.jpg"), size=(140, 140))
        self.ruined_friendship_label = customtkinter.CTkLabel(self.coming_soon_frame, image=self.ruined_friendship, text=" ")
        self.ruined_friendship_label.grid(row=1, column=3, padx=10, pady=10)

        # Available Games
        self.games_frame = customtkinter.CTkFrame(self, height=400)
        self.games_frame.grid(row=2, column=0, columnspan=2, padx=50, pady=50, sticky="nsew")
        self.games_frame.grid_columnconfigure((1,2,3,4), weight=0)
        self.games_frame.grid_columnconfigure(5, weight=1)
        self.games_frame.grid_rowconfigure((1,2), weight=1)

        self.games_label = customtkinter.CTkLabel(self.games_frame, text="Available Games", font=customtkinter.CTkFont(size=16, weight="bold"))
        self.games_label.grid(row=0, column=0, padx=10, pady=10)

        self.cookie_clicker = customtkinter.CTkImage(Image.open(self.current_path + "/assets/Game_Preview/cookie_clicker.jpg"), size=(140, 140))
        self.cookie_clicker_label = customtkinter.CTkButton(self.games_frame, command=self.open_cookie_clicker, image=self.cookie_clicker, text=" ")
        self.cookie_clicker_label.grid(row=1, column=0, padx=10, pady=10)

    def open_cookie_clicker(self):
            os.startfile(self.current_path + "/CookieClicker/CookieClicker.exe")


if __name__ == "__main__":
    app = App()
    app.mainloop()
