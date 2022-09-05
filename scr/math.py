# -*- coding: utf-8 -*-
# function defined to test pytest local hook
import numpy as np


def calculate_log(x: np.array) -> np.array:
    """_summary_

    Args:
        x (np.array): provide a pandas series

    Returns:
        np.array: natural logarithm of x
    """

    return np.log(x)
