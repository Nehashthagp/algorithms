# Given an array of strings, group anagrams together.
#
# Example:
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]

anagrams_list = ['bat', 'tab', 'eat', 'tea', 'hub', 'buh', 'traingle', 'integral', 'tan']
for m in range(len(anagrams_list)):
    word1 = anagrams_list[m]
    for n in range(m + 1, len(anagrams_list)):
        word2 = anagrams_list[n]
        count = 0
        first_anagrams = list(word1)
        second_anagrams = list(word2)
        new_list = []
        if len(first_anagrams) == len(second_anagrams):
            for i in range(len(first_anagrams)):
                for j in range(len(second_anagrams)):
                    if first_anagrams[i] == second_anagrams[j]:
                        count = count + 1

                        if count == len(first_anagrams):
                            new_list.append(word1)
                            new_list.append(word2)
                            print(new_list)
