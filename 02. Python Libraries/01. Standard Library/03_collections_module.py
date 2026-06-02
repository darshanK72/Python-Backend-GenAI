# 03 — collections (Counter, defaultdict, deque)
# Run: python 03_collections_module.py

from collections import Counter, defaultdict, deque

# --- 1. Counter — count items ---
votes = ["apple", "banana", "apple", "cherry", "apple", "banana"]
counts = Counter(votes)
print("counts:", counts)
print("most common:", counts.most_common(2))

# --- 2. defaultdict — default value for missing keys ---
words_by_letter = defaultdict(list)
for word in ["apple", "ant", "banana", "bear"]:
    words_by_letter[word[0]].append(word)
print("by letter:", dict(words_by_letter))

# --- 3. deque — fast append/pop from both ends ---
queue = deque([1, 2, 3])
queue.append(4)
queue.appendleft(0)
print("deque:", list(queue))
queue.pop()
print("after pop:", list(queue))
