'''
ECOO '21 P1  solotion
https://dmoj.ca/problem/ecoo21p1
'''

clock = int(input())
interval = int(input())
msg  = int(input())
counter = 0 #for keeping intervals in checks.
while (True):    
    clock += interval
    counter += 1
    if (clock >=msg ):
        print (clock)
        break
    elif (counter == 3): # No more checking after 3 times interval
        print("Who knows...")
        break
