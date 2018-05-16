import re
import collections

with open("/home/ubuntu/workspace/1155-0.txt") as f:
    text = f.read().lower()
    
print(text[9990:10100])

words = text.split(" ")
print(words[:100])

words = re.findall('\w+', text)
print(words[:100])


big_words = [word for word in words if len(word) >= 10]

print(collections.Counter(big_words).most_common(10))

print(collections.Counter(words).most_common(10))