def string_anagram(s1, s2):

    if sorted(s1) == sorted(s2):
        return True

    return False

print string_anagram('partha', 'tharpaa')
