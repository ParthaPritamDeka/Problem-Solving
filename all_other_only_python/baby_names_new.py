
import re

def baby_names(filename):

    names = []

    f = open(filename, 'r')

    file = f.read()

    year_match = re.search('Popularity\s\in\s(\d\d\d\d)', file)

    if not year_match:
        sys.stderr.write('couldn\'t find the year! \n')
        sys.exit(1)

    year = year_match.group(1)

    names.append(year)

    tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', file)

    names_rank_dict = {}

    for name_rank in tuples:
        (rank, boyname, girlname) = name_rank
        if boyname not in names_rank_dict.keys():
           names_rank_dict[boyname] = rank
        if girlname not in names_rank_dict.keys():
           names_rank_dict[girlname] = rank

    sorted_dict = sorted(names_rank_dict.keys())

    for name in sorted_dict:
        names.append(name + " " + names_rank_dict[name])

    text = '\n'.join(names)    

    g = open(filename + '.summary', 'w')

    g.write(text)

    f.close()
    g.close()

    return names

c = baby_names('baby2006.html')
        
    
