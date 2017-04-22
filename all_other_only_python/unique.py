def unique(list):
 output = []
 for x in list:
  if x not in list:
    output.append(x)
 return output

 unique([1, 1, 1, 1, 2, 3, 3, 4, 5, 6, 6, 7, 7, 7])
 
