import tkinter as tk
import tkinter.messagebox as mb
import tkinter.filedialog as fd
import csv
import tkinter.ttk as ttk
import ttkthemes as themes
from user_methods import AdminMethods


# Grouping admin window attributes into a class that inherits from tkinter top level
class AdminWindow(tk.Toplevel):
    def __init__(self, main_menu, category):
        # Assign given parameters to class variables
        self.main_menu = main_menu
        self.category = category

        # Create root admin window as child of main menu by calling superclass constructor
        super().__init__(self.main_menu)
        self.title(f"{self.category} (Admin)")
        self.geometry("900x750")

        # Set admin window theme
        self.admin_style = themes.ThemedStyle(self)
        self.admin_style.set_theme("arc")

        # Create main notebook inside admin window
        self.admin_notebook = ttk.Notebook(self)

        # Create search frame inside main notebook
        self.frame_search = ttk.Frame(self.admin_notebook)
        self.admin_notebook.add(self.frame_search, text="Search Items")

        # Create search entry and button for search frame
        self.txt_search = ttk.Entry(self.frame_search)
        self.btn_search = ttk.Button(self.frame_search, text="Search", command=self.search)

        # Create shortlist button for search frame
        self.btn_shortlist = ttk.Button(self.frame_search, text="Add Selected Item(s) To Shortlist",
                                        command=self.shortlist)

        # Create search tree frame inside search frame
        self.frame_tree_search = ttk.Frame(self.frame_search)

        # Create search tree for search tree frame using number of column headings
        self.col_heads = AdminMethods.get_col_heads(self.category)
        self.tree_search = ttk.Treeview(self.frame_tree_search,
                                        columns=[f"#{i}" for i in range(1, len(self.col_heads))])

        # Create 2D list containing items in database by searching it, passing chosen category
        search_results = AdminMethods.search(self.category)

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
            self.tree_search.column(f"#{i}", width=self.widths[i])
            self.tree_search.heading(f"#{i}", text=self.col_heads[i])

        # Create vertical and horizontal scrollbars for search tree
        self.vsb_search = ttk.Scrollbar(self.frame_tree_search, orient="vertical", command=self.tree_search.yview)
        self.hsb_search = ttk.Scrollbar(self.frame_tree_search, orient="horizontal", command=self.tree_search.xview)
        self.tree_search.configure(yscrollcommand=self.vsb_search.set, xscrollcommand=self.hsb_search.set)

        # Create add frame inside main notebook
        self.frame_add = ttk.Frame(self.admin_notebook)
        self.admin_notebook.add(self.frame_add, text="Add Item")

        # Create list of column heading labels and entries inside add frame
        self.lbl_add = []
        self.txt_add = []
        for i in range(len(self.col_heads) - 1):
            self.lbl_add.append(ttk.Label(self.frame_add, text=self.col_heads[i + 1], anchor="center"))
            self.txt_add.append(ttk.Entry(self.frame_add))

        # Create add button for add frame
        self.btn_add = ttk.Button(self.frame_add, text="Add Item", command=self.add)

        # Create edit frame inside main notebook
        self.frame_edit = ttk.Frame(self.admin_notebook)
        self.admin_notebook.add(self.frame_edit, text="Edit Item")

        # Create edit combobox inside edit frame and bind selection event
        self.cmb_edit = ttk.Combobox(self.frame_edit, state="readonly")
        self.cmb_edit.bind("<<ComboboxSelected>>", self.fill_txt_edit)

        # Create list of column heading labels and entries inside edit frame
        self.lbl_edit = [ttk.Label(self.frame_edit, text=self.col_heads[0], anchor="center")]
        self.txt_edit = [ttk.Entry(self.frame_edit, state="disabled")]
        for i in range(len(self.col_heads) - 1):
            self.lbl_edit.append(ttk.Label(self.frame_edit, text=self.col_heads[i + 1], anchor="center"))
            self.txt_edit.append(ttk.Entry(self.frame_edit))

        # Create edit button inside edit frame
        self.btn_edit = ttk.Button(self.frame_edit, text="Edit Item", command=self.edit)

        # Create delete frame inside main notebook
        self.frame_delete = ttk.Frame(self.admin_notebook)
        self.admin_notebook.add(self.frame_delete, text="Delete Item")

        # Create delete combobox inside delete frame and bind selection event
        self.cmb_delete = ttk.Combobox(self.frame_delete, state="readonly")
        self.cmb_delete.bind("<<ComboboxSelected>>", self.fill_txt_delete)

        # Create list of column heading labels and entries inside delete frame
        self.lbl_delete = []
        self.txt_delete = []
        for i in range(len(self.col_heads)):
            self.lbl_delete.append(ttk.Label(self.frame_delete, text=self.col_heads[i], anchor="center"))
            self.txt_delete.append(ttk.Entry(self.frame_delete, state="disabled"))

        # Create delete button inside delete frame
        self.btn_delete = ttk.Button(self.frame_delete, text="Delete Item", command=self.delete)

        # Create import frame inside main notebook
        self.frame_import = ttk.Frame(self.admin_notebook)
        self.admin_notebook.add(self.frame_import, text="Import Items")

        # Create open csv button inside import frame
        self.btn_open_csv = ttk.Button(self.frame_import, text="Open CSV File", command=self.open_csv)

        # Create import all and import selected buttons inside import frame
        self.btn_import_all = ttk.Button(self.frame_import, text="Import All Items", command=self.import_all)
        self.btn_import_selected = ttk.Button(self.frame_import, text="Import Selected Item(s)",
                                              command=self.import_selected)

        # Create clear all and clear selected buttons inside import frame
        self.btn_clear_all = ttk.Button(self.frame_import, text="Clear All Items", command=self.clear_all)
        self.btn_clear_selected = ttk.Button(self.frame_import, text="Clear Selected Item(s)",
                                             command=self.clear_selected)

        # Create import tree frame inside import frame
        self.frame_tree_import = ttk.Frame(self.frame_import)

        # Create import tree for import tree frame using number of column headings
        self.tree_import = ttk.Treeview(self.frame_tree_import,
                                        columns=[f"#{i}" for i in range(1, len(self.col_heads) - 1)])

        # Set import tree columns using list of widths and column headings
        for i in range(len(self.col_heads) - 1):
            self.tree_import.column(f"#{i}", width=self.widths[i + 1])
            self.tree_import.heading(f"#{i}", text=self.col_heads[i + 1])

        # Create vertical and horizontal scrollbars for import tree
        self.vsb_import = ttk.Scrollbar(self.frame_tree_import, orient="vertical", command=self.tree_import.yview)
        self.hsb_import = ttk.Scrollbar(self.frame_tree_import, orient="horizontal", command=self.tree_import.xview)
        self.tree_import.configure(yscrollcommand=self.vsb_import.set, xscrollcommand=self.hsb_import.set)

        # Grid all GUI elements
        self.grid_widgets()

        # Load items into search tree from database
        self.search()

        # Add main notebook to admin window
        self.admin_notebook.pack(expand=1, fill="both")

    def grid_widgets(self):
        # Configure rows and columns in search frame
        for i in range(15):
            self.frame_search.rowconfigure(i, weight=1)
        for i in range(4):
            self.frame_search.columnconfigure(i, weight=1)

        # Grid search tree frame in search frame
        self.frame_tree_search.grid(row=0, column=0, rowspan=13, columnspan=4, sticky="nsew", padx=5,
                                    pady=5)

        # Grid search entry and button in search frame
        self.txt_search.grid(row=13, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)
        self.btn_search.grid(row=13, column=3, sticky="nsew", padx=5, pady=5)

        # Grid shortlist button in search frame
        self.btn_shortlist.grid(row=14, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        # Configure rows and columns in search tree frame
        self.frame_tree_search.rowconfigure(0, weight=999)
        self.frame_tree_search.rowconfigure(1, weight=1)
        self.frame_tree_search.columnconfigure(0, weight=999)
        self.frame_tree_search.columnconfigure(1, weight=1)

        # Grid search tree and scrollbars in search tree frame
        self.tree_search.grid(row=0, column=0, sticky="nsew")
        self.vsb_search.grid(row=0, column=1, rowspan=2, sticky="nsew")
        self.hsb_search.grid(row=1, column=0, sticky="nsew")

        # Configure rows and columns in add frame
        for i in range(len(self.col_heads)):
            self.frame_add.rowconfigure(i, weight=1)
        for i in range(4):
            self.frame_add.columnconfigure(i, weight=1)

        # Grid column heading labels and entries in add frame
        for i in range(len(self.col_heads) - 1):
            self.lbl_add[i].grid(row=i, column=0, sticky="nsew", padx=5, pady=5)
            self.txt_add[i].grid(row=i, column=1, columnspan=3, sticky="nsew", padx=5, pady=5)

        # Grid add button in add frame
        self.btn_add.grid(row=len(self.col_heads) - 1, column=0, columnspan=4, sticky="nsew", padx=5,
                          pady=5)

        # Configure rows and columns in edit frame
        for i in range(len(self.col_heads) + 2):
            self.frame_edit.rowconfigure(i, weight=1)
        for i in range(4):
            self.frame_edit.columnconfigure(i, weight=1)

        # Grid edit combobox in edit frame
        self.cmb_edit.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        # Grid column heading labels and entries in edit frame
        for i in range(len(self.col_heads)):
            self.lbl_edit[i].grid(row=i + 1, column=0, sticky="nsew", padx=5, pady=5)
            self.txt_edit[i].grid(row=i + 1, column=1, columnspan=3, sticky="nsew", padx=5, pady=5)

        # Grid edit button in edit frame
        self.btn_edit.grid(row=len(self.col_heads) + 1, column=0, columnspan=4, sticky="nsew", padx=5,
                           pady=5)

        # Configure rows and columns in delete frame
        for i in range(len(self.col_heads) + 2):
            self.frame_delete.rowconfigure(i, weight=1)
        for i in range(4):
            self.frame_delete.columnconfigure(i, weight=1)

        # Grid delete combobox in delete frame
        self.cmb_delete.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        # Grid column heading labels and entries in delete frame
        for i in range(len(self.col_heads)):
            self.lbl_delete[i].grid(row=i + 1, column=0, sticky="nsew", padx=5, pady=5)
            self.txt_delete[i].grid(row=i + 1, column=1, columnspan=3, sticky="nsew", padx=5, pady=5)

        # Grid delete button in delete frame
        self.btn_delete.grid(row=len(self.col_heads) + 1, column=0, columnspan=4, sticky="nsew", padx=5,
                             pady=5)

        # Configure rows and columns in import frame
        for i in range(15):
            self.frame_import.rowconfigure(i, weight=1)
        for i in range(5):
            self.frame_import.columnconfigure(i, weight=1)

        # Grid import tree frame in import frame
        self.frame_tree_import.grid(row=0, column=0, rowspan=14, columnspan=5, sticky="nsew", padx=5,
                                    pady=5)

        # Grid open csv button in import frame
        self.btn_open_csv.grid(row=14, column=0, sticky="nsew", padx=5, pady=5)

        # Grid import all and import selected buttons in import frame
        self.btn_import_all.grid(row=14, column=1, sticky="nsew", padx=5, pady=5)
        self.btn_import_selected.grid(row=14, column=2, sticky="nsew", padx=5, pady=5)

        # Grid clear all and clear selected buttons in import frame
        self.btn_clear_all.grid(row=14, column=3, sticky="nsew", padx=5, pady=5)
        self.btn_clear_selected.grid(row=14, column=4, sticky="nsew", padx=5, pady=5)

        # Configure rows and columns in import tree frame
        self.frame_tree_import.rowconfigure(0, weight=999)
        self.frame_tree_import.rowconfigure(1, weight=1)
        self.frame_tree_import.columnconfigure(0, weight=999)
        self.frame_tree_import.columnconfigure(1, weight=1)

        # Grid import tree and scrollbars in import tree frame
        self.tree_import.grid(row=0, column=0, sticky="nsew")
        self.vsb_import.grid(row=0, column=1, rowspan=2, sticky="nsew")
        self.hsb_import.grid(row=1, column=0, sticky="nsew")

    def search(self):
        # Update combobox in edit and delete frames
        self.update_cmb()

        # Remove existing items from search tree
        self.tree_search.delete(*self.tree_search.get_children())

        # Loop through items in database by searching it, passing chosen category
        for item in AdminMethods.search(self.category):
            # Insert all items from database into search tree if search entry is empty
            if self.txt_search.get() == "":
                self.tree_search.insert("", tk.END, text=item[0], values=item[1:])

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
                    self.tree_search.insert("", tk.END, text=item[0], values=item[1:])

    def shortlist(self):
        # Store selected items to append to shortlist in 2D list
        items = []
        for selection in self.tree_search.selection():
            items.append([self.tree_search.item(selection, "text"), self.tree_search.item(selection, "values")[0]])

            # Remove selection from search tree to indicate completion of shortlisting
            self.tree_search.selection_remove(selection)

        # Append items to shortlist, passing chosen category and items
        AdminMethods.shortlist(self.category, items)

    def add(self):
        # Check if first entry is not empty
        if self.txt_add[0].get() != "":
            # Store text from each entry in list
            item = []
            for i in range(len(self.col_heads) - 1):
                item.append(self.txt_add[i].get())

                # Clear text in entry
                self.txt_add[i].delete(0, tk.END)

            # Add item to database, passing chosen category and item
            AdminMethods.add(self.category, item)

            # Load items into search tree from database
            self.search()
        else:
            # Else display error message asking user to provide value in first entry
            mb.showinfo("Error Adding Item", f"Please provide a value for {self.col_heads[1]}.")

    def edit(self):
        # Check if first and second entries are not empty
        if self.txt_edit[0].get() != "" and self.txt_edit[1].get() != "":
            # Clear text in edit combobox
            self.cmb_edit.set("")

            # Store text from second entry onwards in list
            item = []
            for i in range(len(self.col_heads) - 1):
                item.append(self.txt_edit[i + 1].get())

                # Clear text in entry
                self.txt_edit[i + 1].delete(0, tk.END)

            # Append text from first entry to list of item values
            item.append(int(self.txt_edit[0].get()))

            # Clear text in first entry
            self.txt_edit[0].configure(state="normal")
            self.txt_edit[0].delete(0, tk.END)
            self.txt_edit[0].configure(state="disabled")

            # Edit item in database, passing chosen category and new item values
            AdminMethods.edit(self.category, item)

            # Load items into search tree from database
            self.search()
        else:
            # Else display error message asking user to select item and provide value in second entry
            mb.showinfo("Error Editing Item", f"Please select an item and provide a value for {self.col_heads[1]}.")

    def delete(self):
        # Check if first entry is not empty
        if self.txt_delete[0].get() != "":
            # Clear text in delete combobox
            self.cmb_delete.set("")

            # Store text from first entry to variable
            item_id = int(self.txt_delete[0].get())

            # Clear text in entries
            for i in range(len(self.col_heads)):
                self.txt_delete[i].configure(state="normal")
                self.txt_delete[i].delete(0, tk.END)
                self.txt_delete[i].configure(state="disabled")

            # Delete item from database, passing chosen category and item id
            AdminMethods.delete(self.category, item_id)

            # Load items into search tree from database
            self.search()
        else:
            # Else display error message asking user to select item
            mb.showinfo("Error Deleting Item", "Please select an item.")

    def open_csv(self):
        # Store csv file path that user opens to variable
        path_to_file = fd.askopenfilename(filetypes=[("CSV Files", "*.csv")])

        # Check if path to file is not blank
        if path_to_file != "":
            # Open CSV file
            csv_file = open(path_to_file)

            # Loop through rows in CSV file
            for item in csv.reader(csv_file):
                # Store values in list and append empty strings as needed to match number of column headings
                values = item[1:]
                for _ in range(len(self.col_heads) - 2 - len(item[1:])):
                    values.append("")

                # Trim values as needed to match number of column headings
                values = values[:len(self.col_heads) - 2]

                # Insert item from CSV file into import tree
                self.tree_import.insert("", tk.END, text=item[0], values=values)

            # Close CSV file
            csv_file.close()

    def import_all(self):
        # Flag to indicate validity of item(s) to be imported
        valid = True

        # Store item(s) from import tree in 2D list
        items = []
        for row in self.tree_import.get_children():
            item = [self.tree_import.item(row, "text")]
            item.extend(self.tree_import.item(row, "values"))
            items.append(item)

            # Check if first value of item is blank and if flag state is unchanged
            if item[0] == "" and valid:
                # Change flag state
                valid = False

        # Check if item(s) to be imported is not blank
        if len(items) > 0:
            # Check if flag state is unchanged
            if valid:
                # Clear item(s) from import tree
                self.clear_all()

                # Import item(s) into database, passing chosen category and item(s)
                AdminMethods.import_items(self.category, items)

                # Load items into search tree from database
                self.search()
            else:
                # Else display error message asking user to provide first value for each item
                mb.showinfo("Error Importing Item(s)", f"All items must have a value for {self.col_heads[1]}.")

    def import_selected(self):
        # Flag to indicate validity of item(s) to be imported
        valid = True

        # Store selected item(s) from import tree in 2D list
        items = []
        for row in self.tree_import.selection():
            item = [self.tree_import.item(row, "text")]
            item.extend(self.tree_import.item(row, "values"))
            items.append(item)

            # Check if first value of item is blank and if flag state is unchanged
            if item[0] == "" and valid:
                # Change flag state
                valid = False

        # Check if item(s) to be imported is not blank
        if len(items) > 0:
            # Check if flag state is unchanged
            if valid:
                # Clear selected item(s) from import tree
                self.clear_selected()

                # Import selected item(s) into database, passing chosen category and selected item(s)
                AdminMethods.import_items(self.category, items)

                # Load items into search tree from database
                self.search()
            else:
                # Else display error message asking user to provide first value for each selected item
                mb.showinfo("Error Importing Item(s)", f"Selected item(s) must have a value for {self.col_heads[1]}.")

    def clear_all(self):
        # Remove existing items from import tree
        self.tree_import.delete(*self.tree_import.get_children())

    def clear_selected(self):
        # Remove selected items from import tree
        self.tree_import.delete(*self.tree_import.selection())

    def fill_txt_edit(self, event):
        # Log edit combobox selection event
        print(event)

        # Store database items in 2D list by searching it, passing chosen category
        search_results = AdminMethods.search(self.category)

        # Store id of each database item in list
        item_ids = []
        for result in search_results:
            item_ids.append(str(result[0]))

        # Assign database item at id of combobox selection to variable
        item = search_results[item_ids.index(self.cmb_edit.get().split(": ")[0])]

        # Insert item id as text into first entry
        self.txt_edit[0].configure(state="normal")
        self.txt_edit[0].delete(0, tk.END)
        self.txt_edit[0].insert(0, item[0])
        self.txt_edit[0].configure(state="disabled")

        # Insert remaining item values as text into respective entries
        for i in range(len(self.col_heads) - 1):
            self.txt_edit[i + 1].delete(0, tk.END)
            self.txt_edit[i + 1].insert(0, item[i + 1])

    def fill_txt_delete(self, event):
        # Log delete combobox selection event
        print(event)

        # Store database items in 2D list by searching it, passing chosen category
        search_results = AdminMethods.search(self.category)

        # Store id of each database item in list
        item_ids = []
        for result in search_results:
            item_ids.append(str(result[0]))

        # Assign database item at id of combobox selection to variable
        item = search_results[item_ids.index(self.cmb_delete.get().split(": ")[0])]

        # Insert item values as text into respective entries
        for i in range(len(self.col_heads)):
            self.txt_delete[i].configure(state="normal")
            self.txt_delete[i].delete(0, tk.END)
            self.txt_delete[i].insert(0, item[i])
            self.txt_delete[i].configure(state="disabled")

    def update_cmb(self):
        # Store item id and first value of each item in 2D list by searching database, passing chosen category
        items = []
        for result in AdminMethods.search(self.category):
            items.append(f"{result[0]}: {result[1]}")

        # Assign items to edit combobox values and delete combobox values
        self.cmb_edit["values"] = items
        self.cmb_delete["values"] = items
