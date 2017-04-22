def findMissingNumber3(array1, array2):
    result=0
    for num in array1+array2:
        result^=num
    return result

print findMissingNumber3([1,2,6,5,3,4], [2,5,6,1,3])
