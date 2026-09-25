class Solution:
    def reverseString(self, s: list[str]) -> None:
        # Does not actually return anything
        left = 0
        right = len(s) - 1

        while left <= right:
            # swap left and right
            temp = s[left]
            s[left] = s[right]
            s[right] = temp

            left += 1
            right -= 1


        