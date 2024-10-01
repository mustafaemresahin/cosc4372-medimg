# Virtual MRI Scanner Simulation

This project simulates a simple virtual MRI scanner using a modified Shepp-Logan phantom. It generates water content (A-map), longitudinal relaxation time (T1-map), and transverse relaxation time (T2-map) maps. It also computes and plots the signal intensity (SI) for different TR (repetition time) and TE (echo time) values, along with SSIM (Structural Similarity Index) comparisons between generated images.

## Table of Contents
1. [Installation](#installation)
2. [Running the Code](#running-the-code)
3. [Project Files](#project-files)
4. [Libraries and Packages](#libraries-and-packages)

---

## Installation

1. Clone the repository or download the project folder.
2. Ensure that you have Python 3.8+ installed on your machine.
3. Install the required libraries using `pip` by running the following command.

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains the following dependencies:

```txt
numpy==1.19.5
matplotlib==3.3.4
scikit-image==0.18.1
```

## Running the Code

1. Open a terminal in the project folder.
2. Run the Python script `virtual_mri_scanner.py` using a command.

```bash
python virtual_mri_scanner.py
```

3. The script will generate the following outputs:
   - A-map, T1-map, and T2-map images.
   - MRI images for various TR and TE values.
   - Plots of Signal Intensity (SI) vs. TR and SI vs. TE.
   - SSIM comparison results between different MRI images.

All generated images will be saved in the project directory.

---

## Project Files

The project contains the following files:

- **virtual_mri_scanner.py**: The main Python script to simulate the virtual MRI scanner, generate maps, calculate signal intensity, and plot the results.
- **requirements.txt**: A list of required Python packages and their versions.
- **README.md**: Instructions on how to install and run the code.

### Output Files
- `A_T1_T2_maps.png`: Visualization of A-map, T1-map, and T2-map.
- `MRI_images_TR_TE.png`: MRI images generated for various TR and TE values.
- `SI_vs_TR.png`: Plot showing Signal Intensity vs. TR for each compartment.
- `SI_vs_TE_comp2.png`: Plot showing Signal Intensity vs. TE for Compartment 2.
- `SSIM_results.txt`: A text file containing SSIM comparison results between the generated MRI images.

---

## Libraries and Packages

This project requires the following Python libraries:

1. **NumPy** (for numerical operations): Used for array manipulations and numerical calculations.
   
2. **Matplotlib** (for plotting): Used for generating visual plots for maps and signal intensity.

3. **Scikit-Image** (for image processing): Used for calculating SSIM (Structural Similarity Index) between generated images.

---

### Note

- Make sure your system has Python 3.8+ and `pip` installed before running the project.

- Ensure that all required libraries are installed using the `pip` command.

```bash
pip install -r requirements.txt
```