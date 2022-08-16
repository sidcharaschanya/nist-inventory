import tkinter as tk
import tkinter.ttk as ttk
import ttkthemes as themes
from PIL import ImageTk, Image
import sys
import student_window as stw
import teacher_window as tw
import admin_window as aw
import shortlist_window as shw


# Grouping main menu attributes into a class that inherits from tkinter top level
class MainMenu(tk.Toplevel):
    def __init__(self, login_window, role):
        self.wd = ""
        # noinspection SpellCheckingInspection
        if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
            # noinspection PyProtectedMember
            self.wd = f"{sys._MEIPASS}/"

        # Assign given parameters to class variables
        self.login_window = login_window
        self.role = role

        # Create root main menu by calling superclass constructor
        super().__init__()
        self.title(f"{self.role} Main Menu")
        self.geometry("900x600")
        self.protocol("WM_DELETE_WINDOW", self.logout)

        # Set main menu theme
        self.main_style = themes.ThemedStyle(self)
        self.main_style.set_theme("arc")

        # Create main frame inside main menu
        self.main_frame = ttk.Frame(self)

        # Create top frame inside main frame
        self.frame_top = ttk.Frame(self.main_frame)

        # Create school logo for top frame
        self.img_school_logo = ImageTk.PhotoImage(Image.open(f"{self.wd}images/school-logo.png").resize((160, 98)))
        self.lbl_school_logo = ttk.Label(self.frame_top, image=self.img_school_logo)

        # Create middle frame inside main frame
        self.frame_middle = ttk.Frame(self.main_frame)

        # Create buttons with images for each inventory category for middle frame
        self.img_physics = ImageTk.PhotoImage(Image.open(f"{self.wd}images/physics.png").resize((150, 150)))
        self.btn_physics = ttk.Button(self.frame_middle, image=self.img_physics, command=self.physics)
        self.img_glassware = ImageTk.PhotoImage(Image.open(f"{self.wd}images/glassware.png").resize((150, 150)))
        self.btn_glassware = ttk.Button(self.frame_middle, image=self.img_glassware, command=self.glassware)
        self.img_biology = ImageTk.PhotoImage(Image.open(f"{self.wd}images/biology.png").resize((150, 150)))
        self.btn_biology = ttk.Button(self.frame_middle, image=self.img_biology, command=self.biology)
        self.img_chemistry = ImageTk.PhotoImage(Image.open(f"{self.wd}images/chemistry.png").resize((150, 150)))
        self.btn_chemistry = ttk.Button(self.frame_middle, image=self.img_chemistry, command=self.chemistry)
        self.img_misc = ImageTk.PhotoImage(Image.open(f"{self.wd}images/misc.png").resize((150, 150)))
        self.btn_misc = ttk.Button(self.frame_middle, image=self.img_misc, command=self.misc)
        self.img_bacteria = ImageTk.PhotoImage(Image.open(f"{self.wd}images/bacteria.png").resize((150, 150)))
        self.btn_bacteria = ttk.Button(self.frame_middle, image=self.img_bacteria, command=self.bacteria)
        self.img_algae = ImageTk.PhotoImage(Image.open(f"{self.wd}images/algae.png").resize((150, 150)))
        self.btn_algae = ttk.Button(self.frame_middle, image=self.img_algae, command=self.algae)
        self.img_enzymes = ImageTk.PhotoImage(Image.open(f"{self.wd}images/enzymes.png").resize((150, 150)))
        self.btn_enzymes = ttk.Button(self.frame_middle, image=self.img_enzymes, command=self.enzymes)
        self.img_posters = ImageTk.PhotoImage(Image.open(f"{self.wd}images/posters.png").resize((150, 150)))
        self.btn_posters = ttk.Button(self.frame_middle, image=self.img_posters, command=self.posters)
        self.img_chemicals = ImageTk.PhotoImage(Image.open(f"{self.wd}images/chemicals.png").resize((150, 150)))
        self.btn_chemicals = ttk.Button(self.frame_middle, image=self.img_chemicals, command=self.chemicals)

        # Create bottom frame inside main frame
        self.frame_bottom = ttk.Frame(self.main_frame)

        # Create login and shortlist buttons for bottom frame
        self.btn_logout = ttk.Button(self.frame_bottom, text="Logout", command=self.logout)
        self.btn_shortlist = ttk.Button(self.frame_bottom, text="Open Shortlist", command=self.open_shortlist)

        # Grid all GUI elements
        self.grid_widgets()

        # Add main frame to main menu
        self.main_frame.pack(expand=1, fill="both")

    def grid_widgets(self):
        # Configure rows and columns in main frame
        for i in range(8):
            self.main_frame.rowconfigure(i, weight=1)
        for i in range(1):
            self.main_frame.columnconfigure(i, weight=1)

        # Grid top, middle, and bottom frames in main frame
        self.frame_top.grid(row=0, column=0, sticky="nsew")
        self.frame_middle.grid(row=1, column=0, rowspan=6, sticky="nsew")
        self.frame_bottom.grid(row=7, column=0, sticky="nsew")

        # Add school logo to top frame
        self.lbl_school_logo.pack(expand=1, anchor="center", padx=5, pady=5)

        # Configure rows and columns in middle frame
        for i in range(2):
            self.frame_middle.rowconfigure(i, weight=1)
        for i in range(5):
            self.frame_middle.columnconfigure(i, weight=1)

        # Grid inventory category buttons in middle frame
        self.btn_physics.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.btn_glassware.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        self.btn_biology.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)
        self.btn_chemistry.grid(row=0, column=3, sticky="nsew", padx=5, pady=5)
        self.btn_misc.grid(row=0, column=4, sticky="nsew", padx=5, pady=5)
        self.btn_bacteria.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        self.btn_algae.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
        self.btn_enzymes.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)
        self.btn_posters.grid(row=1, column=3, sticky="nsew", padx=5, pady=5)
        self.btn_chemicals.grid(row=1, column=4, sticky="nsew", padx=5, pady=5)

        # Configure rows and columns in bottom frame
        for i in range(2):
            self.frame_bottom.rowconfigure(i, weight=1)
        for i in range(1):
            self.frame_bottom.columnconfigure(i, weight=1)

        # Grid shortlist and logout buttons in bottom frame
        self.btn_shortlist.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.btn_logout.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

    def physics(self):
        # Initialize appropriate window given user, passing root main menu object and chosen category
        if self.role == "Student":
            stw.StudentWindow(self, "Physics Equipment")
        if self.role == "Teacher":
            tw.TeacherWindow(self, "Physics Equipment")
        if self.role == "Admin":
            aw.AdminWindow(self, "Physics Equipment")

    def glassware(self):
        # Initialize appropriate window given user, passing root main menu object and chosen category
        if self.role == "Student":
            stw.StudentWindow(self, "Glassware")
        if self.role == "Teacher":
            tw.TeacherWindow(self, "Glassware")
        if self.role == "Admin":
            aw.AdminWindow(self, "Glassware")

    def biology(self):
        # Initialize appropriate window given user, passing root main menu object and chosen category
        if self.role == "Student":
            stw.StudentWindow(self, "Biology Equipment")
        if self.role == "Teacher":
            tw.TeacherWindow(self, "Biology Equipment")
        if self.role == "Admin":
            aw.AdminWindow(self, "Biology Equipment")

    def chemistry(self):
        # Initialize appropriate window given user, passing root main menu object and chosen category
        if self.role == "Student":
            stw.StudentWindow(self, "Chemistry Equipment")
        if self.role == "Teacher":
            tw.TeacherWindow(self, "Chemistry Equipment")
        if self.role == "Admin":
            aw.AdminWindow(self, "Chemistry Equipment")

    def misc(self):
        # Initialize appropriate window given user, passing root main menu object and chosen category
        if self.role == "Student":
            stw.StudentWindow(self, "Miscellaneous")
        if self.role == "Teacher":
            tw.TeacherWindow(self, "Miscellaneous")
        if self.role == "Admin":
            aw.AdminWindow(self, "Miscellaneous")

    def bacteria(self):
        # Initialize appropriate window given user, passing root main menu object and chosen category
        if self.role == "Student":
            stw.StudentWindow(self, "Bacteria")
        if self.role == "Teacher":
            tw.TeacherWindow(self, "Bacteria")
        if self.role == "Admin":
            aw.AdminWindow(self, "Bacteria")

    def algae(self):
        # Initialize appropriate window given user, passing root main menu object and chosen category
        if self.role == "Student":
            stw.StudentWindow(self, "Algae")
        if self.role == "Teacher":
            tw.TeacherWindow(self, "Algae")
        if self.role == "Admin":
            aw.AdminWindow(self, "Algae")

    def enzymes(self):
        # Initialize appropriate window given user, passing root main menu object and chosen category
        if self.role == "Student":
            stw.StudentWindow(self, "Enzymes")
        if self.role == "Teacher":
            tw.TeacherWindow(self, "Enzymes")
        if self.role == "Admin":
            aw.AdminWindow(self, "Enzymes")

    def posters(self):
        # Initialize appropriate window given user, passing root main menu object and chosen category
        if self.role == "Student":
            stw.StudentWindow(self, "Posters")
        if self.role == "Teacher":
            tw.TeacherWindow(self, "Posters")
        if self.role == "Admin":
            aw.AdminWindow(self, "Posters")

    def chemicals(self):
        # Initialize appropriate window given user, passing root main menu object and chosen category
        if self.role == "Student":
            # noinspection SpellCheckingInspection
            stw.StudentWindow(self, "Chemical Stocklist")
        if self.role == "Teacher":
            # noinspection SpellCheckingInspection
            tw.TeacherWindow(self, "Chemical Stocklist")
        if self.role == "Admin":
            # noinspection SpellCheckingInspection
            aw.AdminWindow(self, "Chemical Stocklist")

    def open_shortlist(self):
        # Initialize shortlist window, passing root main menu object and user
        shw.ShortlistWindow(self, self.role)

    def logout(self):
        # Destroy root main menu
        self.destroy()

        # Show root login window
        self.login_window.wm_deiconify()
