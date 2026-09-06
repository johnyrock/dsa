def group_anagrams(strs):
    groups = {}  # letter-count key -> words with that count
    for word in strs:
        counts = [0] * 26
        for ch in word:
            counts[ord(ch) - ord("a")] += 1
        key = tuple(counts)
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())
