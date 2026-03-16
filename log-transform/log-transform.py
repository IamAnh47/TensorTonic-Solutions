import numpy as np

def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    X = np.array(values, dtype=float)

    return np.log(1.0 + X)