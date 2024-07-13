import tkinter as tk

class SpiralGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Animated Spiral")

        # Welcome message
        self.welcome_label = tk.Label(self.root, text="Welcome to the animated spiral generator!", font=("Helvetica", 16, "bold"))
        self.welcome_label.pack(pady=10)

        # Entry field for spiral size
        self.n_label = tk.Label(self.root, text="Enter size of spiral:")
        self.n_label.pack()
        
        self.n_entry = tk.Entry(self.root)
        self.n_entry.pack()

        # Start animation button
        self.start_button = tk.Button(self.root, text="Start Animation", command=self.start_animation)
        self.start_button.pack(pady=10)

        # Canvas for drawing spiral
        self.canvas_size = 800  # Initial canvas size
        self.canvas = tk.Canvas(self.root, width=self.canvas_size, height=self.canvas_size, bg='white')
        self.canvas.pack()

        self.cell_size = 0
        self.num = 1
        self.spiral = []

    def start_animation(self):
        """Starts the animation of drawing the spiral."""
        try:
            n = int(self.n_entry.get())
            if n <= 0:
                raise ValueError("Size must be a positive integer")
            
            self.spiral = [[''] * n for _ in range(n)]  # Initialize with blank spaces
            self.cell_size = self.canvas_size // n
            self.num = 1

            self.canvas.config(width=self.canvas_size, height=self.canvas_size)  # Resize canvas if needed

            self.draw_spiral_animation()
        except ValueError as e:
            print(f"Error: {e}")

    def draw_spiral_animation(self):
        """Draws the spiral animation on the canvas."""
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

    def draw_canvas(self):
        """Draws the current state of the spiral on the canvas."""
        self.canvas.delete("all")

        for i in range(len(self.spiral)):
            for j in range(len(self.spiral)):
                x0, y0 = j * self.cell_size, i * self.cell_size
                x1, y1 = x0 + self.cell_size, y0 + self.cell_size
                self.canvas.create_rectangle(x0, y0, x1, y1, outline='black', fill='white')
                if self.spiral[i][j] != '':
                    self.canvas.create_text(x0 + self.cell_size//2, y0 + self.cell_size//2, text=self.spiral[i][j])

def main():
    root = tk.Tk()
    app = SpiralGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
