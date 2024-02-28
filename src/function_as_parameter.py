import tkinter as tk 

# Function to handle button click
def on_button_click():
    print("Button clicked!")

# Function to create a button with a specified callback function
def create_button(window, text, callback):
    button = tk.Button(window, text=text, command=callback)
    button.pack()

# Create the main application window
root = tk.Tk()
root.geometry("200x100")

# Create a button using the create_button function and pass the on_button_click function as a parameter
create_button(root, "Click me!", on_button_click)

# Run the application
root.mainloop()
