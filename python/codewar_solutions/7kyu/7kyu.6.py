#Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with the lowest index. If you get an empty array/list, return an empty array/list.

#Don't change the order of the elements that are left.

def remove_smallest(numbers):
    if numbers == []:
        return []
    
    smallest = min(numbers)
    
    new_list = []
    
    removed = False
    
    for n in numbers:
        if n is smallest and not removed:
            removed = True
            
        else:
            new_list.append(n)
            
    return new_list

#Created 20.02.26
