# coding=utf-8
"""
collections.Counter 练习
"""
from collections import Counter
words1 = "A counter tool is provided to support convenient and rapid tallies. For example:"
words2 = "A Counter is a dict subclass for counting hashable objects."
words3 = "It is an unordered collection where elements are stored as dictionary keys and their counts are stored as " \
         "dictionary values.Counts are allowed to be any integer value including zero or negative counts. The Counter" \
         " class is similar to bags or multisets in other languages."

cnt1 = Counter(words1.split())
cnt2 = Counter(words2.split())
cnt3 = Counter(words3.split())

print(cnt1)
print(cnt2)
print(cnt3.most_common(3))
print(cnt1.keys())
print(sum(cnt1.values()))
