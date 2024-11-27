
# Simple program to display the recursion of a program

def printFun(test):
    
    if (test < 1):
        return
    else:
        print(test, end=" ")
        printFun(test-1)
        print(test, end=" ")
        return
test = 3     
printFun(test)