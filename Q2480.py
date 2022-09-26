#Baekjoon Question 2480
import collections
trials = map (int, input().split())
counter = collections.Counter(trials)
key_value = counter.most_common(1)[0][0]

if max(counter.values()) == 1:
    max(counter)
    print("{}".format(100 * max(counter)))
elif max(counter.values()) == 2:
    print("{}".format(1000 + 100 * key_value ))
else:
    print("{}".format(10000 + 1000 * key_value))