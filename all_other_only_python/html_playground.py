
from bs4 import BeautifulSoup

def options(soup, id):
    option_values = []
    carrier_list = soup.find(id=id)
    for option in carrier_list.find_all('option'):
        option_values.append(option['value'])
    return option_values

def print_list(label, codes):
    print "\n%s:" % label
    for c in codes:
        print c

def main():
    soup = BeautifulSoup(open("Data Elements.html"))

    #print soup

    codes = options(soup, 'CarrierList')
    print_list("Carriers", codes)

    codes = options(soup, 'AirportList')
    #print_list("Airport", codes)
    


if __name__ == '__main__':
    main()
