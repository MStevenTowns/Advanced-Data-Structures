'''
Authors: 
Michael Steven Towns
Collin Neal
Zakaria El-Awadi

CSC325 
Final Project - Signal Ranges
November 10, 2016
'''

#link to the problem
#https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/signal-range/

#to allow the stack data structure to be used
from Stack import Stack

def computeRanges(heights):
    #declare variables for use later
    s = Stack()
    ranges = []
    
    #cycle through each tower
    for i in range(len(heights)):
        #default value of done. this ensures the while loop will execute at least once
        done = False
        
        #if there are values in the stack and we haven't found a height greater than the current
        #if there are no values in the stack the range is not limited by height
        while not(s.isEmpty() or done):
            
            #if height of current tower is greater than the height at the top of the stack, pop and repeat
            if heights[i] >= heights[s.peek()]:
                s.pop()
            
            #if current height is less than the height at the top of the stack, stop looking
            #this means that we have found the maximum range of the tower
            else: 
                done = True
        
        #if we ran out of values to check, the range is the number of towers to the left, plus the current tower
        #(1+towers to the left) (0-(-1)=1)
        if s.isEmpty():
            #this value is -1 because the list starts at index 0, and subtraction means that this adds 1 to the range
            rng = -1
            
        #otherwise it is the number of towers to the left, until it finds a tower it can't pass
        else:
            rng = s.peek()
            
        #take the place of the current tower, subtract the furthest tower it can reach, that is the range
        #place of current tower-place of furthest tower
        ranges.append(i-rng)
        
        #push the current tower to the stack as the minimum needed to increase range
        s.push(i)
    #return the range of each tower
    return ranges
    
#open the file
test = open("Input.txt","r")

#check how many cases will follow
cases = int(test.readline())
#print(cases)

#loop through the cases
for i in range(cases):
    
    #how many towers will be included in this case
    #this line is used to increment the pointer to the next line, the value is not used
    towers = int(test.readline())
    #print(towers)
    
    #read the heights from the file
    #remove any trailing white space and split the line by spaces and stor it into a list
    heights = test.readline().strip().split()
    #print(heights)
    
    #go through each element in the list, strip any trailing whitespace, then cast the string element to an int
    heights = [int(h.strip()) for h in heights]
    #print(heights)
    
    #call computeRanges() using the list of heights and print out the list that follows
    print(computeRanges(heights))
