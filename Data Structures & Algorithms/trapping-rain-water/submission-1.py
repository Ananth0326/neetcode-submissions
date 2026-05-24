class Solution:
    def trap(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0

        total_water = 0

        while left < right:

            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max < right_max:

                water = left_max - height[left]
                total_water += water

                left += 1

            else:

                water = right_max - height[right]
                total_water += water

                right -= 1

        return total_water