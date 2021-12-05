"""
Given a sorted array of n integers that has been rotated an unknown
number of times, write code to find an element in the array. You may assume that the array was
originally sorted in increasing order.
EXAMPLE
Input:find5in{15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
Output: 8 (the index of 5 in the array)
"""

def seatch(nums, target):
    if not nums:
        return -1

    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid

        if nums[mid] > nums[left]:
            # left side is sorted normally
            if nums[left] <= target and target < nums[mid]:
                # target is on left side
                right = mid - 1
            else:
                left = mid + 1

        elif nums[mid] < nums[left]:
            # right side is normally sorted
            if nums[mid] < target and target <= nums[right]:
                # target is on right side
                left = mid + 1
            else:
                right = mid - 1

        else:
            if nums[mid] != nums[right]:
                # all values between left and mid should equal
                # so search right
                left = mid + 1

            else:
                # search both right and left side






