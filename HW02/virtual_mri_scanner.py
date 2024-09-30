import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim

# Function to generate an ellipse
def generate_ellipse(x0, y0, a, b, angle, intensity, N):
    y, x = np.ogrid[-N//2:N//2, -N//2:N//2]
    theta = np.deg2rad(angle)
    xr = np.cos(theta) * x + np.sin(theta) * y
    yr = -np.sin(theta) * x + np.cos(theta) * y
    mask = ((xr - x0) / a)**2 + ((yr - y0) / b)**2 <= 1
    return mask * intensity

# Function to generate a phantom
def generate_phantom(N, ellipses):
    phantom = np.zeros((N, N))
    for ellipse in ellipses:
        x0, y0, a, b, angle, intensity = ellipse
        phantom += generate_ellipse(x0, y0, a, b, angle, intensity, N)
    return phantom

# Use the original phantom from Assignment 1 for A-map
ellipses_no_overlap = [
    (0, 0, 60, 90, 0, 1),         # Compartment 1
    (0, 0, 50, 80, 0, 0.85),      # Compartment 2
    (-40, -30, 10, 25, 20, 0.4),  # Compartment 3
    (-10, 40, 15, 20, -30, 0.65)  # Compartment 4
]

# Generate A-map, T1-map, and T2-map using the correct formula for T1 and T2
def generate_physical_properties_maps(N):
    # A-map directly from the phantom configuration
    A_map = generate_phantom(N, ellipses_no_overlap)
    
    # Number of compartments
    num_compartments = 4
    
    # Initialize empty maps for T1 and T2
    T1_map = np.zeros((N, N))
    T2_map = np.zeros((N, N))
    
    # Loop through each compartment and calculate the T1 and T2 values
    for j, ellipse in enumerate(ellipses_no_overlap, 1):  # Start indexing at 1
        x0, y0, a, b, angle, _ = ellipse
        mask = generate_ellipse(x0, y0, a, b, angle, 1, N)  # Get the mask for this compartment
        
        # Calculate T1 and T2 for this compartment based on its index (j)
        T1_value = 250 + (j - 1) * 375
        T2_value = 10 + (j - 1) * 25
        
        # Assign T1 and T2 values to the corresponding areas in the map
        T1_map += mask * T1_value
        T2_map += mask * T2_value
    
    return A_map, T1_map, T2_map

# Step 1: Generate A-map, T1-map, T2-map
N = 256
A_map, T1_map, T2_map = generate_physical_properties_maps(N)

# Save and display A-map, T1-map, and T2-map
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(A_map, cmap='gray')
axes[0].set_title("A-map (Water Content)")
axes[0].axis('off')

axes[1].imshow(T1_map, cmap='gray')
axes[1].set_title("T1-map (Longitudinal Relaxation)")
axes[1].axis('off')

axes[2].imshow(T2_map, cmap='gray')
axes[2].set_title("T2-map (Transverse Relaxation)")
axes[2].axis('off')

plt.tight_layout()
plt.savefig('A_T1_T2_maps.png', dpi=300)
plt.show()

# Step 2: Define acquisition parameters for MRI images
TR_values = [50, 250, 1000, 2500]
TE_values = [10, 10, 10, 10]

# Signal intensity calculation
def calculate_signal_intensity(A, T1, T2, TR, TE):
    return A * (1 - np.exp(-TR / T1)) * np.exp(-TE / T2)

# Compute the signal intensity for each acquisition parameter
def compute_signal_intensities(A_map, T1_map, T2_map, TR_values, TE_values):
    si_maps = []
    for TR, TE in zip(TR_values, TE_values):
        si_map = calculate_signal_intensity(A_map, T1_map, T2_map, TR, TE)
        si_maps.append(si_map)
    return si_maps

# Compute the signal intensity for each acquisition parameter
si_maps = compute_signal_intensities(A_map, T1_map, T2_map, TR_values, TE_values)

# Display and save the MRI images with different TR and TE values
fig, axes = plt.subplots(1, 4, figsize=(20, 5))
for i, ax in enumerate(axes):
    ax.imshow(si_maps[i], cmap='gray')
    ax.set_title(f"TR={TR_values[i]}, TE={TE_values[i]}")
    ax.axis('off')

plt.tight_layout()
plt.savefig('MRI_images_TR_TE.png', dpi=300)
plt.show()

### Q.2.3: Plot SI vs TR for all compartments ###
# Prepare to plot SI vs TR
plt.figure(figsize=(8, 6))

# Loop through compartments and calculate SI for different TR values
for i, ellipse in enumerate(ellipses_no_overlap):
    A = ellipse[5]
    T1 = 250 + (i * 375)
    T2 = 10 + (i * 25)
    
    # Calculate SI for each TR value
    SI_values = [calculate_signal_intensity(A, T1, T2, TR, 10) for TR in TR_values]
    
    # Plot the results
    plt.plot(TR_values, SI_values, marker='o', label=f"Compartment {i + 1}")

# Set plot details for SI vs TR
plt.title("SI vs TR for Each Compartment (TE=10)")
plt.xlabel("TR")
plt.ylabel("Signal Intensity (SI)")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save and show the SI vs TR plot
plt.savefig('SI_vs_TR.png', dpi=300)
plt.show()

### Q.2.4: Fix TR=250, vary TE for compartment 2 ###
# TE values to test
TE_values_vary = [10, 40, 80, 150]
TR_fixed = 250  # TR is fixed at 250 for this part

# Parameters for compartment 2
A_comp2 = 0.85
T1_comp2 = 625
T2_comp2 = 35

# Compute signal intensities for compartment 2
si_comp2 = []
for TE in TE_values_vary:
    si = A_comp2 * (1 - np.exp(-TR_fixed / T1_comp2)) * np.exp(-TE / T2_comp2)
    si_comp2.append(si)

# Plot SI vs TE for compartment 2 and save the plot
plt.figure(figsize=(8, 5))
plt.plot(TE_values_vary, si_comp2, marker='o')
plt.title("SI vs TE for Compartment 2 (TR=250)")
plt.xlabel("TE")
plt.ylabel("Signal Intensity (SI)")
plt.grid(True)
plt.savefig('SI_vs_TE_comp2.png', dpi=300)
plt.show()

# Step 4: Compute SSIM between pairs of images
ssim_1_2 = ssim(si_maps[0], si_maps[1], data_range=si_maps[1].max() - si_maps[1].min())
ssim_1_3 = ssim(si_maps[0], si_maps[2], data_range=si_maps[2].max() - si_maps[2].min())
ssim_1_4 = ssim(si_maps[0], si_maps[3], data_range=si_maps[3].max() - si_maps[3].min())

# Save SSIM results to a text file
ssim_results = {
    "SSIM between Image 1 and Image 2": ssim_1_2,
    "SSIM between Image 1 and Image 3": ssim_1_3,
    "SSIM between Image 1 and Image 4": ssim_1_4,
}

with open('SSIM_results.txt', 'w') as f:
    for key, value in ssim_results.items():
        f.write(f"{key}: {value}\n")

# Print SSIM results
print(ssim_results)
