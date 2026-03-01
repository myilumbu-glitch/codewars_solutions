#An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

def is_isogram(string):
    #your code here
    string = string.lower()
    seen = set() #what we have seen is collected here
    
    for letter in string:
        if letter in seen:
            return False
        seen.add(letter)
        
    return True
