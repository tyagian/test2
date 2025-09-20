"""Array Product Calculator

This module provides a function to calculate the product of all elements in a list,
excluding the element at each position.
"""

from typing import List

def calculate_products(nums: List[int]) -> List[int]:
    """Calculate the product of all elements in a list, excluding the element at each position.

    Args:
        nums (List[int]): A list of integers.

    Returns:
        List[int]: A new list where each element is the product of all elements in the original list, excluding the element at that position.
    """
    if not nums:
        return []

    if len(nums) == 1:
        return [0]

    products = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if j != i:
                product *= nums[j]
        products.append(product)

    return products

# Example usage
print(calculate_products([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
print(calculate_products([0, 1, 2]))     # Output: [2, 0, 0]
print(calculate_products([]))           # Output: []
print(calculate_products([5]))          # Output: [0]