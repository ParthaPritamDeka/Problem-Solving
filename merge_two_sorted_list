
def merge(list1, list2):
    listm = []
    if len(list1)> 1 and len(list2)> 1:
        
        i = 0
        j = 0
        k = 0
        
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                listm.append(list1[i])
                i = i + 1
            else:
                listm.append(list2[j])
                j = j + 1
            k = k + 1
        while i < len(list1):
            listm.append(list1[i])
            i = i + 1
            k = k + 1
        while j < len(list2):
            listm.append(list2[j])
            j = j + 1
            k = k + 1    
    
    return listm
    

print merge([1,2,3,4,5,6,88,99,100], [22,33,44,55,66,77,88,99])
