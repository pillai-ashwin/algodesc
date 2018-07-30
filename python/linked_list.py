class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = Node()
    
    # method to add elements to the linked list
    def append(self,data):
        new_node = Node(data)
        currently_pointing_at = self.head
        while currently_pointing_at.next != None:
            currently_pointing_at = currently_pointing_at.next
        currently_pointing_at.next = new_node
    
    # method to calculate the length of the linked list
    def length(self):
        currently_pointing_at = self.head
        lengthoflinkedlist = 0
        while currently_pointing_at.next != None:
            lengthoflinkedlist +=1
            currently_pointing_at = currently_pointing_at.next
        return(lengthoflinkedlist)
    
    #