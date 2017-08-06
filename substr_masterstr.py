def findsub(p, s):
    list = []
    j = len(s)
    for i in range(len(p)):
        k = 0
        if p[i] == s[0]:
            while k < j:
                if p[i+k] == s[k]:
                    list.append((s[k],i+k))
                k = k + 1
                
    return list


print findsub('xyzabcmnopqrstabc', 'abc')
            
