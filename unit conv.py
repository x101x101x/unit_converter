import tkinter as tk
from tkinter import ttk, messagebox

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")
        self.root.configure(bg='pink')  # Set background color

        # Initialize variables
        self.temperature_var = tk.StringVar()
        self.temperature_unit_var = tk.StringVar()
        self.measurement_var = tk.StringVar()
        self.measurement_unit_var = tk.StringVar()
        self.weight_var = tk.StringVar()
        self.weight_unit_var = tk.StringVar()

        # Center window on launch
        window_width = 450
        window_height = 240
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_position = int((screen_width - window_width) / 2)
        y_position = int((screen_height - window_height) / 2)
        root.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')

        # Temperature Converter Frame
        temp_frame = ttk.LabelFrame(self.root, text="Temperature Converter",width=screen_width)
        temp_frame.pack_propagate(False)
        temp_frame.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        ttk.Label(temp_frame, text="Temperature:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.temp_entry = ttk.Entry(temp_frame, width=25, textvariable=self.temperature_var)
        self.temp_entry.grid(row=0, column=1, padx=5, pady=5)
        self.temp_entry.focus()

        self.temp_unit_combo = ttk.Combobox(temp_frame, width=8, textvariable=self.temperature_unit_var,
                                            values=["Celsius", "Fahrenheit"])
        self.temp_unit_combo.grid(row=0, column=2, padx=5, pady=5)
        self.temp_unit_combo.current(0)  # Set default to Celsius

        ttk.Button(temp_frame, text="Convert", command=self.convert_temperature).grid(row=0, column=3, padx=5, pady=5)

        # Measurement Converter Frame
        meas_frame = ttk.LabelFrame(self.root, text="Measurement Converter")
        meas_frame.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        ttk.Label(meas_frame, text="Measurement:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.meas_entry = ttk.Entry(meas_frame, width=24, textvariable=self.measurement_var)
        self.meas_entry.grid(row=0, column=1, padx=5, pady=5)

        self.meas_unit_combo = ttk.Combobox(meas_frame, width=8, textvariable=self.measurement_unit_var,
                                            values=["Meters", "Feet"])
        self.meas_unit_combo.grid(row=0, column=2, padx=5, pady=5)
        self.meas_unit_combo.current(0)  # Set default to Meters

        ttk.Button(meas_frame, text="Convert", command=self.convert_measurement).grid(row=0, column=3, padx=5, pady=5)

        # Weight Converter Frame
        weight_frame = ttk.LabelFrame(self.root, text="Weight Converter")
        weight_frame.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        ttk.Label(weight_frame, text="Weight:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.weight_entry = ttk.Entry(weight_frame, width=30, textvariable=self.weight_var)
        self.weight_entry.grid(row=0, column=1, padx=5, pady=5)

        self.weight_unit_combo = ttk.Combobox(weight_frame, width=8, textvariable=self.weight_unit_var,
                                              values=["Kilograms", "Pounds"])
        self.weight_unit_combo.grid(row=0, column=2, padx=5, pady=5)
        self.weight_unit_combo.current(0)  # Set default to Kilograms

        ttk.Button(weight_frame, text="Convert", command=self.convert_weight).grid(row=0, column=3, padx=5, pady=5)

    def convert_temperature(self):
        try:
            temperature = float(self.temperature_var.get())
            if self.temperature_unit_var.get() == "Celsius":
                converted_temp = temperature * 9/5 + 32
                messagebox.showinfo("Converted Temperature", f"{temperature} Celsius = {converted_temp:.2f} Fahrenheit")
            elif self.temperature_unit_var.get() == "Fahrenheit":
                converted_temp = (temperature - 32) * 5/9
                messagebox.showinfo("Converted Temperature", f"{temperature} Fahrenheit = {converted_temp:.2f} Celsius")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for temperature.")

    def convert_measurement(self):
        try:
            measurement = float(self.measurement_var.get())
            if self.measurement_unit_var.get() == "Meters":
                converted_meas = measurement * 3.28084
                messagebox.showinfo("Converted Measurement", f"{measurement} Meters = {converted_meas:.2f} Feet")
            elif self.measurement_unit_var.get() == "Feet":
                converted_meas = measurement / 3.28084
                messagebox.showinfo("Converted Measurement", f"{measurement} Feet = {converted_meas:.2f} Meters")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for measurement.")

    def convert_weight(self):
        try:
            weight = float(self.weight_var.get())
            if self.weight_unit_var.get() == "Kilograms":
                converted_weight = weight * 2.20462
                messagebox.showinfo("Converted Weight", f"{weight} Kilograms = {converted_weight:.2f} Pounds")
            elif self.weight_unit_var.get() == "Pounds":
                converted_weight = weight / 2.20462
                messagebox.showinfo("Converted Weight", f"{weight} Pounds = {converted_weight:.2f} Kilograms")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for weight.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()
