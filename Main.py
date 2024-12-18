import tkinter as tk
from tkinter import ttk  # Import ttk for more modern widgets
from owlready2 import *

# Load your ontology (replace with your ontology file path)
onto_path.append("path/to/your/ontology/folder")  # Update with your actual path
onto = get_ontology("Ontology_geometrics.owl").load()  # Use the correct filename
# --- UI Functions ---

def calculate_area():
    """Calculates the area based on selected shape and dimensions."""
    shape = shape_var.get()
    try:
        if shape == "Triangle":
            base = float(base_entry.get())
            height = float(height_entry.get())
            # Accessing the formula from the ontology
            triangle_class = onto.Triangle
            area_formula = triangle_class.Area.python_name  # Get the Python equivalent of the property
            area = area_formula(base, height)  # Assuming the formula is defined in your ontology
        elif shape == "Rectangle":
            length = float(length_entry.get())
            width = float(width_entry.get())
            # Accessing the formula from the ontology (similar to Triangle)
            rectangle_class = onto.Rectangle
            area_formula = rectangle_class.Area.python_name
            area = area_formula(length, width)
        elif shape == "Square":
            side = float(side_entry.get())
            # Accessing the formula from the ontology (similar to Triangle)
            square_class = onto.Square
            area_formula = square_class.Area.python_name
            area = area_formula(side)
        else:
            area = "Invalid shape selected"
        result_label.config(text=f"Area: {area}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter numbers.")

def show_input_fields():
    """Shows the relevant input fields based on the selected shape."""
    shape = shape_var.get()
    hide_all_fields()  # Hide all fields initially
    if shape == "Triangle":
        base_label.pack()
        base_entry.pack()
        height_label.pack()
        height_entry.pack()
    elif shape == "Rectangle":
        length_label.pack()
        length_entry.pack()
        width_label.pack()
        width_entry.pack()
    elif shape == "Square":
        side_label.pack()
        side_entry.pack()

def hide_all_fields():
    """Hides all input fields."""
    base_label.pack_forget()
    base_entry.pack_forget()
    height_label.pack_forget()
    height_entry.pack_forget()
    length_label.pack_forget()
    length_entry.pack_forget()
    width_label.pack_forget()
    width_entry.pack_forget()
    side_label.pack_forget()
    side_entry.pack_forget()

# --- UI Setup ---

window = tk.Tk()
window.title("Geometry Tutor")

# Shape selection (using ttk.Combobox for a more modern look)
shape_var = tk.StringVar(value="Select Shape")
shape_options = ["Triangle", "Rectangle", "Square"]
shape_dropdown = ttk.Combobox(window, textvariable=shape_var, values=shape_options)
shape_dropdown.pack(pady=10)
shape_dropdown.bind("<<ComboboxSelected>>", lambda event: show_input_fields())  # Show fields on selection

# Input fields
base_label = tk.Label(window, text="Base:")
base_entry = tk.Entry(window)
height_label = tk.Label(window, text="Height:")
height_entry = tk.Entry(window)
length_label = tk.Label(window, text="Length:")
length_entry = tk.Entry(window)
width_label = tk.Label(window, text="Width:")
width_entry = tk.Entry(window)
side_label = tk.Label(window, text="Side Length:")
side_entry = tk.Entry(window)

# Calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate_area)
calculate_button.pack(pady=10)

# Result label
result_label = tk.Label(window, text="")
result_label.pack()

# Initial hiding of input fields
hide_all_fields()

window.mainloop()