from lru_cache import LRUCache


def run(capacity, ops):
    # ops is a list of ("get", key) or ("put", key, value); returns the list of get results
    cache = LRUCache(capacity)
    out = []
    for op in ops:
        if op[0] == "get":
            out.append(cache.get(op[1]))
        else:
            cache.put(op[1], op[2])
    return out


def test_lru_cache():
    cases = [
        # (capacity, ops, expected get results)
        (2, [("put", 1, 1), ("put", 2, 2), ("get", 1), ("put", 3, 3), ("get", 2),
             ("put", 4, 4), ("get", 1), ("get", 3), ("get", 4)], [1, -1, -1, 3, 4]),
        (1, [("put", 2, 1), ("get", 2), ("put", 3, 2), ("get", 2), ("get", 3)], [1, -1, 2]),   # capacity 1
        (2, [("get", 5)], [-1]),                                                                 # get on empty cache
        (2, [("put", 1, 1), ("put", 1, 10), ("get", 1)], [10]),                                  # update existing key
        (2, [("put", 1, 1), ("put", 2, 2), ("put", 1, 100), ("put", 3, 3), ("get", 1), ("get", 2)], [100, -1]),  # update counts as a use, 2 is evicted
        (2, [("put", 1, 1), ("put", 2, 2), ("get", 1), ("get", 2), ("put", 3, 3), ("get", 1), ("get", 2)], [1, 2, -1, 2]),  # get reorders, 1 is evicted
        (3, [("put", 1, 1), ("put", 2, 2), ("put", 3, 3), ("put", 4, 4), ("get", 4), ("get", 3), ("get", 2), ("get", 1),
             ("put", 5, 5), ("get", 1), ("get", 2), ("get", 3), ("get", 4), ("get", 5)], [4, 3, 2, -1, -1, 2, 3, -1, 5]),
        (2, [("put", 2, 1), ("put", 2, 2), ("get", 2), ("put", 1, 1), ("put", 4, 1), ("get", 2)], [2, -1]),  # same key put twice does not fill two slots
        (2, [("put", 0, 0), ("get", 0)], [0]),                                                   # value 0 must not be confused with a miss
    ]

    failures = 0
    for capacity, ops, expected in cases:
        result = run(capacity, ops)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            failures += 1
        print(f"{status}  capacity={capacity}, ops={len(ops)} -> {result} (expected {expected})")

    print(f"\n{len(cases) - failures}/{len(cases)} passed")


test_lru_cache()
