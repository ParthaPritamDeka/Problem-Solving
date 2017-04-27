def func(num, target):
    list = []
    for i in range(len(num)):
        for j in range(i+1 ,len(num), 1):
            if (num[i] + num[j]) == target:
                list.append(i)
                list.append(j)
                break
        if len(list) !=0:
                break
    return list

def main():
    print func([3,2,4], 6)

if __name__ == '__main__':
    main()