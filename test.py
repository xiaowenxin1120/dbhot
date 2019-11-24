# class Node():
#     def __init__(self, item):
#         self.item = item  # 根节点
#         self.left = None  # 左节点
#         self.right = None  # 右节点
#
#
# class Tree(object):
#     def __init__(self):
#         self.root = None
#
#     def addNode(self, item):
#         node = Node(item)
#         # 插入第一个节点的情况
#         if self.root == None:
#             self.root = node
#             return
#         cur = self.root
#         q = [cur]  # 列表元素是我们进行遍历判断的节点
#         while q:
#             nd = q.pop(0)
#             if nd.left == None:
#                 nd.left = node
#                 return
#             else:
#                 q.append(nd.left)
#             if nd.right == None:
#                 nd.right = node
#                 return
#             else:
#                 q.append(nd.right)
#
#     # 层级遍历
#     def travel(self):
#         cur = self.root
#         q = [cur]
#         while q:
#             nd = q.pop(0)
#             print(nd.item)
#             if nd.left:
#                 q.append(nd.left)
#             if nd.right:
#                 q.append(nd.right)
#
#     # 前序：根左右
#     def forwoar(self,root):
#         if root == None:
#             return
#         print(root.item)
#         self.forwoar(root.left)
#         self.forwoar(root.right)
#
#     def middle(self,root):#前序:左根右
#         if root == None:
#             return
#         self.middle(root.left)
#         print(root.item)
#         self.middle(root.right)
#
#     def back(self,root):#前序:左右根
#         if root == None:
#             return
#         self.back(root.left)
#         self.back(root.right)
#         print(root.item)
#
#
#
# tree = Tree()
# tree.addNode(1)
# tree.addNode(2)
# tree.addNode(3)
# tree.addNode(4)
# tree.addNode(5)
# tree.addNode(6)
# tree.addNode(7)
# # tree.travel()
# # tree.forwoar(tree.root)
# # tree.middle(tree.root)
# tree.back(tree.root)


def find(alist,item):
    find = False
    first = 0
    last = len(alist) - 1

    while first < last:
        mid_index = (first + last) // 2
        if alist[mid_index] < item:
            first = mid_index + 1
        elif alist[mid_index] < item:
            last = mid_index - 1
        else:
            find = True
            break
    return find

print(find([1,2,3,4,5,6,7,8],31))







