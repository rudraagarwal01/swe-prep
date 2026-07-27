class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num): 
            return sum(int(digit) ** 2 for digit in str(num)) 
            # convert num into a str and return the sum of each digit (converted back to num) squared

        seen = set() # if we see the same number again we know we are in a look
        while n != 1 and n not in seen:
            seen.add(n) # adds number to seen
            n = get_next(n) # runs through the helper method
        return n == 1 
