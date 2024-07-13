import tkinter as tk
import colorsys

class SpiralGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Animated Spiral")

        # Initialize GUI elements
        self.setup_gui()

        # Initialize animation variables
        self.cell_size = 0
        self.num = 1
        self.spiral = []
        self.colors = []

    def setup_gui(self):
        """Set up the GUI components."""
        self.create_widgets()

    def create_widgets(self):
        """Create all the widgets (labels, entry, button, canvas)."""
        self.create_welcome_label()
        self.create_entry_widgets()
        self.create_start_button()
        self.create_canvas()

    def create_welcome_label(self):
        """Create the welcome label."""
        self.welcome_label = tk.Label(self.root, text="Welcome to the animated spiral generator!", font=("Helvetica", 16, "bold"))
        self.welcome_label.pack(pady=10)

    def create_entry_widgets(self):
        """Create the entry widgets (label and entry field for size)."""
        self.n_label = tk.Label(self.root, text="Enter size of spiral:")
        self.n_label.pack()
        
        self.n_entry = tk.Entry(self.root)
        self.n_entry.pack()

    def create_start_button(self):
        """Create the start animation button."""
        self.start_button = tk.Button(self.root, text="Start Animation", command=self.start_animation)
        self.start_button.pack(pady=10)

    def create_canvas(self):
        """Create the canvas for drawing the spiral."""
        self.canvas_size = 800  # Initial canvas size
        self.canvas = tk.Canvas(self.root, width=self.canvas_size, height=self.canvas_size, bg='white')
        self.canvas.pack()

    def start_animation(self):
        """Start the animation of drawing the spiral."""
        try:
            n = int(self.n_entry.get())
            if n <= 0:
                raise ValueError("Size must be a positive integer")
            
            self.spiral = [[''] * n for _ in range(n)]  # Initialize with blank spaces
            self.cell_size = self.canvas_size // n
            self.colors = self.generate_color_gradient(n)
            self.num = 1

            self.canvas.config(width=self.canvas_size, height=self.canvas_size)  # Resize canvas if needed

            self.draw_spiral_animation()
        except ValueError as e:
            print(f"Error: {e}")

    def draw_spiral_animation(self):
        """Draws the animated spiral on the canvas."""
        left, right = 0, len(self.spiral) - 1
        top, bottom = 0, len(self.spiral) - 1

        while left <= right and top <= bottom:
            # Fill from left to right
            for i in range(left, right + 1):
                if self.spiral[top][i] == '':
                    self.spiral[top][i] = str(self.num)
                    self.draw_canvas()
                    self.root.update()
                    self.root.after(50)  # Adjust delay as needed for animation speed
                    self.num += 1
            
            top += 1

            # Fill from top to bottom
            for i in range(top, bottom + 1):
                if self.spiral[i][right] == '':
                    self.spiral[i][right] = str(self.num)
                    self.draw_canvas()
                    self.root.update()
                    self.root.after(50)  # Adjust delay as needed for animation speed
                    self.num += 1
            
            right -= 1

            # Fill from right to left
            for i in range(right, left - 1, -1):
                if self.spiral[bottom][i] == '':
                    self.spiral[bottom][i] = str(self.num)
                    self.draw_canvas()
                    self.root.update()
                    self.root.after(50)  # Adjust delay as needed for animation speed
                    self.num += 1
            
            bottom -= 1

            # Fill from bottom to top
            for i in range(bottom, top - 1, -1):
                if self.spiral[i][left] == '':
                    self.spiral[i][left] = str(self.num)
                    self.draw_canvas()
                    self.root.update()
                    self.root.after(50)  # Adjust delay as needed for animation speed
                    self.num += 1
            
            left += 1

    def generate_color_gradient(self, n):
        """Generates a gradient of colors for the spiral cells."""
        colors = []
        hue_start = 0.6  # Start hue (blue-green)
        hue_end = 0.1    # End hue (purple)
        hue_diff = (hue_end - hue_start) / (n * n)  # Calculate hue difference per cell
        
        for i in range(n * n):
            current_hue = hue_start + i * hue_diff
            rgb_color = colorsys.hsv_to_rgb(current_hue, 1.0, 1.0)
            tk_color = f"#{int(rgb_color[0]*255):02x}{int(rgb_color[1]*255):02x}{int(rgb_color[2]*255):02x}"
            colors.append(tk_color)
        
        return colors

    def draw_canvas(self):
        """Draws the current state of the spiral on the canvas."""
        self.canvas.delete("all")

        for i in range(len(self.spiral)):
            for j in range(len(self.spiral)):
                x0, y0 = j * self.cell_size, i * self.cell_size
                x1, y1 = x0 + self.cell_size, y0 + self.cell_size
                self.canvas.create_rectangle(x0, y0, x1, y1, outline='black', fill='white')
                if self.spiral[i][j] != '':
                    color_index = int(self.spiral[i][j]) - 1
                    text_color = self.colors[color_index]
                    self.canvas.create_text(x0 + self.cell_size//2, y0 + self.cell_size//2, text=self.spiral[i][j], fill=text_color)

def main():
    root = tk.Tk()
    app = SpiralGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
