from collections import Counter


def topKFrequent(nums, k):  # pass

    counter = Counter(nums)
    a = []
    b = counter.most_common(k)
    for i in b:
        a.append(i[0])
    print(a)


if __name__ == "__main__":
    topKFrequent([1, 1, 1, 2, 2, 3], 2)
