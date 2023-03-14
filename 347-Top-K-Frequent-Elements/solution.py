class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Time: O(n)
        Space: O(n)
        """

        # initialise empty bucket list, counter dict and result list
        bucket = [[] for _ in range(len(nums) + 1)]
        counter = {}
        result = []

        # loop through each num in the list
        for num in nums:

            # update counter dict    
            counter[num] = 1 + counter.get(num, 0)
        
        # loop through each num:count pair in the dict
        for num, count in counter.items():

            # add number to their respective bucket
            bucket[count].append(num)
        
        # loop from end
        for i in range(len(bucket)-1, 0, -1):

            # loop through each num in the bucket
            for num in bucket[i]:
                result.append(num)

                # found k most frequent numbers
                if len(result) == k:
                    return result