class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        word_dict: dict[str, List] = defaultdict(list)

        for each_word in strs:
            factorized_word = "".join(sorted(list(each_word)))
            word_dict[factorized_word].append(each_word)
        
        return [each_val for each_val in word_dict.values()]