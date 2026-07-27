class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if the strings can even have a common divisor
        # str1: ABCABC, str2: ABC
        # str1 + str2 = ABCABCABC
        # str2 + str1 = ABCABCABC
        if str1 + str2 != str2 + str1:
            return ""
        
        # Find the GCD of the lengths of the two strings
        gcd_len = math.gcd(len(str1), len(str2))

        # Return the prefix of that GCD length (e.g. "AB")
        return str1[:gcd_len]