import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Import our custom modules
from database import init_db, add_expense
from tracker import get_spending_data, validate_expense

class FinanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WealthWatch Pro")
        self.root.geometry("350x450")
        init_db()

        # UI Layout
        tk.Label(root, text="WealthWatch Tracker", font=("Arial", 16, "bold")).pack(pady=10)
        
        tk.Label(root, text="Category:").pack()
        self.cat_entry = tk.Entry(root)
        self.cat_entry.pack(pady=5)

        tk.Label(root, text="Amount:").pack()
        self.amt_entry = tk.Entry(root)
        self.amt_entry.pack(pady=5)

        tk.Button(root, text="Save Expense", command=self.handle_save, bg="#4CAF50", fg="white", width=20).pack(pady=10)
        tk.Button(root, text="View Analytics Chart", command=self.handle_plot, bg="#2196F3", fg="white", width=20).pack(pady=5)

    def handle_save(self):
        try:
            # Use tracker to validate
            cat, amt = validate_expense(self.cat_entry.get(), self.amt_entry.get())
            # Use database to save
            add_expense(cat, amt)
            
            messagebox.showinfo("Success", f"Logged ${amt} for {cat}")
            self.cat_entry.delete(0, tk.END)
            self.amt_entry.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    def handle_plot(self):
        # Use tracker to get formatted data
        labels, values = get_spending_data()
        
        if labels is None:
            messagebox.showinfo("Info", "No data available yet.")
            return

        plt.figure(figsize=(6, 5))
        plt.pie(values, labels=labels, autopct='%1.1f%%', shadow=False, startangle=140)
        plt.title("My Spending Habits")
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceApp(root)
    root.mainloop()