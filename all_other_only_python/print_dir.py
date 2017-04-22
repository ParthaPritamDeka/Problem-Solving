import os
import shutil
def printdir(dir):
    filenames = os.listdir(dir)

    dir_file_list = []
    
    for filename in filenames:
        #print filename
        #print os.path.join(dir, filename)
        #file_path = os.path.join(dir, filename)
        dir_file_list.append(os.path.join(dir, filename))
        
        #print os.path.abspath(os.path.join(dir, filename))
    #os.mkdir('C:\Python27\Partha_new_dir')
        #shutil.copy(os.path.join(dir, filename), 'C:\Python27\Partha_new_dir')
    #return filenames
    return dir_file_list       

#printdir('C:\Python27')
c = printdir('C:\Python27')
print c
