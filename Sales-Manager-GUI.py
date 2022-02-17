import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # App configuration
        self.title('Sales Manager')
        tabControl = ttk.Notebook(self)
        tabProduct = ttk.Frame(tabControl)
        tabControl.add(tabProduct, text='Products')
        tabCustomers = ttk.Frame(tabControl)
        tabControl.add(tabCustomers, text='Customers')
        tabSales = ttk.Frame(tabControl)
        tabControl.add(tabSales, text='Sales')
        tabInventory = ttk.Frame(tabControl)
        tabControl.add(tabInventory, text='Inventory')
        tabControl.pack(expand=1, fill='both')


if __name__ == "__main__":
    app = App()
    print('here?')
    app.mainloop()
    print('there?')
#root = tk.Tk()
#root.title("Tab Widget")
#tabControl = ttk.Notebook(root)
#tab1 = ttk.Frame(tabControl)
#tab2 = ttk.Frame(tabControl)
#tabControl.add(tab1, text="Tab 1")
#tabControl.add(tab2, text="Tab 2")
#tabControl.pack(expand=1, fill="both")
#ttk.Label(tab1, text="Welcome to Demo").grid(column=0, row=0, padx=30, pady=30)
#ttk.Label(tab2, text="A second tab").grid(column=0, row=0, padx=30, pady=30)
#root.mainloop()
