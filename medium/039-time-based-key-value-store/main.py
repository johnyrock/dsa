from time_based_key_value_store import TimeMap

store = TimeMap()

store.set("foo", "bar", 1)
store.set("foo", "bar2", 4)
store.set("foo", "bar3", 7)
print(store.get("foo", 4))   # bar2
print(store.get("foo", 5))   # bar2
print(repr(store.get("foo", 0)))   # ''
print(store.get("foo", 9))   # bar3
print(repr(store.get("nope", 3)))  # ''
