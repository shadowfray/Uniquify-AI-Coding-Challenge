#Benjamin Jewell

'''
Given a set of data (a list of numbers), and a shape (a list of positive
integers which represents the dimensions of a tensor), the class can
put together the given tensor using .shape_data() and prints it for the
user. Using .checks() we ensure that the data given is the right type,
otherwise we stop the program and return an empty list. 
'''

class Tensor():

    def __init__(self, data, shape):
        self.data = data
        self.shape = shape
        self.tensor = []

        #how many layers is the shape
        self.layers = len(shape)
        
        #how long is the data
        self.dataLength = len(data)

        #the total number of slots we will have so we can calculate
        #if we have too many
        self.total_slots = 1

        #checkpoint to see if inputs are correct
        if self.checks():
            
            #calculates total slots
            for i in shape:
                self.total_slots *= i

            #pads in extra zeroes if needed
            if self.dataLength < self.total_slots:
                for i in range(self.total_slots - self.dataLength):
                    self.data.append(0)

            #removes extra values if there are too many
            if self.dataLength > self.total_slots:
                for i in range(self.dataLength - self.total_slots):
                    self.data.pop(-1)

            #runs the shape data program
            self.shape_data()

        #in the event input is wrong
        else:
            print(self.tensor)
            

    def checks(self):
        '''Takes the values of the shape and ensures that they will conform
        with the proper guidelines. If they do, it returns True, otherwise
        it returns False and prints a statement explaining what went
        wrong.
        '''
        
        #double checks that the shape is a list of positive integers
        for s in self.shape:
            
            if s < 1:
                print('Error: Shape list must contain at least one value.')
                return False
            
            if type(s) != int:
                print('Error: Shape list must only contain positive integers')
                return False

        #in case we get no shape
        if self.shape == None:
            self.total_slots = 0
            return False

        else:
            return True
        

    def shape_data(self):
        '''Takes our data given, and slots it into the proper amount of lists
        to form the tensor. At the end it sets self.tensor to this value for
        future use, and prints it out for the user to see.

        We begin with a copy of the data, which has been pre prepared. From
        there we move down the values of self.shape, and fit the data into
        small lists with the length of that value of self.shape we are
        currently looping through.

        The process repeats until we have gone through every value of
        self.shape and then returns the final tensor.
        '''

        #lets us work with the list without changing the original
        workingList = self.data

        #goes through each value of the shape
        #reads right to left to match the order shape is given in
        for i in range(self.layers-1, 0, -1):

            newList = []
            
            #The shape value of this loop
            groupValue = self.shape[i]

            #loops a number of times equal to the list length divided
            #by the shape value
            for j in range((len(workingList) // groupValue)):

                #the blank list piece we will fill with values before
                #returning to the larger list
                list_piece = []

                #for a number of times equal to our shape value here we
                #put the first value into the list_piece and remove it
                #to avoid repeats
                for k in range(groupValue):
                    list_piece.append(workingList[0])
                    workingList.pop(0)

                #take the new small list and put it inside the bigger list
                newList.append(list_piece)

            #now the newList is shaped, and we can move up a degree to begin
            #again until we reach the end of the shape values
            workingList = newList

        self.tensor = workingList
        print(self.tensor)
