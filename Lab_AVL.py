#Maximiliano David
import sys
from bigtree import Node as BTNode, Tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


def getHeight(node):
    if not node:
        return 0
    return node.height

def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)

def updateHeight(node):
    if node:
        node.height = 1 + max(getHeight(node.left), getHeight(node.right))

def rotate_right(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    updateHeight(y)
    updateHeight(x)

    return x

def rotate_left(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    updateHeight(x)
    updateHeight(y)

    return y

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if not node:
            return Node(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        else:
            return node
       
        updateHeight(node)
       
        balance = getBalance(node)

        if balance > 1 and getBalance(node.left) >= 0:
            node=rotate_right(node)
        elif balance > 1 and getBalance(node.left) < 0:
            node.left = rotate_left(node.left)
            node=rotate_right(node)
        elif balance < -1 and getBalance(node.right) <= 0:
            node=rotate_left(node)
        elif balance < -1 and getBalance(node.right) > 0:
            node.right = rotate_right(node.right)
            node=rotate_left(node)
       
        return node
  
    def delete(self, value):
        self.root = self._delete_recursivo(self.root, value)

    def _delete_recursivo(self, node, value):
        if not node:
            return node
        if value < node.value:
            node.left = self._delete_recursivo(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursivo(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                siguiente = self._min_value_node(node.right)
                node.value = siguiente.value
                node.right = self._delete_recursivo(node.right, siguiente.value)

        if not node:
            return node

        updateHeight(node)
        equilibrio = getBalance(node)

        if equilibrio > 1 and getBalance(node.left) >= 0:
            return rotate_right(node)
        if equilibrio > 1 and getBalance(node.left) < 0:
            node.left = rotate_left(node.left)
            return rotate_right(node)
        if equilibrio < -1 and getBalance(node.right) <= 0:
            return rotate_left(node)
        if equilibrio < -1 and getBalance(node.right) > 0:
            node.right = rotate_right(node.right)
            return rotate_left(node)

        return node
    
    def _min_value_node(self, node):                          
        current = node
        while current.left:
            current = current.left
        return current

    def inorder(self):                                       
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def display(self):
        def build(avl_node, parent=None):
            if not avl_node:
                return None
            label = f"{avl_node.value} (b={getBalance(avl_node)})"
            bt_node = BTNode(label, parent=parent)
            build(avl_node.left, bt_node)
            build(avl_node.right, bt_node)
            return bt_node

        root_bt = build(self.root)
        if root_bt:
            Tree(root_bt).show()

avl = AVLTree()
values_to_insert = [10, 20, 30, 40, 50, 25]

print("Insertando valores:", values_to_insert)
for val in values_to_insert:
    avl.insert(val)

print("\n--- Después de inserciones ---")
avl.display()
print("In-order:", avl.inorder())

print("\n--- Eliminando 40 ---")
avl.delete(40)
avl.display()
print("In-order:", avl.inorder())

print("\n--- Eliminando 10 ---")
avl.delete(10)
avl.display()
print("In-order:", avl.inorder())
