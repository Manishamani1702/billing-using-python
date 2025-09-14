import tkinter as tk
from tkinter import messagebox

class SimpleBillingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Billing Software")
        self.items = []
        self.total = 0.0

        # Labels and entries
        tk.Label(root, text="Product Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(root, text="Price:").grid(row=1, column=0, padx=5, pady=5)
        self.price_entry = tk.Entry(root)
        self.price_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(root, text="Quantity:").grid(row=2, column=0, padx=5, pady=5)
        self.qty_entry = tk.Entry(root)
        self.qty_entry.grid(row=2, column=1, padx=5, pady=5)

        # Buttons
        tk.Button(root, text="Add Item", command=self.add_item).grid(row=3, column=0, columnspan=2, pady=5)
        tk.Button(root, text="Show Total", command=self.show_total).grid(row=4, column=0, columnspan=2, pady=5)

        # Listbox for items
        self.listbox = tk.Listbox(root, width=40)
        self.listbox.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def add_item(self):
        name = self.name_entry.get()
        try:
            price = float(self.price_entry.get())
            qty = int(self.qty_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Enter valid price and quantity")
            return

        line_total = price * qty
        self.items.append((name, price, qty, line_total))
        self.total += line_total

        self.listbox.insert(tk.END, f"{name} - {qty} x ₹{price:.2f} = ₹{line_total:.2f}")

        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.qty_entry.delete(0, tk.END)

    def show_total(self):
        messagebox.showinfo("Total", f"Total Amount: ₹{self.total:.2f}")


if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleBillingApp(root)
    root.mainloop()
