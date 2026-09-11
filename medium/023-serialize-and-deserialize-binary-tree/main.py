from serialize_and_deserialize_binary_tree import Codec, TreeNode

codec = Codec()
root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
data = codec.serialize(root)
print(data)
back = codec.deserialize(data)
print(codec.serialize(back) == data)
