class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # if candies[i] + extraCandies > greatest_candies -> true 

        output = []

        greatest_candy = max(candies)

        for candy in candies:
            if candy + extraCandies >= greatest_candy:
                output.append(True)
            else:
                output.append(False)
        return output

        