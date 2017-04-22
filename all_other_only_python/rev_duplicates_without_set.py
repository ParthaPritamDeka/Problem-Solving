def rem_dup(s):

    list = []
    for i in s:
        if i not in list:
            list.append(i)

    return ''.join(list)

print rem_dup('aaaaaaaaaaaaaaaabbbbbbbbbbccccccccccccccdddddddddddeeeeeeeeeefffffff')
