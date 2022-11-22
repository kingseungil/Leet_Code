# https://velog.io/@yoopark/r-prefix-in-regexp
# 정규 표현식 설명

import collections
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.sub('[^\w]', ' ', paragraph).lower().split()
        words = filter(lambda x: x not in banned, words)

        # Counter 객체 이용
        counts = collections.Counter(words)
        # 가장 흔하게 등장하는 단어(most_common(1))의 첫 번째 인덱스[0][0] 리턴
        return counts.most_common(1)[0][0]
