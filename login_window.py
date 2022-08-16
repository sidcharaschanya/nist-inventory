import mysql.connector as sql
import tkinter as tk
import tkinter.messagebox as mb
import tkinter.ttk as ttk
import ttkthemes as themes
from PIL import ImageTk, Image
import sys
from user_methods import get_db_conn
import main_menu as mm


# Grouping login window attributes into a class that inherits from tkinter tk
class LoginWindow(tk.Tk):
    def __init__(self):
        self.wd = ""
        # noinspection SpellCheckingInspection
        if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
            # noinspection PyProtectedMember
            self.wd = f"{sys._MEIPASS}/"

        # Create root login window by calling superclass constructor
        super().__init__()
        self.title("Login Window")
        self.geometry("400x330")

        # Set login window theme
        self.login_style = themes.ThemedStyle(self)
        self.login_style.set_theme("arc")

        # Create main frame inside login window
        self.login_frame = ttk.Frame(self)

        # Create top frame inside main frame
        self.frame_top = ttk.Frame(self.login_frame)

        # Create school logo for top frame
        self.img_school_logo = ImageTk.PhotoImage(Image.open(f"{self.wd}images/school-logo.png").resize((160, 98)))
        self.lbl_school_logo = ttk.Label(self.frame_top, image=self.img_school_logo)

        # Create bottom frame inside main frame
        self.frame_bottom = ttk.Frame(self.login_frame)

        # Create username and password labels and entries for bottom frame
        self.lbl_username = ttk.Label(self.frame_bottom, text="Username:", anchor="center")
        self.txt_username = ttk.Entry(self.frame_bottom)
        self.lbl_password = ttk.Label(self.frame_bottom, text="Password:", anchor="center")
        self.txt_password = ttk.Entry(self.frame_bottom, show="•")

        # Create login and quit buttons for bottom frame
        self.btn_login = ttk.Button(self.frame_bottom, text="Login", command=self.login)
        self.btn_quit = ttk.Button(self.frame_bottom, text="Quit", command=self.destroy)

        # noinspection SpellCheckingInspection
        self.lbl_developer = ttk.Label(self.frame_bottom, text="© 2021 Sid (Suchit) Charaschanya", anchor="center")

        # Grid all GUI elements
        self.grid_widgets()

        # Add main frame to log in window
        self.login_frame.pack(expand=1, fill="both")

        # Run tkinter event loop
        self.mainloop()

    def grid_widgets(self):
        # Configure rows and columns in main frame
        for i in range(3):
            self.login_frame.rowconfigure(i, weight=1)
        for i in range(1):
            self.login_frame.columnconfigure(i, weight=1)

        # Grid top and bottom frames in main frame
        self.frame_top.grid(row=0, column=0, sticky="nsew")
        self.frame_bottom.grid(row=1, column=0, rowspan=2, sticky="nsew")

        # Add school logo to top frame
        self.lbl_school_logo.pack(expand=1, anchor="center", padx=5, pady=5)

        # Configure rows and columns in bottom frame
        for i in range(5):
            self.frame_bottom.rowconfigure(i, weight=1)
        for i in range(4):
            self.frame_bottom.columnconfigure(i, weight=1)

        # Grid username and password labels and entries in bottom frame
        self.lbl_username.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.txt_username.grid(row=0, column=1, columnspan=3, sticky="nsew", padx=5, pady=5)
        self.lbl_password.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        self.txt_password.grid(row=1, column=1, columnspan=3, sticky="nsew", padx=5, pady=5)

        # Grid login and quit buttons in bottom frame
        self.btn_login.grid(row=2, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
        self.btn_quit.grid(row=3, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        self.lbl_developer.grid(row=4, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

    def login(self):
        try:
            # Connect to MySQL database
            db = get_db_conn()

            # Create database cursor and fetch user login details
            cur = db.cursor()
            cur.execute("SELECT * FROM users")
            records = cur.fetchall()

            # Store fetched user login details in 2D list
            users = []
            for record in records:
                users.append(list(record))

            # Flag to indicate validity of inputted login details
            valid = False

            # Loop through user login details to determine current user
            for user in users:
                # Check if inputted login details match user login details
                if self.txt_username.get() == user[2] and self.txt_password.get() == user[3]:
                    # Change flag state
                    valid = True

                    # Hide root login window
                    self.wm_withdraw()

                    # Initialize main menu, passing root login window object and current user
                    mm.MainMenu(self, user[1])

                    # End loop
                    break

            # Display error message if flag state is unchanged
            if not valid:
                mb.showinfo("Error Logging In", "Invalid username or password.")

            # Disconnect from MySQL database
            db.close()
        except sql.Error as error:
            # Display error message if MySQL database connected failed
            mb.showinfo("Database Connection Error", str(error))


if __name__ == "__main__":
    # Initialize login window
    LoginWindow()
