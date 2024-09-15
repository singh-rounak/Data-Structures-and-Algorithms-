class Node:
    def __init__(self, data,next=None):
        self.data = data
        self.next = next #pointer to next_node
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
                
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:  # If the list is empty
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:  # Traverse to the end of the list
                last_node = last_node.next
            last_node.next = new_node

        
    def print_list(self):
        if self.head is None:
            print('List is empty')
            return
        
        iteration = self.head
        list_string =''
        
        while iteration:
            list_string = list_string+ str(iteration.data) + '-->'
            iteration = iteration.next
        
        print(list_string)
            

if __name__ == '__main__':
    obj = LinkedList()
    # obj.insert_at_beginning(5)
    # obj.print_list()
    obj.insert_at_end(2)
    obj.insert_at_end(1)
    obj.insert_at_end(4)
    obj.insert_at_end(8)
    obj.print_list()