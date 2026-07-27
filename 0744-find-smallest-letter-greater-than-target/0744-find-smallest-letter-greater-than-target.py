class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # letters (str) is stored in increasing order


        for letter in letters:
            if letter > target:
                return letter
        
        return letters[0]

        

            