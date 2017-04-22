import commands

def listdir(dir):
    cmd = 'cd' + ' ' + dir

    print "Command to Run:", cmd
    (status, output) = commands.getstatusoutput(cmd)

    if status:
        sys.stderr.write(output)
        
        sys.exit(1)
    print output

listdir('C:\Python27')
    

    
