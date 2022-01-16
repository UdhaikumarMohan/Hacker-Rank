# Find the the lcm of the given number:
# Maximum number in the list has been considered as an LCM and verify it.

a = [3,4,10]

def LCM(a):
  
    count=0
    
    i=0
    
    lcm = max(a)
    
    while not count==len(a):

        if lcm % a[i] == 0:

            count+=1
            i+=1
          
        else:

            count = 0
            i=0
            lcm = lcm+len(a)

    if count==len(a):

        return(lcm)

LCM(a)
