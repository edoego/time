#!/usr/bin/env    python2.7

def chronos (n, lstx, lsty):
    i=1
    T = 0 #TimeMidlleValue
    while i<n:
        T=T+max(abs(lstx[i]-lstx[i-1]),abs(lsty[i]-lsty[i-1]))
        i+=1    
    return T
    
def main():
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
    #Calculate the time itself
    Time = chronos (n,lstx,lsty)
    print (Time)

if __name__ == '__main__':
    main()