import re
def extract_names(filename):

    name = []

    dict_rank_name = {}

    f =open(filename, 'r')
    text = f.read()
    match_year = re.search(r'Popularity\sin\s(\d\d\d\d)',text)

    if not match_year:
        sys.stderr.write('could not find year')
        sys.exit(1)
                         
    year = match_year.group(1)
    name.append(year)

    tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)

    for tuple in tuples:
        (rank, boyname, girlname) = tuple
        if boyname not in dict_rank_name:
                dict_rank_name[boyname] = rank
        if girlname not in dict_rank_name:
                dict_rank_name[girlname] = rank

    sorted_name = sorted(dict_rank_name.keys())

    for names in sorted_name:
            name.append(names + " " + dict_rank_name[names])


    return name


print extract_names('C:\\Python27\\babynames\\baby1990.html')
                        
