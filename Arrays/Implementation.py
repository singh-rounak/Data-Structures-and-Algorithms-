class Array:
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.array = [None]*size #Initializing with None

    def __str__(self):
        return str(self.array)

    def is_full(self):
        return self.count == self.size
    
    def is_empty(self):
        return self.count == 0
    
    def insert(self, element):
        if self.is_full():
            raise Exception("Array Full")
        self.array[self.count] = element
        self.count +=1

    def get(self, index):
        if index < 0 or index >= self.count:
            return IndexError
        return self.array[index]

    def set(self, index, element):
        if index < 0 or index >= self.count:
            raise IndexError
        self.array[index] = element


    def delete(self, index):
        if index < 0 or index >= self.count:
            raise IndexError
        #shift elements to the left
        for i in range(index, self.count - 1):
            self.array[i] = self.array[i+1]
        self.array[self.count -1] = None
        self.count -=1

    def search(self,element):
        for i in range(self.count):
            if i == element:
                return i #retuen the index
        return -1 #not found
    
    def traverse(self):
        for i in range(self.count):
            print(self.array[i], end ='')
        print()
            

#instantiate an object to run code:

my_array = Array(5)
# print("initial array = ",my_array)

# # #Inserting elements:
my_array.insert(10)
my_array.insert(20)
my_array.insert(30)

#print(my_array)

element = my_array.get(1)
print('element =', element)

my_array.set(1,25)
print('after updating index 1 to 25:', my_array)

my_array.delete(2)
print('after deleting at index 2:', my_array)