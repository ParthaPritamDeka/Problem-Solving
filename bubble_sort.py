#Time Complexity O(n)
#Space Complexity O(1)
def bubble_sort(list):
    for i in range(len(list)-1 , 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j+1]
                list[j+1] = list[j]
                list[j] = temp
    return list