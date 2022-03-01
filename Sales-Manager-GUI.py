import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
import pandas as pd


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Connect to database
        self.conn = sqlite3.connect('Sales-Manager.db')
        self.product_name_list = [tuple[0] for tuple in self.conn.execute('SELECT * FROM Product').description]
        self.customers_name_list = [tuple[0] for tuple in self.conn.execute('SELECT * FROM Customer').description]
        self.sales_name_list = [tuple[0] for tuple in self.conn.execute('SELECT * FROM Sales').description]
        self.inventory_name_list = [tuple[0] for tuple in self.conn.execute('SELECT * FROM Inventory').description]

        # App configuration
        self.colwidth = 20
        self.title('Sales Manager')
        tabControl = ttk.Notebook(self)

        self.tabProduct = ttk.Frame(tabControl)
        self.tab_setup('Product', self.tabProduct)
        tabControl.add(self.tabProduct, text='Products')

        self.tabCustomers = ttk.Frame(tabControl)
        self.tab_setup('Customer', self.tabCustomers)
        tabControl.add(self.tabCustomers, text='Customers')

        self.tabSales = ttk.Frame(tabControl)
        self.tab_setup('Sales', self.tabSales)
        tabControl.add(self. tabSales, text='Sales')

        self.tabInventory = ttk.Frame(tabControl)
        self.tab_setup('Inventory', self.tabInventory)
        tabControl.add(self.tabInventory, text='Inventory')

        tabControl.pack(expand=1, fill='both')

    def tab_setup(self, table, tab):
        sql_query = 'SELECT * FROM %s' % table
        query = self.conn.execute(sql_query)
        cols = [column[0] for column in query.description]
        ttk.Button(tab, text='Add ' + table, command=lambda: self.add_entry(table, cols)).grid(column=0, row=0)
        for i in range(len(cols)-1):
            ttk.Label(tab, text=cols[i+1], width=self.colwidth).grid(column=i, row=1)
        data = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
        for i in range(len(data)):
            for j in range(len(cols)-1):
                ttk.Label(tab, text=data.loc[i, cols[j+1]], width=self.colwidth).grid(column=j, row=i+2)
            ttk.Button(tab, text='Edit', command=self.edit_entry).grid(column=len(cols), row=i+2)
            ttk.Button(tab, text='Delete', command=self.delete_entry).grid(column=len(cols)+1, row=i+2)

    def edit_entry(self):
        print('This will be an edit')

    def delete_entry(self):
        print('This will be a delete')

    def add_entry(self, table, cols):
        add_popup = Toplevel()
        add_popup.title('Add to '+table)
        values = []
        for i in range(len(cols)-1):
            ttk.Label(add_popup, text=cols[i+1]).grid(column=i, row=0)
            text_value = tk.Text(add_popup, height=1, width=self.colwidth)
            values.append(text_value)
            text_value.grid(column=i, row=1)
        ttk.Button(add_popup, text='Add', command=lambda: self.add_entry_sql(table, cols, values)).grid(column=len(cols), row=2)
        ttk.Button(add_popup, text='Close', command=add_popup.destroy).grid(column=len(cols), row=3)

    def add_entry_sql(self, table, cols, values):
        retrieved_values = list(map(self.get_values, values))
        retrieved_values = list(map(lambda s: s.strip(), retrieved_values))
        col_string = ', '.join(cols[1:])
        values_string = '\', \''.join(retrieved_values)
        sql_insert = 'INSERT INTO %s (%s) VALUES (\'%s\')' % (table, col_string, values_string)
        self.conn.execute(sql_insert)
        self.conn.commit()
        self.tab_setup(table, self.tabProduct)

    def get_values(self, text_widget):
        value = text_widget.get("1.0", END)
        return value


if __name__ == "__main__":
    app = App()
    app.mainloop()
