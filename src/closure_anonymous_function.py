import tkinter as tk

# Create main application window
root = tk.Tk()
root.title("Anonymous Function Example")
root.geometry("300x200")

# Function to display a message
def display_message(message):
    label.config(text=message)

# Create a label
label = tk.Label(root, text="Click the button!", font=("Arial", 12))
label.pack(pady=10)

# Create a button with an anonymous function as the callback
button = tk.Button(root, text="Click me!", command=lambda: display_message("Button clicked!"))
button.pack()

# Run the application
root.mainloop()
