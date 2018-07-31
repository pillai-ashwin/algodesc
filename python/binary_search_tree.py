class Node:
    def __init__(self,value=None):
        self.value = value
        self.leftchild = None
        self.rightchild = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value,self.root)
    
    def _insert(self,value,current_node):
        # case when element is lesser than value at the node
        if value < current_node.value:
            if current_node.leftchild == None:
                current_node.leftchild = Node(value)
            else:
                self._insert(value,current_node.leftchild)
        # case when element is greater than value at the node
        elif value > current_node.value:
            if current_node.rightchild == None:
                current_node.rightchild = Node(value)
            else:
                self._insert(value,current_node.rightchild) 
        # case for when the element is same element exists 
        else:
            print("Value already in tree!")
    
    def display(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self,current_node):  
        if current_node != None:
            self._print_tree(current_node.leftchild)
            print(str(current_node.value))
            self._print_tree(current_node.rightchild)
    
    def height(self):
        if self.root != None:
            return self._height(self.root,0)
        else:
            return 0
    
    def _height(self,current_node,current_height):
        if current_node ==  None:
            return current_height
        leftheight = self._height(current_node.leftchild, current_height + 1)
        rightheight = self._height(current_node.rightchild, current_height + 1)
        return max(leftheight,rightheight)

    def search(self,value):
        if self.root != None:
            return self._search(value,self.root)
        else:
            return False
    
    def _search(self,value,current_node):
        if value == current_node.value:
            return True
        elif value < current_node.value and current_node.leftchild != None:
            return self._search(value,current_node.leftchild)
        elif value > current_node.value and current_node.rightchild != None:
            return self._search(value,current_node.rightchild)
        return False
