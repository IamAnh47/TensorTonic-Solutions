import numpy as np
def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    X = np.array(values, dtype=float)
    min_val = np.min(X)
    max_val = np.max(X)

    if min_val == max_val:
        return np.zeros_like(X, dtype=int).tolist()

    bin_width = (max_val - min_val)/num_bins

    bin_indices = np.floor((X - min_val)/bin_width)

    bin_indices = np.clip(bin_indices, 0, num_bins - 1)

    return bin_indices.astype(int).tolist()