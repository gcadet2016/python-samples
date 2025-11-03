import numpy as np
from pathlib import Path

CONFIG_DIR = str(Path.home()) + '\\OneDrive\\Dev\\GitRepositories\\python-samples\\parameters\\numpySettings\\'
# Linux environment example
# CONFIG_DIR = str(Path.home()) + '/numpySettings/'

def save_calibration_params(dist, mtx):
    np.savez(CONFIG_DIR + 'calibration_params.npz', dist_array=dist, mtx_array=mtx)

def load_calibration_params():
    with np.load(CONFIG_DIR + 'calibration_params.npz') as data:
        return data['dist_array'], data['mtx_array']

# Example usage:
if __name__ == "__main__":
    # Save example calibration parameters
    dist_example = np.array([0.1, 0.01, 0.001, 0.0001])
    mtx_example = np.array([[1000, 0, 320], [0, 1000, 240], [0, 0, 1]])
    save_calibration_params(dist_example, mtx_example)
    
    # Load calibration parameters
    dist_loaded, mtx_loaded = load_calibration_params()
    print("Loaded Distortion Coefficients:", dist_loaded)
    print("Loaded Camera Matrix:\n", mtx_loaded)