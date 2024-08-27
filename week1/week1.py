import nltk
from nltk.book import text7

text_list = list(text7)
print(len(text_list))

text_set = set(text_list)

print(len(text_set))

hash_map = {}

for item in text_list:
    if item not in hash_map:
        hash_map[item] = 1
    else:
        hash_map[item] += 1

frequent = sorted(hash_map.items(), key=lambda x: -x[1])
print(frequent[:20])

