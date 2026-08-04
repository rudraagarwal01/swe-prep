class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a dictionary to store key (num) -> value (freq)

        # this tells it that when a new value needs to be created it will be an int
        count = defaultdict(int)

        # adds to frequency for each num
        for num in nums:
            # num is the key
            count[num] += 1
        
        stack = []
        # iterate through our dictionary and swap key and value
        for num, freq in count.items():
            stack.append([freq, num])
        # sort it so that the greatest frequency goes to the end
        stack.sort()

        # create result array
        res = []
        # continue until k elements
        while len(res) < k:
            res.append(stack.pop()[1])
        return res




# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         # return the elements that show up the most (return k elements)

#         # create result array
#         res = []

#         count = Counter(nums)

#         # create an array of empty lists where index represents frequency 
#         # The max possible frequency is len(nums), so we need an array of size len(nums) + 1
#         freq = []
#         for _ in range(len(nums) + 1):
#             freq.append([])
        
#         # Group numbers by their frequency
#         # 'c' is the frequency, so we put the 'num' into the list at index 'c'
#         for num, c in count.items():
#             freq[c].append(num)

#         # iterate from the highest possible frequency down to 1
#         for i in range(len(freq) - 1, 0, -1):
#             for num in freq[i]:
#                 res.append(num)
#                 # Once we have k elements, we are done
#                 if len(res) == k:
#                     return res
        
