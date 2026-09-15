#1
def min_max(nums):
    if len(nums) == 0:
        raise ValueError("список пуст")
    return (min(nums), max(nums))

print(min_max([3, -1, 5, 5, 0]))    
print(min_max([42]))                 
print(min_max([-5, -2, -9]))          
print(min_max([1.5, 2, 2.0, -3.1]))   
print(min_max([])) 

#2
def unique_sorted(nums):
    return sorted(set(nums))

print(unique_sorted([3, 1, 2, 1, 3]))       
print(unique_sorted([]))                      
print(unique_sorted([-1, -1, 0, 2, 2]))        
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))    

#3
def flatten(mat):
    result = []
    for num in mat:
        if type(num) != list and type(num) != tuple:
            raise TypeError("это не список и не кортеж")
        for number in num:
            result.append(number) 
    
    return result

print(flatten([[1, 2], [3, 4]]))       
print(flatten([[1, 2], (3, 4, 5)]))    
print(flatten([[1], [], [2, 3]]))    
print(flatten([[1,2], 'ab']))  








