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
        self.tab_setup('Product')
        tabControl.add(self.tabProduct, text='Products')

        tabCustomers = ttk.Frame(tabControl)
        tabControl.add(tabCustomers, text='Customers')
        tabSales = ttk.Frame(tabControl)
        tabControl.add(tabSales, text='Sales')
        tabInventory = ttk.Frame(tabControl)
        tabControl.add(tabInventory, text='Inventory')
        tabControl.pack(expand=1, fill='both')


        #self.add_products('Product 1',10.00,'Unrestricted','oz','This is the first product')

    def tab_setup(self, table):
        sql_query = 'SELECT * FROM %s' % table
        query = self.conn.execute(sql_query)
        cols = [column[0] for column in query.description]
        for i in range(len(cols)-1):
            ttk.Label(self.tabProduct, text=cols[i+1]).grid(column=i, row=0)
        data = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
        print(data)

    def add_products(self, name, price, restrictions, unit, comment):
        sql_insert = 'INSERT INTO Product (Name, Price, Restrictions, Unit, Comment) VALUES (\'%s\', %d, \'%s\', \'%s\', \'%s\')' % (name, price, restrictions, unit, comment)
        self.conn.execute(sql_insert)
        self.conn.commit()


if __name__ == "__main__":
    app = App()
    app.mainloop()
