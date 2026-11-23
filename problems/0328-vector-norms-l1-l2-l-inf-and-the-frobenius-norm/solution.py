
import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:

    if norm_type == 'l1':
        l1_norm = 0.0
        for i in arr.flat:
            l1_norm += abs(i)
        return float(l1_norm)

    elif norm_type == 'l2':
        l2_norm = 0.0
        for i in arr.flat:
            l2_norm += abs(i) ** 2
        return float(np.sqrt(l2_norm))

    elif norm_type == 'linf':
        l_inf = 0.0
        for i in arr.flat:
            l_inf = max(l_inf, abs(i))
        return float(l_inf)

    elif norm_type == 'frobenius':
        if arr.ndim != 2:
            raise ValueError("Frobenius norm requires a 2D array")

        fro_norm = 0.0
        for i in arr.flat:
            fro_norm += abs(i) ** 2
        return float(np.sqrt(fro_norm))

    else:
        raise ValueError("Invalid norm type")
