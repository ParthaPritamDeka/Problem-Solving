def not_bad(s):

    n = s.find('not')
    b = s.find('bad')

    if n != -1 and b != -1 and b>n:
        s = s[:n] + 'good' + s[b+3:]

    return s

def main():

    print not_bad('this thing is not that bad')


if __name__ == '__main__':
    main()
