import tkinter as tk

# Constants and styling
FONT_TITLE = ("Arial", 16, "bold")
FONT_LABEL = ("Arial", 12)
FONT_ENTRY = ("Arial", 12)
FONT_BTN = ("Arial", 11, "bold")

COLOR_BG = "#F5F5F5"
COLOR_YELLOW = "#FFF59D"
COLOR_PINK = "#F8BBD0"
COLOR_RESET = "#E0E0E0"
COLOR_HOME = "#B3E5FC"
COLOR_TEXT = "#333333"
COLOR_ERROR = "#D32F2F"

ABS_ZERO_C = -273.15
ABS_ZERO_F = -459.67

# Logic class for calculations
class TemperatureConverter:
    """Handles all validation and calculation logic without Tkinter dependencies."""
    
    def to_celsius(self, f_str):
        try:
            f = float(f_str)
            if f < ABS_ZERO_F:
                return "Temperature too low"
            c = (f - 32) * 5 / 9
            return f"{c:.2f} °C"
        except ValueError:
            return "Please enter a number"

    def to_fahrenheit(self, c_str):
        try:
            c = float(c_str)
            if c < ABS_ZERO_C:
                return "Temperature too low"
            f = (c * 9 / 5) + 32
            return f"{f:.2f} °F"
        except ValueError:
            return "Please enter a number"

# Responsive GUI class
class ConverterGUI:
    """Handles the user interface, widget mapping, and window responsiveness."""
    
    def __init__(self):
        # Create logic object
        self.converter = TemperatureConverter()
        
        # Setup main window
        self.root = tk.Tk()
        self.root.title("Temperature Converter")
        self.root.geometry("400x350")
        self.root.minsize(350, 300)
        self.root.configure(bg=COLOR_BG)
        
        # Configure root window grid to expand
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        
        # Container frame to stack screens
        self.container = tk.Frame(self.root, bg=COLOR_BG)
        self.container.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        
        # Configure container grid to expand
        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)
        
        # Frame dictionary setup
        self.frames = {}
        self.frames["MainFrame"] = self.create_main_frame()
        self.frames["to_cFrame"] = self.create_to_c_frame()
        self.frames["to_fFrame"] = self.create_to_f_frame()
        
        # Show home screen first
        self.show_frame("MainFrame")
        
    def show_frame(self, frame_name):
        """Hides all screens first, then displays only the requested frame."""
        for frame in self.frames.values():
            frame.grid_forget()
            
        active_frame = self.frames[frame_name]
        # Use sticky="nsew" to fill container frame space
        active_frame.grid(row=0, column=0, sticky="nsew")

    def configure_grid_weights(self, frame, num_rows, num_cols):
        """Loops through rows/columns giving them equal scaling weight."""
        for r in range(num_rows):
            frame.rowconfigure(r, weight=1)
        for c in range(num_cols):
            frame.columnconfigure(c, weight=1)

    # Responsive screens
    def create_main_frame(self):
        frame = tk.Frame(self.container, bg=COLOR_BG)
        self.configure_grid_weights(frame, num_rows=3, num_cols=1)
        
        lbl_title = tk.Label(frame, text="Temperature Converter", font=FONT_TITLE, bg=COLOR_BG, fg=COLOR_TEXT)
        lbl_title.grid(row=0, column=0, pady=10, sticky="ew")
        
        btn_to_c = tk.Button(frame, text="Fahrenheit to Celsius", font=FONT_BTN, bg=COLOR_YELLOW, 
                             command=lambda: self.show_frame("to_cFrame"), height=2)
        btn_to_c.grid(row=1, column=0, pady=10, sticky="ew")
        
        btn_to_f = tk.Button(frame, text="Celsius to Fahrenheit", font=FONT_BTN, bg=COLOR_PINK, 
                             command=lambda: self.show_frame("to_fFrame"), height=2)
        btn_to_f.grid(row=2, column=0, pady=10, sticky="ew")
        
        return frame

    def create_to_c_frame(self):
        frame = tk.Frame(self.container, bg=COLOR_BG)
        self.configure_grid_weights(frame, num_rows=5, num_cols=2)
        
        lbl_title = tk.Label(frame, text="Fahrenheit to Celsius", font=FONT_TITLE, bg=COLOR_BG, fg=COLOR_TEXT)
        lbl_title.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")
        
        lbl_prompt = tk.Label(frame, text="Enter Fahrenheit:", font=FONT_LABEL, bg=COLOR_BG)
        lbl_prompt.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        
        ent_input = tk.Entry(frame, font=FONT_ENTRY, justify="center")
        ent_input.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        lbl_result = tk.Label(frame, text="", font=FONT_LABEL, bg=COLOR_BG, fg=COLOR_TEXT)
        lbl_result.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")
        
        btn_calc = tk.Button(frame, text="Calculate", font=FONT_BTN, bg=COLOR_YELLOW,
                             command=lambda: self.calculate_celsius(ent_input, lbl_result))
        btn_calc.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        
        btn_reset = tk.Button(frame, text="Reset", font=FONT_BTN, bg=COLOR_RESET,
                              command=lambda: self.reset_fields(ent_input, lbl_result))
        btn_reset.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
        
        btn_home = tk.Button(frame, text="Home", font=FONT_BTN, bg=COLOR_HOME,
                             command=lambda: self.show_frame("MainFrame"))
        btn_home.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")
        
        return frame

    def create_to_f_frame(self):
        frame = tk.Frame(self.container, bg=COLOR_BG)
        self.configure_grid_weights(frame, num_rows=5, num_cols=2)
        
        lbl_title = tk.Label(frame, text="Celsius to Fahrenheit", font=FONT_TITLE, bg=COLOR_BG, fg=COLOR_TEXT)
        lbl_title.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")
        
        lbl_prompt = tk.Label(frame, text="Enter Celsius:", font=FONT_LABEL, bg=COLOR_BG)
        lbl_prompt.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        
        ent_input = tk.Entry(frame, font=FONT_ENTRY, justify="center")
        ent_input.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        lbl_result = tk.Label(frame, text="", font=FONT_LABEL, bg=COLOR_BG, fg=COLOR_TEXT)
        lbl_result.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")
        
        btn_calc = tk.Button(frame, text="Calculate", font=FONT_BTN, bg=COLOR_PINK,
                             command=lambda: self.calculate_fahrenheit(ent_input, lbl_result))
        btn_calc.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        
        btn_reset = tk.Button(frame, text="Reset", font=FONT_BTN, bg=COLOR_RESET,
                              command=lambda: self.reset_fields(ent_input, lbl_result))
        btn_reset.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
        
        btn_home = tk.Button(frame, text="Home", font=FONT_BTN, bg=COLOR_HOME,
                             command=lambda: self.show_frame("MainFrame"))
        btn_home.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")
        
        return frame

    # Dynamic calculator and color
    def calculate_celsius(self, entry, label):
        raw_val = entry.get()
        result = self.converter.to_celsius(raw_val)
        self.update_result_display(result, label)

    def calculate_fahrenheit(self, entry, label):
        raw_val = entry.get()
        result = self.converter.to_fahrenheit(raw_val)
        self.update_result_display(result, label)

    def update_result_display(self, result_text, label):
        """Switches text color to red if an error string occurs."""
        if "too low" in result_text or "number" in result_text:
            label.configure(text=result_text, fg=COLOR_ERROR)
        else:
            label.configure(text=result_text, fg=COLOR_TEXT)

    # Method for reset buttons
    def reset_fields(self, entry, label):
        entry.delete(0, tk.END)
        label.configure(text="", fg=COLOR_TEXT)

    def run(self):
        self.root.mainloop()

# Main execution
if __name__ == "__main__":
    app = ConverterGUI()
    app.run()
