#Task
#create a method all which takes two params:

#a sequence
#a function
#and returns true if the function in the params returns true for every element in the sequence. Otherwise, it should return false. If the sequence is empty, it should return true, since technically nothing failed the test.

def _all(seq, fun): 
    # your code here
    if not seq: #empty sequence is true
        return True
    
    for element in seq:
        if not fun(element):
            return False
    return True
    
    
