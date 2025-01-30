#AUTHOR-- --PYTH.ONICMIND --
#THIS IS A SIMPLE CALCULATOR TO PLOT 3D GRAPH WITH EQUATIONS
#ENJOY AND CODE MORE /......

import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sympy as sp  # Import sympy for symbolic math

class Calculator3D(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("3D Calculator")
        self.geometry("600x600")

        # Instruction label to instruct
        self.label = tk.Label(self, text="Enter a function of x and y (e.g., sin(x) * cos(y)):")
        self.label.pack(pady=10)

        # Entry widget for user to input the function
        self.entry = tk.Entry(self, width=50)
        self.entry.pack(pady=10)

        # Button to plot the 3D surface
        self.plot_button = tk.Button(self, text="Plot 3D Surface", command=self.plot_surface)
        self.plot_button.pack(pady=10)

        # Button to clear the plot
        self.clear_button = tk.Button(self, text="Clear Plot", command=self.clear_plot)
        self.clear_button.pack(pady=10)

        # Button to clear the input field
        self.clear_input_button = tk.Button(self, text="Clear Input", command=self.clear_input)
        self.clear_input_button.pack(pady=10)

        # Create a matplotlib figure and embed it in the Tkinter window
        self.figure = plt.Figure(figsize=(5, 5), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().pack()

    def plot_surface(self):
        function_str = self.entry.get()
        x, y = sp.symbols('x y')

        try:
            # Parse the function using sympy
            z = sp.sympify(function_str)

            # Create a grid of x and y values
            x_vals = np.linspace(-5, 5, 100)
            y_vals = np.linspace(-5, 5, 100)
            x_mesh, y_mesh = np.meshgrid(x_vals, y_vals)

            # Evaluate the function on the grid
            z_mesh = np.array([[float(z.subs({x: x_val, y: y_val})) for x_val in x_vals] for y_val in y_vals])

            # Clear the previous plot
            self.figure.clear()

            # Create a new 3D plot
            ax = self.figure.add_subplot(111, projection='3d')
            ax.plot_surface(x_mesh, y_mesh, z_mesh, cmap='viridis')

            ax.set_xlabel('X axis')
            ax.set_ylabel('Y axis')
            ax.set_zlabel('Z axis')
            ax.set_title('3D Surface Plot')

            # Redraw the plot
            self.canvas.draw()
        except Exception as e:
            messagebox.showerror("Error", f"Invalid function: {e}")

    def clear_plot(self):
        # Clear the figure (plot)
        self.figure.clear()

        # Redraw the empty figure
        self.canvas.draw()

    def clear_input(self):
        # Clear the input field
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    app = Calculator3D()
    app.mainloop()
