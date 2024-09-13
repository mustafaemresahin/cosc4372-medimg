import numpy as np
import matplotlib.pyplot as plt

def generate_ellipse(x0, y0, a, b, angle, intensity, N):
    """
    Generate an ellipse with specified parameters and return a mask.
    :param x0: X position of the center.
    :param y0: Y position of the center.
    :param a: Semi-major axis (width).
    :param b: Semi-minor axis (height).
    :param angle: Rotation angle in degrees.
    :param intensity: Signal intensity of the ellipse.
    :param N: Phantom matrix size.
    :return: Mask representing the ellipse in the phantom.
    """
    y, x = np.ogrid[-N//2:N//2, -N//2:N//2]  # Create a grid for the phantom size
    theta = np.deg2rad(angle)  # Convert angle to radians

    # Rotation matrix
    xr = np.cos(theta) * x + np.sin(theta) * y
    yr = -np.sin(theta) * x + np.cos(theta) * y

    # Generate the ellipse
    mask = ((xr - x0) / a)**2 + ((yr - y0) / b)**2 <= 1
    return mask * intensity  # Return mask with the intensity value

def generate_phantom(N, ellipses):
    """
    Generate a phantom image with ellipses.
    :param N: Phantom matrix size (NxN).
    :param ellipses: List of ellipses parameters.
    :return: Phantom image with ellipses.
    """
    phantom = np.zeros((N, N))
    for ellipse in ellipses:
        x0, y0, a, b, angle, intensity = ellipse
        phantom += generate_ellipse(x0, y0, a, b, angle, intensity, N)
    return phantom

def display_phantoms(ph_list, titles):
    """
    Display all generated phantoms in a single figure.
    :param ph_list: List of phantoms to display.
    :param titles: List of titles for each phantom.
    """
    n = len(ph_list)
    cols = 3
    rows = (n // cols) + (n % cols > 0)  # Determine the number of rows
    
    plt.figure(figsize=(15, 5 * rows))  # Adjust the figure size depending on rows
    
    for i, ph in enumerate(ph_list):
        plt.subplot(rows, cols, i + 1)
        plt.imshow(ph, cmap='gray')
        plt.title(titles[i])
        plt.axis('off')
    
    plt.tight_layout()  # Ensure no overlap between subplots
    plt.show()

# Define ellipses for different phantoms
# Q2.1: Phantom with no overlapping structures
ellipses_no_overlap = [
    (0, 0, 60, 90, 0, 1),
    (0, 0, 50, 80, 0, -0.85),        # Central ellipse
    (-40, -30, 10, 25, 20, 0.4),  # Smaller ellipse moved down
    (-10, 40, 15, 20, -30, 0.65)  # Another small ellipse, shifted
]

# Q2.2: Add two circular structures outside the brain
ellipses_with_circles = ellipses_no_overlap + [
    (100, 80, 20, 20, 0, 0.5),  # Circle on the right
    (-100, 80, 20, 20, 0, 0.5)  # Circle on the left
]

# Q2.3: Phantom with three concentric circles
ellipses_concentric = [
    (0, 0, 60, 90, 0, 1),
    (0, 0, 50, 80, 0, -0.85),
    (0, 0, 35, 35, 0, 0.1),    # Outer circle
    (0, 0, 25, 25, 0, 0.3),      # Middle circle
    (0, 0, 10, 10, 0, 0.6)         # Inner circle
]

# Generate and display the phantoms
N = 256  # Phantom matrix size

# Phantom 1: No overlap
phantom_no_overlap = generate_phantom(N, ellipses_no_overlap)

# Phantom 2: With additional circles
phantom_with_circles = generate_phantom(N, ellipses_with_circles)

# Phantom 3: Concentric circles
phantom_concentric = generate_phantom(N, ellipses_concentric)

# Display all phantoms in one window
phantoms = [phantom_no_overlap, phantom_with_circles, phantom_concentric]
titles = ["Phantom with No Overlap", "Phantom with Added Circles", "Concentric Circles Phantom"]

display_phantoms(phantoms, titles)
