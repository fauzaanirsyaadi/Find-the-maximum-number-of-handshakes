'''
### Find the maximum number of handshakes ###

# There are N persons in a room.
# Find the maximum number of Handshakes possible.
# Given the fact that any two persons shake hand exactly once.
# each person should shake hand with every other person in the room

# function to find all 
# possible handshakes
'''
def handshake(n): 
    '''
    # when n becomes 0 that means 
    # all the persons have done
    # handshake with other
    '''
    if (n == 0):
        return 0
    else:
        return int((n * (n - 1)) / 2)
        # another code
        # return (n - 1) + handshake(n - 1) 
# Driver Code
n = 5
print(handshake(n))
