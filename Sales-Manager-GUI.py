import tkinter as tk
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
        ttk.Button(tab, text='Add '+table, command=self.add_entry).grid(column=0, row=0)
        sql_query = 'SELECT * FROM %s' % table
        query = self.conn.execute(sql_query)
        cols = [column[0] for column in query.description]
        for i in range(len(cols)-1):
            ttk.Label(tab, text=cols[i+1]).grid(column=i, row=1)
        data = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
        for i in range(len(data)):
            for j in range(len(cols)-1):
                ttk.Label(tab, text=data.loc[i, cols[j+1]]).grid(column=j, row=i+2)
            ttk.Button(tab, text='Edit', command=self.edit_entry).grid(column=len(cols), row=i+2)
            ttk.Button(tab, text='Delete', command=self.delete_entry).grid(column=len(cols)+1, row=i+2)

    def edit_entry(self):
        print('This will be an edit')

    def delete_entry(self):
        print('This will be a delete')

    def add_entry(self):
        print('This will be an add')

    def add_products(self, name, price, restrictions, unit, comment):
        sql_insert = 'INSERT INTO Product (Name, Price, Restrictions, Unit, Comment) VALUES (\'%s\', %d, \'%s\', \'%s\', \'%s\')' % (name, price, restrictions, unit, comment)
        self.conn.execute(sql_insert)
        self.conn.commit()


if __name__ == "__main__":
    app = App()
    app.mainloop()
