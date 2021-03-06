class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return len(self.items)


class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)
    '''
    From terminal -
    >>> nums = [1]
    >>> num = 3
    >>> nums.insert(0, num)
    >>> print(nums)
    [3, 1]
    '''
    #we peek the last element of list and when we insert both left and right children
    #into list, we insert left child first at index 0 and then right child at index 0
    #The above snippet shows that when right child is added to list at index 0, the
    #previous left child value gets pushed to the next position, which is why we use
    #self.items[-1].value to peek(we get the last element of list(the left child))
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return len(self.items)




class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def printTraversal(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder(tree.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder(tree.root)
        elif traversal_type == "reverseorder":
            return self.reverseorder(tree.root)
        else:
            print("Traversal type " + traversal_type + "is not supported")
            return False


    def preorder(self, start, traversal):
        "root -> left -> right"
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal

    def inorder(self, start, traversal):
        "left -> root -> right"
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder(start.right, traversal)
        return traversal

    def postorder(self, start, traversal):
        "left -> right -> root"
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def levelorder(self, start):
        if start is None:
            return
        traversal = ""
        queue = Queue()
        queue.enqueue(start)

        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            peekedNode = queue.dequeue()

            if peekedNode.left:
                queue.enqueue(peekedNode.left)
            if peekedNode.right:
                queue.enqueue(peekedNode.right)

        return traversal

    def reverseorder(self, start):
        if start is None:
            return

        traversal = ""
        queue = Queue()
        stack = Stack()

        queue.enqueue(start)

        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:
            element = stack.pop()
            traversal += str(element.value) + "-"

        return traversal

    def height(self, node):
        if node is None:
            return -1

        leftHeight = self.height(node.left)
        rightHeight = self.height(node.right)

        return 1 + max(leftHeight, rightHeight)

    def sizeIterative(self):
        if self.root is None:
            return 0

        stack = Stack()

        stack.push(self.root)
        size = 1
        while len(stack) > 0:
            node = stack.pop()
            #size += 1
            if node.left:
                stack.push(node.left)
                size += 1
            if node.right:
                stack.push(node.right)
                size += 1
        return size

    def sizeRecursive(self, node):
        if node is None:
            return 0
        return 1 + self.sizeRecursive(node.left) + self.sizeRecursive(node.right)
        #function within Binary Tree class called recursively,
        #so must call as self.sizeRecursive



#                The constructed tree
#level 1                     1
#                         /     \
#level 2                 2       3
#                       / \     / \
#level 3               4   5   6   7
#                     /
#level 4             8

#level 1
tree = BinaryTree(1)

#level 2
tree.root.left = Node(2)
tree.root.right = Node(3)

#level 3
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

#level 4
tree.root.left.left.left = Node(8)

print(tree.printTraversal("preorder")) #O/P -> 1-2-4-8-5-3-6-7-
print(tree.printTraversal("inorder")) #O/P -> 8-4-2-5-1-6-3-7-
print(tree.printTraversal("postorder")) #O/P -> 8-4-5-2-6-7-3-1-
print(tree.printTraversal("levelorder")) #O/P -> 1-2-3-4-5-6-7-8-
print(tree.printTraversal("reverseorder")) #O/P -> 8-4-5-6-7-2-3-1-
print(tree.height(tree.root.left)) #O/P -> 2
print(tree.sizeIterative()) #O/P -> 8
print(tree.sizeRecursive(tree.root)) #O/P -> 8
