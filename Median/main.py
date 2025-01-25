'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Combina os dois arrays e os ordena
        total = sorted(nums1 + nums2)
        
        n = len(total)
        
        # Se o comprimento combinado é par
        if n % 2 == 0:
            mid1 = n // 2  # Índice do meio (superior)
            mid2 = mid1 - 1  # Índice do meio (inferior)
            # Calcula a média dos dois elementos centrais
            return (total[mid1] + total[mid2]) / 2.0
        else:
            # Se o comprimento combinado é ímpar, retorna o elemento do meio
            mid = n // 2
            return total[mid]
