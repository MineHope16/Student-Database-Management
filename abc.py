import tkinter as tk

def update_label_text():
    new_text = entry.get()
    label.config(text=new_text)
    label_width = label.winfo_width()
    print(f"Label Width: {label_width}")

# Create the main window
root = tk.Tk()
root.title("Dynamic Label Width Example")

# Create an Entry widget for entering text
entry = tk.Entry(root)
entry.pack(pady=10)

# Create a Label widget
label = tk.Label(root, text="Initial Text")
label.pack(pady=10)

# Create a button to update the label text
update_button = tk.Button(root, text="Update Text", command=update_label_text)
update_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
