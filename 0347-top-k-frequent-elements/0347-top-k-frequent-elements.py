class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return the elements that show up the most (return k elements)
        # can sort the array first and use two pointer to add amount of same element
        # can use a dictionary to store the frequency of each element and return top k elements

        # create result array
        res = []

        count = Counter(nums)

        # create an array of empty lists where index represents frequency 
        # The max possible frequency is len(nums), so we need an array of size len(nums) + 1
        freq = []
        for _ in range(len(nums) + 1):
            freq.append([])
        
        # Group numbers by their frequency
        # 'c' is the frequency, so we put the 'num' into the list at index 'c'
        for num, c in count.items():
            freq[c].append(num)

        # iterate from the highest possible frequency down to 1
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                # Once we have k elements, we are done
                if len(res) == k:
                    return res

        
