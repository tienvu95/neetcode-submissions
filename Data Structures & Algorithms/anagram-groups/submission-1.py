class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        temp = {}
        for s in strs:
            sorted_str = "".join(sorted(s))
            temp.setdefault(sorted_str, []).append(s)

        # 2. Extract just the lists
        result = list(temp.values())

        return(result)