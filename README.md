# Fourier Series Drawer

This project is an interactive visualizer for drawing and animating Fourier series using Python's Tkinter library. You can draw any shape with the mouse, and the program will use Fourier series to create an animated approximation of your drawing.

## Features

- **Interactive Drawing**: Click and drag to draw a shape on the canvas.
- **Fourier Series Animation**: Visualize the Fourier series approximation of your drawing in real-time.
- **Customizable Terms**: Change the number of Fourier terms (`n`) using the input field to adjust the accuracy of the approximation.

## Customization

- **`width`, `height`**: Dimensions of the canvas window (default: `800x800`).
- **`rel_factor`**: Factor to control the speed of the animation (default: `10000`).
- **`scale`**: Scale factor for rendering the Fourier series (default: `100`).
- **`n`**: Number of Fourier series terms for approximation (default: `50`).

## Usage

1. Run the script using Python:

    ```bash
    python fourier_series_drawer.py
    ```

2. Draw any shape by clicking and dragging on the canvas.

3. Adjust the number of Fourier terms using the input field and click "subm" to apply the changes.

4. The animation will start automatically after you finish drawing.

## Dependencies

This project uses the following Python libraries:

- `tkinter`
- `numpy`

Install the required packages using `pip`:

```bash
pip install numpy
