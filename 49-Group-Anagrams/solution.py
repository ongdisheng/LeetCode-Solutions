import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Time: O(m * n)
        Space: O(n)
        """

        # initialize empty dict 
        result_dict = collections.defaultdict(list)

        # loop through each string in the list
        for i in range(len(strs)):

            # used to store char count for each string 
            char_count = [0] * 26

            # loop through each char in the string
            for char in strs[i]:

                # update char count
                char_count[ord(char) - ord('a')] += 1
            
            # key: char count
            # value: string
            result_dict[tuple(char_count)].append(strs[i])

        return result_dict.values()