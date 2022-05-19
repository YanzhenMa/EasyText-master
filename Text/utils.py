"""一些插件
"""
from typing import List
import numpy as np


def matrix_to_list(array: list) -> List[str]:
    """二维列表转一维列表

    Args:
        list ([type]): [description]

    Returns:
        List[str]: [description]
    """
    if array:
        if isinstance(array[0], list):
            res = sum(array, [])
        else:
            res = array
        return res
    else:
        return array


def get_std(array: list) -> float:
    """[求一个列表的标准差]

    Args:
        array (list): [description]

    Returns:
        flot: [description]
    """
    if array:
        nums = np.array(array)
        result = float(np.std(nums))
        return round(result, 4)
    else:
        return 0
