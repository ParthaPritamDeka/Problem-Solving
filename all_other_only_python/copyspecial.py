import sys
import re
import os
import shutil
import commands

def get_special_paths(dir):

    filenames = os.listdir(dir)

    pathnames = []

    for filename in filenames:
        match = re.search(r'(__)\w+(__)',filename)
        if match:
            actualpath = os.path.join(dir, filename)
            absolutepath = os.path.abspath(actualpath)
            if not absolutepath in pathnames:
                pathnames.append(absolutepath)
            else:
                sys.stderr.write('Duplicate filenames in the directory')

    #str = '\n'.join(pathnames)
    #return str
    return pathnames



def copy_to(paths,dir):

    if not os.path.exists(dir):
     os.mkdir(dir)
    for filepath in paths:
     fname = os.path.basename(filepath)
     shutil.copy(filepath, dir)
     #os.path.join(dir, fname)


def zip_to(paths, zipfile):
  """Zip up all of the given files into a new zip file with the given name."""
  cmd = 'zip -j ' + zipfile + ' ' + ' '.join(paths)
  print "Command I'm going to do:" + cmd
  (status, output) = commands.getstatusoutput(cmd)
  # If command had a problem (status is non-zero),
  # print its output to stderr and exit.
  if status:
    sys.stderr.write(output)
    sys.exit(1)     


s = get_special_paths('C:\Python27\copyspecial')

zip_to(s, 'partha_zip.zip')


#new_dir = 'C:\Python27\copyspecial\Output'

#copy_to(s, new_dir)


            
#c = get_special_paths('C:\Python27\copyspecial')
#print c



    
