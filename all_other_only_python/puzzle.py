import os
import re
import sys
import urllib
def url_sort_key(url):
  """Used to order the urls in increasing order by 2nd word if present."""
  match = re.search(r'-(\w+)-(\w+)\.\w+', url)
  if match:
    return match.group(2)
  else:
    return url

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  # LAB(begin solution)
  # Extract the hostname from the filename
  underbar = filename.index('_')
  host = filename[underbar + 1:]

  # Store the ulrs into a dict to screen out the duplicates
  new_url_dict = {}

  f = open(filename, 'r')
  for line in f:
    # Find the path which is after the GET and surrounded by spaces.
    match = re.search(r'"GET\s(\S+)', line)
    # Above uses \S (upper case S) which is any non-space char
    # Alternately could use square brackets: "GET ([^ ]+)"
    # or the ? form: "GET (.+?) "

    if match:
      path = match.group(1)
      # Add to dict if it's a special "puzzle" url
      # (could combine this 'puzzle' check with the above GET extraction)
      new_match =re.search(r'puzzle', path)
      if new_match:
         #print 'http://' + host + path
         if 'http://' + host + path in new_url_dict.keys():
              new_url_dict['http://' + host + path] += 1
         else:
              new_url_dict['http://' + host + path] = 1
        
  #for key in sorted(new_url_dict.keys(), key=url_sort_key):
    #print key  

  return sorted(new_url_dict.keys(), key=url_sort_key)

def download_images(img_urls, dest_dir):
 

  if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)
    

  index_file = open(os.path.join(dest_dir, 'index__new.html'), 'w')
  index_file.write('<html><body>\n')

  i = 0
  for img_url in img_urls:
    local_name = 'img%d' % i
    print 'Retrieving image file %s and creating image %s' % (img_url, local_name)
    urllib.urlretrieve(img_url, os.path.join(dest_dir, local_name))

    index_file.write('<img ="%s" from url = "%s">' % (local_name, img_url))
    i += 1

  index_file.write('\n</body></html>\n')
  index_file.close()
  
  

c = read_urls('animal_code.google.com')
#print c

download_images(read_urls('animal_code.google.com'), 'C:\Python27\logpuzzle\Partha_output_new')

#C:\Python27\logpuzzle\



