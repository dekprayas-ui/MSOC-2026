def unique_element(arr):
    unique = []
    for i in arr : 
        if i not in unique:
            unique.append(i)
    return unique


user_input = input("Enter elements for array : ")
arr = user_input.split()
result = unique_element(arr)    
print(f"unique elements are : {result}")