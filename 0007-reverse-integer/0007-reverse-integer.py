class Solution:
    def reverse(self, x: int) -> int:        
        result = 0
      
        # Define 32-bit integer boundaries
        MIN_INT = -(2**31)      # -2147483648
        MAX_INT = 2**31 - 1     # 2147483647
      
        while x != 0:
            # Check for potential overflow before multiplying by 10
            # If result * 10 would exceed boundaries, return 0
            if result < MIN_INT // 10 + 1 or result > MAX_INT // 10:
                return 0
          
            # Extract the last digit
            digit = x % 10
          
            # Handle negative numbers: Python's modulo returns positive remainder
            # For negative x, we need to adjust the digit to be negative
            if x < 0 and digit > 0:
                digit -= 10
          
            # Build the reversed number
            result = result * 10 + digit
          
            # Remove the last digit from x
            # Using (x - digit) ensures proper division for negative numbers
            x = (x - digit) // 10
          
        return result
