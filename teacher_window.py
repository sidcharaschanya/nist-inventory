import tkinter as tk
import tkinter.ttk as ttk
import ttkthemes as themes
from user_methods import TeacherMethods


# Grouping teacher window attributes into a class that inherits from tkinter top level
class TeacherWindow(tk.Toplevel):
    def __init__(self, main_menu, category):
        # Assign given parameters to class variables
        self.main_menu = main_menu
        self.category = category

        # Create root teacher window as child of main menu by calling superclass constructor
        super().__init__(self.main_menu)
        self.title(f"{self.category} (Teacher)")
        self.geometry("900x600")

        # Set teacher window theme
        self.teacher_style = themes.ThemedStyle(self)
        self.teacher_style.set_theme("arc")

        # Create main frame inside teacher window
        self.teacher_frame = ttk.Frame(self)

        # Create search entry and button for main frame
        self.txt_search = ttk.Entry(self.teacher_frame)
        self.btn_search = ttk.Button(self.teacher_frame, text="Search", command=self.search)

        # Create shortlist button for main frame
        self.btn_shortlist = ttk.Button(self.teacher_frame, text="Add Selected Item(s) To Shortlist",
                                        command=self.shortlist)

        # Create tree frame inside main frame
        self.frame_tree = ttk.Frame(self.teacher_frame)

        # Create search tree for tree frame using number of column headings
        self.col_heads = TeacherMethods.get_col_heads(self.category)
        self.tree_teacher = ttk.Treeview(self.frame_tree, columns=[f"#{i}" for i in range(1, len(self.col_heads))])

        # Create 2D list containing items in database by searching it, passing chosen category
        search_results = TeacherMethods.search(self.category)

        # Create list containing search tree column widths that scale according to database items
        self.widths = []

        # Loop through each column heading
        for i in range(len(self.col_heads)):
            # Set initial column width to zero
            width = 0

            # Loop through items in database
            for item in search_results:
                # Assign new value to column width if length of data exceeds it
                if len(str(item[i])) > width:
                    width = len(str(item[i]))
            if len(self.col_heads[i]) > width:
                # Append length of column heading to widths if current column width is smaller
                self.widths.append(len(self.col_heads[i]) * 11)
            else:
                # Else append current column width to widths
                self.widths.append(width * 11)
        self.widths[0] += 21

        # Set search tree columns using list of widths and column headings
        for i in range(len(self.col_heads)):
            self.tree_teacher.column(f"#{i}", width=self.widths[i])
            self.tree_teacher.heading(f"#{i}", text=self.col_heads[i])

        # Create vertical and horizontal scrollbars for search tree
        self.vsb = ttk.Scrollbar(self.frame_tree, orient="vertical", command=self.tree_teacher.yview)
        self.hsb = ttk.Scrollbar(self.frame_tree, orient="horizontal", command=self.tree_teacher.xview)
        self.tree_teacher.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)

        # Grid all GUI elements
        self.grid_widgets()

        # Load items into search tree from database
        self.search()

        # Add main frame to teacher window
        self.teacher_frame.pack(expand=1, fill="both")

    def grid_widgets(self):
        # Configure rows and columns in main frame
        for i in range(12):
            self.teacher_frame.rowconfigure(i, weight=1)
        for i in range(4):
            self.teacher_frame.columnconfigure(i, weight=1)

        # Grid tree frame in main frame
        self.frame_tree.grid(row=0, column=0, rowspan=10, columnspan=4, sticky="nsew", padx=5, pady=5)

        # Grid search entry and button in main frame
        self.txt_search.grid(row=10, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)
        self.btn_search.grid(row=10, column=3, sticky="nsew", padx=5, pady=5)

        # Grid shortlist button in main frame
        self.btn_shortlist.grid(row=11, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        # Configure rows and columns in tree frame
        self.frame_tree.rowconfigure(0, weight=999)
        self.frame_tree.rowconfigure(1, weight=1)
        self.frame_tree.columnconfigure(0, weight=999)
        self.frame_tree.columnconfigure(1, weight=1)

        # Grid search tree and scrollbars in tree frame
        self.tree_teacher.grid(row=0, column=0, sticky="nsew")
        self.vsb.grid(row=0, column=1, rowspan=2, sticky="nsew")
        self.hsb.grid(row=1, column=0, sticky="nsew")

    def search(self):
        # Remove existing items from search tree
        self.tree_teacher.delete(*self.tree_teacher.get_children())

        # Loop through items in database by searching it, passing chosen category
        for item in TeacherMethods.search(self.category):
            # Insert all items from database into search tree if search entry is empty
            if self.txt_search.get() == "":
                self.tree_teacher.insert("", tk.END, text=item[0], values=item[1:])

            # Else insert items from database containing search string
            else:
                # Flag to indicate if item from database contains search string
                valid = False

                # Loop through each value in item
                for value in item:
                    # Check if value in item contains search string by converting both to lowercase
                    if self.txt_search.get().lower() in str(value).lower():
                        # Change flag state
                        valid = True

                        # End loop
                        break

                # Insert item from database into search tree if flag state changed
                if valid:
                    self.tree_teacher.insert("", tk.END, text=item[0], values=item[1:])

    def shortlist(self):
        # Store selected items to append to shortlist in 2D list
        items = []
        for selection in self.tree_teacher.selection():
            items.append([self.tree_teacher.item(selection, "text"), self.tree_teacher.item(selection, "values")[0]])

            # Remove selection from search tree to indicate completion of shortlisting
            self.tree_teacher.selection_remove(selection)

        # Append items to shortlist, passing chosen category and items
        TeacherMethods.shortlist(self.category, items)
