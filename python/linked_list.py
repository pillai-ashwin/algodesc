class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = Node()
    
    # Method to add elements to the linked list
    def append(self,data):
        new_node = Node(data)
        currently_pointing_at = self.head
        while currently_pointing_at.next != None:
            currently_pointing_at = currently_pointing_at.next
        currently_pointing_at.next = new_node
    
    # Method to calculate the length of the linked list
    def length(self):
        currently_pointing_at = self.head
        lengthoflinkedlist = 0
        while currently_pointing_at.next != None:
            lengthoflinkedlist +=1
            currently_pointing_at = currently_pointing_at.next
        return(lengthoflinkedlist)
    
    # Method to remove with a choice of first or last or 1st occurence of an element in the list
    def remove(self,choice = ""):
        currently_pointing_at = self.head
        if choice == "first":
            self.head = currently_pointing_at.next
        if choice == "last":
            while currently_pointing_at.next.next != None:
                currently_pointing_at = currently_pointing_at.next
            currently_pointing_at.next = None
        else:

    # Display the linked list in the form of a list
    def display(self):
        elements_of_linkedlist = []
        currently_pointing_at = self.head
        while currently_pointing_at.next != None:
            currently_pointing_at = currently_pointing_at.next
            elements_of_linkedlist.append(currently_pointing_at.data)
        print(elements_of_linkedlist)
   
        