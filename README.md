# Animated Spiral Generator
This project generates an animated spiral pattern of numbers in the console using Python. The script fills a square spiral with numbers from 1 up to $n^2$ where $n$ is the size of the spiral entered by the user.
## Versions Overview
### Version 1: Console-Based Animated Spiral Generator
**Features:**
- **Animated Spiral:** Visualizes the filling of a square spiral with numbers in the console.
- **Directional Filling:** Fills the spiral in four directions (left to right, top to bottom, right to left, bottom to top) to create the spiral pattern.
- **Clear Animation:** Clears the console screen between frames for smooth animation effect.
- **Dynamic Size:** Accepts user input for the size of the spiral (n).
### Version 2: Basic Spiral Generator without Color Gradient
**Features:**
- **Simplified Visualization:** Focuses solely on generating the spiral pattern without additional color effects.
- **Clear Spiral Representation:** Provides a straightforward representation of the spiral pattern using text-based characters.
- **User Interaction:** Allows the user to specify the size of the spiral for customized patterns.
### Version 3: Animated Spiral Generator with Color Gradient
**Features:**
- **Enhanced Visualization:** Includes all features from Version 2.
- **Colorful Number Representation:** Enhances the spiral pattern by coloring numbers with a gradient.
- **Dynamic Animation:** Animates the filling of the spiral pattern, with colors changing smoothly from start to end.
- **User-Friendly Interface:** Provides a graphical interface (GUI) for interactive input and visualization of the animated spiral.

#### For Version 1:
Run the following command:
```console
python3 NumberSpiral.py
```

#### For Versions 2 and 3:
Firstly install the libraries with:
```console
pip install -r requirements.txt
```
And then run:
```console
python3 NumberSpiralGUI.py
```
or 
```console
python3 NumberSpiralGUI-Color.py
```
## Using the Application
- Enter the desired size of the spiral in the provided entry field.
- (For Versions 2 and 3) Click "Start Animation" to generate and visualize the animated spiral pattern.
- Observe the spiral pattern filling incrementally within the GUI window.
## Notes
- Adjust the animation speed by modifying the `after()` delay parameter in the respective Python script.
- Ensure sufficient screen space for larger spiral sizes to maintain clarity of the numbers.

## Example execution

### Version 1:
<p align="center">

<img src="https://i.imgur.com/LzSaBPi.png">

</p>

### Version 2:
<p align="center">

<img src="https://i.imgur.com/SR51X0B.png">

</p>

### Version 3:
<p align="center">

<img src="https://i.imgur.com/Shn4c8C.png">

</p>
