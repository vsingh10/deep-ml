import numpy as np

def cosine_similarity(v1, v2):
    """
    Calculate the cosine_similarity of two vectors.
    Args:
        vec1 (numpy.ndarray): 1D array representing the first vector.
        vec2 (numpy.ndarray): 1D array representing the second vector.
    Returns:
        The cosine_similarity of the two vectors.
    """
    # Implement your code here
    prod = []
    dot = 0.0
    l2_v1 = 0.0
    l2_v2 = 0.0
    cos = 0.0
    for i in range(len(v1)):
        prod.append(v1[i] * v2[i])

    for j in range(len(prod)):
        dot += prod[j]

    for k in range(len(v1)):
        l2_v1 += (v1[k]**2)
    
    for l in range(len(v2)):
        l2_v2 += (v2[l]**2)

    cos = dot / ((np.sqrt(l2_v1)) * (np.sqrt(l2_v2)))

    return cos
    