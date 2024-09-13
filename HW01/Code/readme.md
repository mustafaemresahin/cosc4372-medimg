# COSC 4372 - Medical Imaging - HW1

This project generates Shepp-Logan phantoms with modifications for MRI simulations. As part of the homework assignment, this project includes visualizations of:
1. A phantom with no overlapping structures.
2. A phantom with additional circular structures.
3. A phantom with concentric circles.

## Requirements

The following libraries are required to run the code:

- **numpy**: 1.23.0
- **matplotlib**: 3.5.0

You can install them using the provided `requirements.txt` file.

## Setup

1. **Extract the downloaded ZIP file**:
   Extract the contents of the ZIP file to a directory on your machine.

2. **Create a virtual environment** (optional but recommended):

   - Open a terminal or command prompt and navigate to the extracted folder.
   - Create and activate a virtual environment to isolate dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use .\venv\Scripts\activate
   ```

3. **Install dependencies**:

    - Install the necessary Python packages using requirements.txt:

    ```bash
    pip install -r Code/requirements.txt
    ```

4. Run the project:

    - After installing the dependencies, you can run the Python code:

    ```bash
    python Code/main.py
    ```

5. **View the Output**:

    - The output is displayed in a single window.
    - The window contains the three generated phantoms shown together:
      - Phantom with no overlapping structures.
      - Phantom with additional circular structures.
      - Phantom with concentric circles.

## Notes

- The phantoms are generated using the `generate_phantom()` function, which takes parameters to create and customize ellipses (size, position, rotation, and intensity).
- The `display_phantoms()` function displays all the generated phantoms in a single window, arranged in a grid format.
- Ensure that all necessary dependencies are installed before running the code (`numpy` and `matplotlib`).
- It is recommended to use a virtual environment to manage dependencies and avoid conflicts with other projects.
