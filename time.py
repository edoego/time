#!/usr/bin/env    python3.7

#Insert the number of dots, which should be a positive integer
while True:
    val = input("How many dots would you like to connect today? ")
    try:
        n = int(val)
        if(n>1):
            break
        else:
            print("Please enter a positive number larger than 1")
    except ValueError:
        print("Please enter a number")
        
#Insert coordinate pairs and organize them as lists
lstx = []
lsty = []
count = 1

while count <= n:
    x = input("Please enter a coordinate x{}: ".format(count))
    y = input("Please enter a coordinate y{}: ".format(count)) 
    count +=1
    lstx.append(int(x))
    lsty.append(int(y))

print(lstx)
print(lsty)

#Calculate the time itself
i=1
T = 0 #Time

while i<n:
    T=T+max(abs(lstx[i]-lstx[i-1]),abs(lsty[i]-lsty[i-1]))
    i+=1
print(T)
