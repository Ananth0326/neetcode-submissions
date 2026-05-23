class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        z = sorted(nums)
        result = []

        for i in range(len(z)):

            if i > 0 and z[i] == z[i - 1]:
                continue

            fixed = z[i]

            left = i + 1
            right = len(z) - 1

            while left < right:

                total = fixed + z[left] + z[right]

                if total == 0:

                    result.append([fixed, z[left], z[right]])

                    left += 1
                    right -= 1

                    while left < right and z[left] == z[left - 1]:
                        left += 1

                    while left < right and z[right] == z[right + 1]:
                        right -= 1

                elif total > 0:

                    right -= 1

                else:

                    left += 1

        return result