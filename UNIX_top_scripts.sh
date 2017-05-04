

How to print/display the first line of a file?
There are many ways to do this. However the easiest way to display the first line of a file is using the [head] command.

$> head -1 file.txt
No prize in guessing that if you specify [head -2] then it would print first 2 records of the file.

Another way can be by using [sed] command. [Sed] is a very powerful text editor which can be used for various text manipulation purposes like this.

$> sed '2,$ d' file.txt

 	
You may be wondering how does the above command work? OK, the 'd' parameter basically tells [sed] to delete all the records from display output from line no. 2 to last line of the file (last line is represented by $ symbol). Of course it does not actually delete those lines from the file, it just does not display those lines in standard output screen. So you only see the remaining line which is the first line.

How to print/display the last line of a file?
The easiest way is to use the [tail] command.

$> tail -1 file.txt
If you want to do it using [sed] command, here is what you should write:

$> sed -n '$ p' test
From our previous answer, we already know that '$' stands for the last line of the file. So '$ p' basically prints (p for print) the last line in standard output screen. '-n' switch takes [sed] to silent mode so that [sed] does not print anything else in the output.

How to display n-th line of a file?
The easiest way to do it will be by using [sed] I guess. Based on what we already know about [sed] from our previous examples, we can quickly deduce this command:

$> sed –n '<n> p' file.txt
You need to replace <n> with the actual line number. So if you want to print the 4th line, the command will be

$> sed –n '4 p' test
Of course you can do it by using [head] and [tail] command as well like below:

$> head -<n> file.txt | tail -1
You need to replace <n> with the actual line number. So if you want to print the 4th line, the command will be

$> head -4 file.txt | tail -1
How to remove the first line / header from a file?
We already know how [sed] can be used to delete a certain line from the output – by using the'd' switch. So if we want to delete the first line the command should be:

$> sed '1 d' file.txt
But the issue with the above command is, it just prints out all the lines except the first line of the file on the standard output. It does not really change the file in-place. So if you want to delete the first line from the file itself, you have two options.

Either you can redirect the output of the file to some other file and then rename it back to original file like below:

$> sed '1 d' file.txt > new_file.txt
$> mv new_file.txt file.txt
Or, you can use an inbuilt [sed] switch '–i' which changes the file in-place. See below:

$> sed –i '1 d' file.txt
How to remove the last line/ trailer from a file in Unix script?
Always remember that [sed] switch '$' refers to the last line. So using this knowledge we can deduce the below command:

$> sed –i '$ d' file.txt
How to remove certain lines from a file in Unix?
If you want to remove line <m> to line <n> from a given file, you can accomplish the task in the similar method shown above. Here is an example:

$> sed –i '5,7 d' file.txt
The above command will delete line 5 to line 7 from the file file.txt

How to remove the last n-th line from a file?
This is bit tricky. Suppose your file contains 100 lines and you want to remove the last 5 lines. Now if you know how many lines are there in the file, then you can simply use the above shown method and can remove all the lines from 96 to 100 like below:

$> sed –i '96,100 d' file.txt   # alternative to command [head -95 file.txt] 
But not always you will know the number of lines present in the file (the file may be generated dynamically, etc.) In that case there are many different ways to solve the problem. There are some ways which are quite complex and fancy. But let's first do it in a way that we can understand easily and remember easily. Here is how it goes:

$> tt=`wc -l file.txt | cut -f1 -d' '`;sed –i "`expr $tt - 4`,$tt d" test
As you can see there are two commands. The first one (before the semi-colon) calculates the total number of lines present in the file and stores it in a variable called “tt”. The second command (after the semi-colon), uses the variable and works in the exact way as shows in the previous example.
How to check the length of any line in a file?
We already know how to print one line from a file which is this:

$> sed –n '<n> p' file.txt
Where <n> is to be replaced by the actual line number that you want to print. Now once you know it, it is easy to print out the length of this line by using [wc] command with '-c' switch.
$> sed –n '35 p' file.txt | wc –c
The above command will print the length of 35th line in the file.txt.
How to get the nth word of a line in Unix?
Assuming the words in the line are separated by space, we can use the [cut] command. [cut] is a very powerful and useful command and it's real easy. All you have to do to get the n-th word from the line is issue the following command:

cut –f<n> -d' '
'-d' switch tells [cut] about what is the delimiter (or separator) in the file, which is space ' ' in this case. If the separator was comma, we could have written -d',' then. So, suppose I want find the 4th word from the below string: “A quick brown fox jumped over the lazy cat”, we will do something like this:
$> echo “A quick brown fox jumped over the lazy cat” | cut –f4 –d' '
And it will print “fox”
How to reverse a string in unix?
Pretty easy. Use the [rev] command.

$> echo "unix" | rev
xinu
How to get the last word from a line in Unix file?
We will make use of two commands that we learnt above to solve this. The commands are [rev] and [cut]. Here we go.

Let's imagine the line is: “C for Cat”. We need “Cat”. First we reverse the line. We get “taC rof C”. Then we cut the first word, we get 'taC'. And then we reverse it again.

$>echo "C for Cat" | rev | cut -f1 -d' ' | rev
Cat
How to get the n-th field from a Unix command output?
We know we can do it by [cut]. Like below command extracts the first field from the output of [wc –c] command

$>wc -c file.txt | cut -d' ' -f1
109
But I want to introduce one more command to do this here. That is by using [awk] command. [awk] is a very powerful command for text pattern scanning and processing. Here we will see how may we use of [awk] to extract the first field (or first column) from the output of another command. Like above suppose I want to print the first column of the [wc –c] output. Here is how it goes like this:

$>wc -c file.txt | awk ' ''{print $1}'
109 
The basic syntax of [awk] is like this:

awk 'pattern space''{action space}'
The pattern space can be left blank or omitted, like below:
$>wc -c file.txt | awk '{print $1}'
109
In the action space, we have asked [awk] to take the action of printing the first column ($1). More on [awk] later.
How to replace the n-th line in a file with a new line in Unix?
This can be done in two steps. The first step is to remove the n-th line. And the second step is to insert a new line in n-th line position. Here we go.

Step 1: remove the n-th line

$>sed -i'' '10 d' file.txt       # d stands for delete
Step 2: insert a new line at n-th line position

$>sed -i'' '10 i This is the new line' file.txt     # i stands for insert
How to show the non-printable characters in a file?
Open the file in VI editor. Go to VI command mode by pressing [Escape] and then [:]. Then type [set list]. This will show you all the non-printable characters, e.g. Ctrl-M characters (^M) etc., in the file.

How to zip a file in Linux?
Use inbuilt [zip] command in Linux

How to unzip a file in Linux?
Use inbuilt [unzip] command in Linux.

$> unzip –j file.zip
How to test if a zip file is corrupted in Linux?
Use “-t” switch with the inbuilt [unzip] command

$> unzip –t file.zip
How to check if a file is zipped in Unix?
In order to know the file type of a particular file use the [file] command like below:

$> file file.txt
file.txt: ASCII text
If you want to know the technical MIME type of the file, use “-i” switch.
$>file -i file.txt
file.txt: text/plain; charset=us-ascii
If the file is zipped, following will be the result
$> file –i file.zip
file.zip: application/x-zip
How to connect to Oracle database from within shell script?
You will be using the same [sqlplus] command to connect to database that you use normally even outside the shell script. To understand this, let's take an example. In this example, we will connect to database, fire a query and get the output printed from the unix shell. Ok? Here we go –

$>res=`sqlplus -s username/password@database_name <<EOF
SET HEAD OFF;
select count(*) from dual;
EXIT;
EOF`
$> echo $res
1
If you connect to database in this method, the advantage is, you will be able to pass Unix side shell variables value to the database. See below example

$>res=`sqlplus -s username/password@database_name  <<EOF
SET HEAD OFF;
select count(*) from student_table t where t.last_name=$1;
EXIT;
EOF`
$> echo $res
12
How to execute a database stored procedure from Shell script?
$> SqlReturnMsg=`sqlplus -s username/password@database<<EOF
BEGIN
Proc_Your_Procedure(… your-input-parameters …); 
END;
/
EXIT;
EOF`
$> echo $SqlReturnMsg
How to check the command line arguments in a UNIX command in Shell Script?
In a bash shell, you can access the command line arguments using $0, $1, $2, … variables, where $0 prints the command name, $1 prints the first input parameter of the command, $2 the second input parameter of the command and so on.

How to fail a shell script programmatically?
Just put an [exit] command in the shell script with return value other than 0. this is because the exit codes of successful Unix programs is zero. So, suppose if you write

exit -1
inside your program, then your program will thrown an error and exit immediately.
How to list down file/folder lists alphabetically?
Normally [ls –lt] command lists down file/folder list sorted by modified time. If you want to list then alphabetically, then you should simply specify: [ls –l]

How to check if the last command was successful in Unix?
To check the status of last executed command in UNIX, you can check the value of an inbuilt bash variable [$?]. See the below example:

$> echo $?
How to check if a file is present in a particular directory in Unix?
Using command, we can do it in many ways. Based on what we have learnt so far, we can make use of [ls] and [$?] command to do this. See below:

$> ls –l file.txt; echo $?
If the file exists, the [ls] command will be successful. Hence [echo $?] will print 0. If the file does not exist, then [ls] command will fail and hence [echo $?] will print 1.
How to check all the running processes in Unix?
The standard command to see this is [ps]. But [ps] only shows you the snapshot of the processes at that instance. If you need to monitor the processes for a certain period of time and need to refresh the results in each interval, consider using the [top] command.

$> ps –ef
If you wish to see the % of memory usage and CPU usage, then consider the below switches
$> ps aux
If you wish to use this command inside some shell script, or if you want to customize the output of [ps] command, you may use “-o” switch like below. By using “-o” switch, you can specify the columns that you want [ps] to print out.
$>ps -e -o stime,user,pid,args,%mem,%cpu
How to tell if my process is running in Unix?
You can list down all the running processes using [ps] command. Then you can “grep” your user name or process name to see if the process is running. See below:

$>ps -e -o stime,user,pid,args,%mem,%cpu | grep "opera"
14:53 opera 29904 sleep 60                     0.0  0.0
14:54 opera 31536 ps -e -o stime,user,pid,arg  0.0  0.0
14:54 opera 31538 grep opera                0.0  0.0
How to get the CPU and Memory details in Linux server?
In Linux based systems, you can easily access the CPU and memory details from the /proc/cpuinfo and /proc/meminfo, like this:

$>cat /proc/meminfo
$>cat /proc/cpuinfo


#### get free space in current directory ##########

df -Ph . | tail -1 | awk '{print $4}'

----------- quick intro to UNIX text file searching ----------
http://en.wikibooks.org/wiki/A_Quick_Introduction_to_Unix/Searching_Text_Files