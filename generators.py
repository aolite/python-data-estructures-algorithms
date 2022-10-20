# Compares the running type between two functions

import time

#Generator function creates an iterator of odd functions. 

def oddGen (n,m): 
    while n<m: 
        yield n
        n+=2

#Same function with list

def oddList (n,m):
    lst = []
    while n<m:
        lst.append (n)
        n+=2
    return lst

# The time it takes to perform sum on an iterator
t1= time.time()
sum (oddGen (1,1000000))
print("Time to sum an iterator: %f" % (time.time() - t1))

# The time it takes to perform sum on a list

t1= time.time()
sum (oddList (1,1000000))
print("Time to sum an list: %f" % (time.time() - t1))