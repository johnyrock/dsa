# Define the function that takes a list of words and returns them bucketed into anagram groups.
def group_anagrams(strs):
    # Map from a canonical key to every word that produces that key. Two words are anagrams exactly when their keys are equal.
    groups = {}  # letter-count key -> words with that count
    # Visit each word once. The whole algorithm is one pass with a dictionary lookup per word.
    for word in strs:
        # Build the key as a 26-slot tally, one slot per lowercase letter. This costs O(k) for a word of length k, cheaper than the O(k log k) of sorting the letters.
        counts = [0] * 26
        for ch in word:
            # ord(ch) - ord("a") turns 'a' into 0, 'b' into 1, ... 'z' into 25.
            counts[ord(ch) - ord("a")] += 1
        # Lists cannot be dictionary keys because they are mutable, so freeze the tally into a tuple.
        key = tuple(counts)
        # First time this key is seen: open a new empty bucket for it.
        if key not in groups:
            groups[key] = []
        # Drop the word into its bucket. Anagrams share a key, so they land in the same list.
        groups[key].append(word)
    # The buckets, in first-seen order, are the answer. The problem accepts any group order.
    return list(groups.values())
