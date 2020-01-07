#!/usr/bin/env    python3.7

def counter (n, listx, listy):
    i=1
    T = 0 #TimeMidlleValue
    while i<n:
        T=T+max(abs(listx[i]-listx[i-1]),abs(listy[i]-listy[i-1]))
        i+=1    
    return T

#Insert the number of dots, which should be a positive integer
while True:
    val = input("How many dots would you like to connect? ")
    try:
        n = int(val)
        if(n>1):
            break
        else:
            print("Please enter a positive number larger than 1")
    except ValueError:
        print("Please enter an integer")
        
#Insert coordinate pairs(should be integers) and organize them as lists
lstx = []
lsty = []
count = 1
while count <= n:
    while True:
        val = input("Please enter a coordinate x{}: ".format(count))
        try:
            x = int(val)
            break
        except ValueError:
            print("Please enter an integer")
    while True:
        val = input("Please enter a coordinate y{}: ".format(count))
        try:
            y = int(val)
            break
        except ValueError:
            print("Please enter an integer")
    count +=1
    lstx.append(int(x))
    lsty.append(int(y))
#print(lstx)
#print(lsty)
#test5
#Calculate the time itself
Time = counter (n,lstx,lsty)
print (Time)