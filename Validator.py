#!/usr/bin/env python3

def main():
    while(1):
        val = input("\n>> Enter your 16-digit credit card number: ")
        val = val.replace(" ","")
        
        #Input error checking
        if(len(val) != 16):
            print("The number must be exactly 16 digits!")
            continue
            
        if not val.isdigit():
            print("The number cannot contain letters!")
            continue
            
        return val
                      
def checksum(tempStr):

    substring = tempStr[:-1]
    myList = []
    
    for elem in substring:
        myList.append(int(elem))
            
    i=0    
    while i < len(myList):
        myList[i] = myList[i] * 2
        if(myList[i] >= 10):
            myList[i] = (myList[i] % 10) + 1
        i+=2
        
    sum = 0
    for elem in myList:
        sum = sum + elem
    
    return sum
    
 
if __name__== "__main__":
    val = main()
    
    if ((int(val[-1:]) + checksum(val)) % 10 == 0) :
        print("\nCredit card number is valid ✓\n")
    else:
        print("\nCredit card number is invalid ✗\n");

