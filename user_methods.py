import mysql.connector as sql
import tkinter.messagebox as mb
import os


def get_db_conn():
    user = "inventory"
    password = "NISTInventory2021"
    database = "inventory"
    host = "localhost"

    return sql.connect(user=user, password=password, host=host, database=database)


# Grouping student methods into a class
class StudentMethods:
    @staticmethod
    def get_col_heads(category):
        # Connect to MySQL database and create database cursor
        db = get_db_conn()
        cur = db.cursor()

        # Fetch first three column headings of chosen category from database
        cur.execute(f"SHOW columns FROM {category.lower().replace(' ', '_')}")
        columns = cur.fetchall()[:3]

        # Disconnect from MySQL database
        db.close()

        # Return list of column headings
        return [column[0] for column in columns]

    @staticmethod
    def search(category):
        # Connect to MySQL database
        db = get_db_conn()

        # Create database cursor and fetch search results from chosen category
        cur = db.cursor()
        cur.execute(f"SELECT * FROM {category.lower().replace(' ', '_')}")
        items = cur.fetchall()

        # Disconnect from MySQL database
        db.close()

        # Return list of first three values of each item
        return [[item[0], item[1], item[2]] for item in items]

    @staticmethod
    def shortlist(category, items):
        # Open shortlist.txt and append items to shortlist
        shortlist_file = open(os.path.join(os.path.expanduser("~"), "Documents", "shortlist.txt"), "a")
        for item in items:
            shortlist_file.write(f"{category}\n{item[0]}\n{item[1]}\n")

        # Close shortlist.txt
        shortlist_file.close()


# Grouping teacher methods into a class that inherits from student methods
class TeacherMethods(StudentMethods):
    # Polymorphic method that overrides method in student methods
    @staticmethod
    def get_col_heads(category):
        # Connect to MySQL database and create database cursor
        db = get_db_conn()
        cur = db.cursor()

        # Fetch all column headings of chosen category from database
        cur.execute(f"SHOW columns FROM {category.lower().replace(' ', '_')}")
        columns = cur.fetchall()

        # Disconnect from MySQL database
        db.close()

        # Return list of column headings
        return [column[0] for column in columns]

    # Polymorphic method that overrides method in student methods
    @staticmethod
    def search(category):
        # Connect to MySQL database
        db = get_db_conn()

        # Create database cursor and fetch search results from chosen category
        cur = db.cursor()
        cur.execute(f"SELECT * FROM {category.lower().replace(' ', '_')}")
        items = cur.fetchall()

        # Disconnect from MySQL database
        db.close()

        # Return list of all values of each item
        return [list(item) for item in items]


# Grouping admin methods into a class that inherits from teacher methods
class AdminMethods(TeacherMethods):
    @staticmethod
    def add(category, item):
        # Connect to MySQL database and create database cursor
        db = get_db_conn()
        cur = db.cursor()

        # Create variable to store table name by manipulating chosen category string
        table_name = category.lower().replace(" ", "_")

        # Create list of column headings
        col_heads = AdminMethods.get_col_heads(category)[1:]

        # Create list of placeholders for item values to be added to database
        placeholders = ["%s" for _ in range(len(col_heads))]

        # Create SQL query string using table name, column headings, and placeholders for item values
        sql_query = f"INSERT INTO {table_name} ({', '.join(col_heads)}) VALUES ({', '.join(placeholders)})"

        try:
            # Execute SQL query, passing item to be added to database
            cur.execute(sql_query, item)
            db.commit()

            # Display message if item added successfully
            mb.showinfo("Item Added Successfully",
                        f"Item added at {AdminMethods.get_col_heads(category)[0]} = {cur.lastrowid}.")
        except sql.Error as error:
            # Display error message if adding item causes error
            mb.showinfo("Error Adding Item", str(error))

        # Disconnect from MySQL database
        db.close()

    @staticmethod
    def edit(category, item):
        # Connect to MySQL database and create database cursor
        db = get_db_conn()
        cur = db.cursor()

        # Create variable to store table name by manipulating chosen category string
        table_name = category.lower().replace(" ", "_")

        # Create list of column headings
        col_heads = AdminMethods.get_col_heads(category)[1:]

        # Create list of fields for item values to be edited in database
        fields = [f"{col_head} = %s" for col_head in col_heads]

        # Create SQL query string using table name, column headings, and fields for item values
        sql_query = f"UPDATE {table_name} SET {', '.join(fields)} WHERE {AdminMethods.get_col_heads(category)[0]} = %s"

        try:
            # Execute SQL query, passing item to be edited in database
            cur.execute(sql_query, item)
            db.commit()

            # Display message if item edited successfully
            mb.showinfo("Item Edited Successfully",
                        f"Item edited where {AdminMethods.get_col_heads(category)[0]} = {item[len(item) - 1]}.")
        except sql.Error as error:
            # Display error message if editing item causes error
            mb.showinfo("Error Editing Item", str(error))

        # Disconnect from MySQL database
        db.close()

    @staticmethod
    def delete(category, item_id):
        # Connect to MySQL database and create database cursor
        db = get_db_conn()
        cur = db.cursor()

        # Create variable to store table name by manipulating chosen category string
        table_name = category.lower().replace(" ", "_")

        # Create SQL query string using table name and id of item to be deleted from database
        sql_query = f"DELETE FROM {table_name} WHERE {AdminMethods.get_col_heads(category)[0]} = {item_id}"

        try:
            # Execute SQL query
            cur.execute(sql_query)
            db.commit()

            # Display message if item deleted successfully
            mb.showinfo("Item Deleted Successfully",
                        f"Item deleted where {AdminMethods.get_col_heads(category)[0]} = {item_id}.")
        except sql.Error as error:
            # Display error message if deleting item causes error
            mb.showinfo("Error Deleting Item", str(error))

        # Disconnect from MySQL database
        db.close()

    @staticmethod
    def import_items(category, items):
        # Connect to MySQL database and create database cursor
        db = get_db_conn()
        cur = db.cursor()

        # Create variable to store table name by manipulating chosen category string
        table_name = category.lower().replace(" ", "_")

        # Create list of column headings
        col_heads = AdminMethods.get_col_heads(category)[1:]

        # Create list of placeholders for item values to be imported into database
        placeholders = ["%s" for _ in range(len(col_heads))]

        # Create SQL query string using table name, column headings, and placeholders for item values
        sql_query = f"INSERT INTO {table_name} ({', '.join(col_heads)}) VALUES ({', '.join(placeholders)})"

        try:
            # Create list to store ids of imported item(s)
            ids = []

            # Loop through each item in items
            for item in items:
                # Execute SQL query, passing item to be imported into database
                cur.execute(sql_query, item)
                db.commit()

                # Append id of imported item to list of ids
                ids.append(cur.lastrowid)
            id_head = AdminMethods.get_col_heads(category)[0]

            # Check if only one item imported into database
            if ids[0] == ids[len(ids) - 1]:
                # Display message if item imported successfully and show id
                mb.showinfo("Item Imported Successfully", f"Item imported at {id_head} = {ids[0]}.")
            else:
                # Display message if items imported successfully and show id range
                mb.showinfo("Items Imported Successfully",
                            f"Items imported at {id_head} = {ids[0]} up to {id_head} = {ids[len(ids) - 1]}.")
        except sql.Error as error:
            # Display error message if importing item(s) causes error
            mb.showinfo("Error Importing Item(s)", str(error))

        # Disconnect from MySQL database
        db.close()
