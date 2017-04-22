def interlace(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
    max_len = max(len_s1, len_s2)
    #new_string =''
    list = []
    for i in range(max_len):
      if len_s1 > len_s2:
         if i < len_s2:
           #new_string = new_string + s1[i] + s2[i]
             list.append(s1[i])
             list.append(s2[i])
         else :
           #new_string = new_string + s1[i]
             list.append(s1[i])
      else:
         if i < len_s1:
           #new_string = new_string + s1[i] + s2[i]
             list.append(s1[i])
             list.append(s2[i])
         else:
            #new_string = new_string + s2[i]
             list.append(s2[i])

    return ''.join(list)

print interlace('abcdefgh','ij')

#print interlace('ij','abcdefgh')

print interlace('ij', 'ab')
