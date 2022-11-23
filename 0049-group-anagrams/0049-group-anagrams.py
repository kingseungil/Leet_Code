import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 존재하지 않는 키를 삽입하려는 경우, keyerror가 발생하므로 defaultdict() 선언
        # 따라서, 매번 키 존재 여부를 체크하지 않고 비교 구문을 생략해 간결하게 구성됨
        anagrams = collections.defaultdict(list)

        for word in strs:
            # 정렬하여 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)
            # print(anagrams)
            # defaultdict(<class 'list'>, {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']})

        return list(anagrams.values())
