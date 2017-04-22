import sys
def error_handling(filename):

   try:
     f = open (filename, 'r')
     text = f.read()
     f.close()
   except IOError:
     sys.stderr.write('problem reading:' + ' ' + filename)

error_handling('partha.html')
     
