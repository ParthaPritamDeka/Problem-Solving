def convert(S, num_rows):
    if num_rows == 1:
        return S
    step, zigzag = 2*num_rows - 2, ""
    
    for i in range(num_rows):
        for j in range(i,len(S),step):
            zigzag += S[j]
            if 0< i< num_rows-1 and j + step - 2*i < len(S):
                zigzag += S[j + step - 2*i]
    return zigzag

print convert("PAYPALISHIRING", 3)