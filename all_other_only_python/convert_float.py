import re
def get_oline_cost(data):

    non_decimal = re.compile(r'[^\d]+')

    actual_cost = non_decimal.sub('',data)

    if actual_cost != '' and actual_cost != 'NULL':
        return float(actual_cost)
    else:
        return 0.0

def main():
    print get_oline_cost('ParthaLoni45')



if __name__ == '__main__':
    main()
    
    
