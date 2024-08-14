"""You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

# Example 3:
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums
"""

"""Another type of Solution"""


class Solution(object):
    def merge1(self, nums1, m, nums2, n):
        i = j = 0
        sort_arr = []
        while (i < m and m != 0):
            while j < n:
                sort_arr.append(nums2[j])
                j = j + 1
            sort_arr.append(nums1[i])
            i = i + 1
        if (m == 0 and n != 0):
            sort_arr = nums2
        return sorted(sort_arr)

    def merge(self, nums1, m, nums2, n):
        size = len(nums1)
        end = size - 1

        while n > 0 and m > 0:
            if nums2[n - 1] >= nums1[m - 1]:
                nums1[end] = nums2[n - 1]
                n -= 1
            else:
                nums1[end] = nums1[m - 1]
                m -= 1
            end -= 1
        while n > 0:
            nums1[end] = nums2[n - 1]
            n -= 1
            end -= 1
        return nums1


if __name__ == "__main__":
    s = Solution()
    output = s.merge(nums1, m, nums2, n)
    print(output)
