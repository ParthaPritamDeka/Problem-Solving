
def comp(s1, s2):

     dict1 = {}
     list =[]
  
     for i in s1:
         dict1[i] = 1

     print dict1

     for j in s2:
         if dict1.get(j) is None:
             list.append(j)
             
     return ''.join(list)


print comp('abcdfefghijklmnopqrstuv6346756676287826kjhgeygashdvh', '23145653786386868089578979987932876786yuterfgjgdshshjgfyhjgfdybdshguhyugyagbcghcjdshvjghjcdgyuddgcdkyugckyug')

         
