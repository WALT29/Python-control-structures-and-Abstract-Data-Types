"""
CONTROL STRUCTURES - sequence control ,loop control ,decision control

Sequence control 
    one section of the code is executed first before the other

Decision control 
    a section of the code will be executed based on whether a condition is met
    if else elif
    
Loop control
    a block of code is executed repeatedly for a particular number of times until the condition is met
    for ,while

"""

#DECISION CONTROL

#1) if else
age =18
if age >=18:
    print("you are allowed to drink and drive")
else:
    print("sorry you are too young")
    
pin=1234
user_entered_pin=2345

if pin == user_entered_pin:
    print("welcome")
else:
    print("wrong password")
    
#2) if elif
household=45000
if household<=12000:
    print("you are in band 1")
elif household>12000 and household<=34000:
    print("you are in band 3")
elif household>34000 and household<=50000:
    print("you are in band 4")
elif household>50000:
    print("you are in band 4")
    
#LOOP CONTROL
#1)for
#for loop is used to itterate over a sequence that can be either a (list ,tupple ,dict,string,set)
fruits=["banana","mango","apple","orange"]
for fruit in fruits:
    print(fruit)

#looping through a string
for x in "banana":
    print(x)

#Break statement
"""
with the break statement you can stop the loop before it loops through all the items 
"""
for fruit in fruits:
    print(fruit) ## banana mango apple
    if fruit=="apple":
        break ##stops the loop at apple

for fruit in fruits:
    if fruit=="mango":
        print("fruit name:",fruit) ## banana mango apple
        break ##stops the loop at apple

#Continue statement
"""
with the continue statement we can stop the current itteration of the loop and continue with the next
"""
for fruit in fruits:
    if fruit =="banana": ##this code doesnt print banana ,since it stops the current itteration and continues to the next 
        continue
    print(fruit) #mango ,apple orange

##range() function 
"""
range(start,stop,step)
range(6)-values of 0 to 6
"""
for i in range(6):
    print(i) #0,1,2,3,4,5

for i in range(2,6):
    print(i) #2,3,4,5

for i in range(0,10,2):
    print(i) #0,2,4,6,8
    
for i in range(10,0,-1):
    print("decrement :",i)
    
##Else in for loop
"""
else keyword in for loop specifies the block of code to be executed when the loop is finished
"""
for i in range(6):
    print(i)
else:
    print("loop is finshed") #this line is executed when the loop is finshed 
    
##Nested loops -is a loop inside a loop
    """
    the inner loop will be executed one time for each iteration of the outter loop
    """
colors=["black","red","yellow","white"]
wrestlers=["roman","john","rhea","dom"]

for color in colors:
    for wrestler in wrestlers:
        print(color,wrestler)
        
##pass statement
    """
    for loops cannot be left empty bt if for some reason you need to leave it empty use the pass statement to avoid getting an error
    for x in range (6):
        pass
    """

## 2)While loop
    """
    in javascript a while loop looks like this:
        let i=0;
        while (i<5){
            console.log(i)
            i++
        }
    
    in python this is the format
        i=0 -initialization variable
        while i<5:
            print(i)
            i +=1 remember to increment by one or the while loop will be forever
    
    """

i=0
while i<5: ##0,1,2,3,4
    print(i)
    i +=1;

i=10
while i>=0: #9,8,7,6,5,4,3,2,1,0
    print(i)
    i -=1

#break statement -breaks the loop if the condition is true
num=0
while num <7:
    print(num)
    if num ==5: #the loop is broken when the num is equal to 5
        break
    num +=1

#continue statement -stops the current iteration and continues to the next

number=0
while number <9:
    number +=1
    if number ==6: ##doesnt print 6
        continue
    print(number)
   