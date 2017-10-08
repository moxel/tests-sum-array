import random
import json
import numpy as np

def predict(data):
    result = np.sum(data.to_numpy())
    return {
        'sum': result
    }
