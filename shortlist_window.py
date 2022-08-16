import tkinter as tk
import tkinter.ttk as ttk
import ttkthemes as themes
import os


# Grouping shortlist window attributes into a class that inherits from tkinter top level
class ShortlistWindow(tk.Toplevel):
    def __init__(self, main_menu, role):
        # Assign given parameters to class variables
        self.main_menu = main_menu
        self.role = role

        # Create root shortlist window as child of main menu by calling superclass constructor
        super().__init__(self.main_menu)
        self.title(f"{self.role} Shortlist Window")
        self.geometry("900x600")

        # Set shortlist window theme
        self.shortlist_style = themes.ThemedStyle(self)
        self.shortlist_style.set_theme("arc")

        # Create main frame inside shortlist window
        self.shortlist_frame = ttk.Frame(self)

        # Create refresh and remove buttons for main frame
        self.btn_refresh = ttk.Button(self.shortlist_frame, text="Refresh Shortlist",
                                      command=self.refresh)
        self.btn_remove = ttk.Button(self.shortlist_frame, text="Remove Selected Item(s) From Shortlist",
                                     command=self.remove)

        # Create tree frame inside main frame
        self.frame_tree = ttk.Frame(self.shortlist_frame)

        # Create shortlist tree for tree frame using number of column headings
        self.col_heads = ["Category", "ID", "Name"]
        self.tree_shortlist = ttk.Treeview(self.frame_tree, columns=[f"#{i}" for i in range(1, len(self.col_heads))])

        # Create list containing tree column widths that scale according to shortlist items
        self.widths = []

        # Loop through each column heading
        for i in range(len(self.col_heads)):
            # Set initial column width to zero
            width = 0

            # Loop through items in shortlist.txt
            for item in ShortlistWindow.read():
                # Assign new value to column width if length of data exceeds it
                if len(item[i]) > width:
                    width = len(item[i])

            if len(self.col_heads[i]) > width:
                # Append length of column heading to widths if current column width is smaller
                self.widths.append(len(self.col_heads[i]) * 11)
            else:
                # Else append current column width to widths
                self.widths.append(width * 11)
        self.widths[0] += 10
        self.widths[1] += 11

        # Set tree columns using list of widths and column headings
        for i in range(len(self.col_heads)):
            self.tree_shortlist.column(f"#{i}", width=self.widths[i])
            self.tree_shortlist.heading(f"#{i}", text=self.col_heads[i])

        # Create vertical and horizontal scrollbars for tree
        self.vsb = ttk.Scrollbar(self.frame_tree, orient="vertical", command=self.tree_shortlist.yview)
        self.hsb = ttk.Scrollbar(self.frame_tree, orient="horizontal", command=self.tree_shortlist.xview)
        self.tree_shortlist.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)

        # Grid all GUI elements
        self.grid_widgets()

        # Load shortlist into tree from shortlist.txt
        self.refresh()

        # Add main frame to shortlist window
        self.shortlist_frame.pack(expand=1, fill="both")

    def grid_widgets(self):
        # Configure rows and columns in main frame
        for i in range(12):
            self.shortlist_frame.rowconfigure(i, weight=1)
        for i in range(1):
            self.shortlist_frame.columnconfigure(i, weight=1)

        # Grid tree frame in main frame
        self.frame_tree.grid(row=0, column=0, rowspan=10, sticky="nsew", padx=5, pady=5)

        # Grid refresh and remove buttons in main frame
        self.btn_refresh.grid(row=10, column=0, sticky="nsew", padx=5, pady=5)
        self.btn_remove.grid(row=11, column=0, sticky="nsew", padx=5, pady=5)

        # Configure rows and columns in tree frame
        self.frame_tree.rowconfigure(0, weight=999)
        self.frame_tree.rowconfigure(1, weight=1)
        self.frame_tree.columnconfigure(0, weight=999)
        self.frame_tree.columnconfigure(1, weight=1)

        # Grid shortlist tree and scrollbars in tree frame
        self.tree_shortlist.grid(row=0, column=0, sticky="nsew")
        self.vsb.grid(row=0, column=1, rowspan=2, sticky="nsew")
        self.hsb.grid(row=1, column=0, sticky="nsew")

    @staticmethod
    def read():
        try:
            # Open shortlist.txt and read lines
            shortlist_file = open(os.path.join(os.path.expanduser("~"), "Documents", "shortlist.txt"), "r")
            file_items = shortlist_file.readlines()

            # Store read lines in 2D list
            shortlist_items = []
            for i in range(0, len(file_items), 3):
                shortlist_items.append([file_items[i][:-1], file_items[i + 1][:-1], file_items[i + 2][:-1]])

            # Close shortlist.txt
            shortlist_file.close()

            # Return 2D list
            return shortlist_items
        except FileNotFoundError:
            return []

    def refresh(self):
        # Remove existing items from shortlist tree
        self.tree_shortlist.delete(*self.tree_shortlist.get_children())

        # Insert items from shortlist.txt into shortlist tree
        for item in ShortlistWindow.read():
            self.tree_shortlist.insert("", tk.END, text=item[0], values=item[1:])

    def remove(self):
        # Store selected items to remove from shortlist in 2D list
        items_to_remove = []
        for selection in self.tree_shortlist.selection():
            item_to_remove = [self.tree_shortlist.item(selection, "text")]
            item_to_remove.extend(list(self.tree_shortlist.item(selection, "values")))
            items_to_remove.append(item_to_remove)

        # Determine new shortlist items by removing selected items from existing shortlist
        shortlist_items = ShortlistWindow.read()
        for item in items_to_remove:
            shortlist_items.remove(item)

        # Open shortlist.txt and overwrite with new shortlist items
        shortlist_file = open(os.path.join(os.path.expanduser("~"), "Documents", "shortlist.txt"), "w")
        for item in shortlist_items:
            shortlist_file.write(f"{item[0]}\n{item[1]}\n{item[2]}\n")

        # Close shortlist.txt
        shortlist_file.close()

        # Refresh shortlist tree after updating shortlist.txt
        self.refresh()
