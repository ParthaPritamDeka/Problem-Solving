import re

def extract_name(filename):

    names = []
    
    #f = open('C:\Users\partha.deka\Downloads\google-python-exercises\babynames\baby1990.html','rU')
    f = open(filename, 'rU')

    text = f.read()

    year_match = re.search(r'Popularity\sin\s(\d\d\d\d)', text)
    if not year_match:
        sys.stderr.write('Couldn\'t find the year!\n')
        sys.exit(1)
    year = year_match.group(1)
    names.append(year)


    tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', text)

    names_to_rank = {}

    for rank_tuple in tuples:
      (rank, boyname, girlname) = rank_tuple
      if boyname not in names_to_rank:
        names_to_rank[boyname] = rank
      if girlname not in tuples:
        names_to_rank[girlname]= rank

    sorted_names = sorted(names_to_rank.keys())

    for name in sorted_names:
      names.append(name + " " + names_to_rank[name])

    text = '\n'.join(names)
    g = open('babyname_output.txt', 'w')

  

    g.write(text + '\n')
    f.close()
    g.close()
    
    return names

    



c = extract_name('baby1990.html')

print c







      
    
