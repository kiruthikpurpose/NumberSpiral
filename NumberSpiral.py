import os
import time

def print_spiral_animation(n):
    spiral = [[' '] * n for _ in range(n)]  # Initialize with blank spaces
    left, right = 0, n - 1
    top, bottom = 0, n - 1
    num = 1
    
    while left <= right and top <= bottom:
        # Fill from left to right
        for i in range(left, right + 1):
            spiral[top][i] = str(num)
            num += 1
        top += 1
        print_spiral_frame(spiral)
        time.sleep(0.1)

        # Fill from top to bottom
        for i in range(top, bottom + 1):
            spiral[i][right] = str(num)
            num += 1
        right -= 1
        print_spiral_frame(spiral)
        time.sleep(0.1)

        # Fill from right to left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                spiral[bottom][i] = str(num)
                num += 1
            bottom -= 1
            print_spiral_frame(spiral)
            time.sleep(0.1)

        # Fill from bottom to top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                spiral[i][left] = str(num)
                num += 1
            left += 1
            print_spiral_frame(spiral)
            time.sleep(0.1)

def print_spiral_frame(spiral):
    # Clear the screen before printing new frame (for animation effect)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    for row in spiral:
        print(" ".join(f"{x:>2s}" for x in row))  # Align right with a minimum width of 2
    print("\n")

def main():
    n = int(input("Enter the size of the spiral (an integer): "))
    print_spiral_animation(n)

if __name__ == "__main__":
    main()
