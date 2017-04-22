import re
import os
import urllib

def read_urls(filename):

    underbar = filename.index('_')

    hostname = filename[underbar + 1:]

    url_dict = {}

    f = open(filename,'rU')

    for line in f:
        match = re.search(r'"GET (\S+)', line)

        if match:
           path = match.group(1)

           if 'puzzle' in path:
               url_dict['http://' + hostname + path] = 1

    return url_dict.keys()

#print read_urls('C:\Python27\logpuzzle\place_code.google.com')


def download_urls(urls, dest_dir):

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    index= file(os.path.join(dest_dir, 'index.html'), 'w')
    index.write('<html><body>\n')

    i=0
    for url in urls:
        localname ='img%d.jpg' % i
        
        urllib.urlretrieve(url, os.path.join(dest_dir, localname))

        

        index.write('<img src="%s">' % localname)

        i +=1


    index.write('\n</body></html>')
    index.close()


def main():

  url = read_urls('C:\Python27\logpuzzle\placesample_code.google.com')

  download_urls(url, 'C:\Python27\logpuzzle\Partha_ultimate_new_another_logfile_practice')


if __name__ == '__main__':
    main()
                  
        

    

    
        
               

        
