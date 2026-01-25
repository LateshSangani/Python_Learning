Python verions
1) Python 1.0 Jan 1994
2) Python 2.0 Oct 2000
3) Python 3.0 Dec 2008

C:\Users\Lenovo>where python
                C:\Programs\Python\python.exe
                C:\Programs\anaconda3\python.exe
                C:\Users\Lenovo\AppData\Local\Microsoft\WindowsApps\python.exe

C:\Users\Lenovo>

The Python is both compile and interpreted language.
PVM : Python Virtual Machine

Source Code -> Compiler -> Byte Code -> Interpreter ( done in PVM ) -> Machine Language in the binary format

The Python is the programming langage but its called as concept also where different flovours we can mixed up.
The below is the few list of the Python Flovours
1) CPYTHON  -> all the internal logic is happening with C language. The below entire cource content is based on the CPYTHON
2) PyPy  -> all the internal logic is happening with Python language only.
3) IRONPYTHON -> all the internal logic is happening with Dot Net language. 
4) JYTHON  -> all the internal logic is happening with Java language. 

---------------------------------------installation and software setup over----------------------

Setup to be downlaod https://www.python.org/downloads/
Run the setup , press next , next..etc.


C:\Programs\anaconda3\python.exe  #3.9.12 versions of the python added
C:\Programs\anaconda3\Scripts # 3.9.12 version libarary



By default Python comes with default IDE called as IDLE where also we can write code and execute it.
The python commands can be executed from the windows command prompt and IDLE also.
In Windows the arrow keys shows the previos commands typed but in the IDEL it does not support by default.
Hence in the IDLE  the default is ALT+P.
To make in the IDLE working same as windows keys
Options -> Configure IDLE -> Keys -> Search "history previos" -> Press Get New Keys for Selection -> PopUp will open and select the "Up Arrow" from it.
Now the Up arrow key will start working.

The windows support cls commond to clear entire typed content but IDLE does not supports and hence closing  the IDLE is the only option left.
The windows support the sliders to go up and down, the IDLE does not have sliders like windows.

PyCharm is  the Famous Editor for the code writing and execution.

IDE Pycharm setup to be downloads
https://www.jetbrains.com/pycharm/download/#section=windows
Download the community version.
Run the setup , press next..

C:\Programs\JetBrains\PyCharm Community Edition 2022.1.2  #PyCharm applicaiton setup
C:\Users\Lenovo\OneDrive\Technology\Python\PyCharm_Project  #Pycharm project


Anaconda is the another famous editor for the data science technologies.

C:\Programs\anaconda3  # Anaconda setup
C:\Programs\anaconda3\python.exe  #Anaconda installed python.
C:\Programs\anaconda3\Lib #Anaconda Python Libarary

Pycharm EXE, ANACONDA , Python 3.9 and Python 3.10,Sublime copied here
D:\Software\

Spyder : Scientific Python Development Platform.

IDE available
1) IDLE
2) Command Prompt
3) Pycharm
4) Sublime
5) Jupyter (notebook)
6) Databricks(notebook)
7) VS Code

---------------------------------------installation and software setup over----------------------

-------------------------------------------Python prompt code Start ------------------------------------------------------
basic commands
1+1 o/p 2    integer
2*3  o/p 6    integer
3-3 o/p 0    integer   
4/2 o/p 2.0  float
5//2 o/p 2   integer   #here // indicate return the integer number  , the quotent part comes up
5/2 o/p 2.5  float
1+1-1 o/p 0   it will work
1+1-     Syntax Error
1+(1*1) o/p 2 It will work

2 rest to power 3  # Here ** indicate its power symbol  
2 ** 3  = 8   or  2**3 = 8

10//3 o/p  3  Quotent number
10%3  o/p  1  Reminder number

'Latesh'   o/p 'Latesh'
"Latesh"   o/p 'Latesh'
print('Latesh')  o/p Latesh
print("Latesh's") o/p Latesh's
print('Latesh"s') o/p Latesh"s
print('Latesh\'s "Sangani"') o/p Latesh's "Sangani"
'latesh'+'sangani'  o/p : lateshsangani
print('latesh' + 'sangani') o/p lateshsangani
print('latesh' || 'sangani') o/p error
'latesh'*10 o/p 'lateshlateshlateshlateshlateshlateshlateshlateshlateshlatesh'
print('c:\latesh\navin') 
o/p : 2 lines
c:\latesh
avin

#here avin come becuase python understood /n and used n from the navin string.
print(r'c:\latesh\navin') # r-> raw means instruct to python not to use any conversion.
o/p 'c:\latesh\navin'

x=3   no output # its just assignment
3+x   o/p 6 
y=2   no output # its just assignment
x+y  o/p 5
x=9  #now value 3 is overwritten by value 9
x    o/p 9 #just typed x it will give its value , no need of the print.

_ + y  # here _ means the output of the previos operation , so here value of x previos operation 9 + y value was 2, so o/p is 11.
name=latesh       #here error comes up , single quote is missing.
name = 'Latesh'   #here we are setting the string variable. here while setting string the single quote is requried.
name              #here output value of the name will come.  o/p 'Latesh'  Note : here string value comes with Single quote.
name + ' rocks'  o/p 'Latesh rocks'  # note value comes with single quote.

0   1    2    3   4   5 
L   a    t    e   s   h
-6 -5   -4   -3   -2  -1



name[0]   o/p 'L'  here the first index values comes up. The index start from 0..n
name[4]   o/p 's'  
name[10]  Error  IndexError: string index out of range
name[-5] o/p 'a'
name[-1] o/p 'h'
name[1:2] o/p 'a'
name[0:1]  o/p 'L'
name[0:5]  o/p 'Lates'
name[0:]  o/p 'Latesh'  #here without end index
name[:5]  o/p 'Lates'   #here without start index
name[0] = 'R' o/p #here Assignment of the 'R' to first index does not work. it will give error. as Name is string ,its not the list.
name[0:2] = 'Ri'  o/p #here Assignment of the 'Ri' to first and second index does not work. it will give error. as Name is string ,its not the list.
'Ri' + name[2:]  o/p 'Ritesh'

# Things to remember : The [n:m] provides the output from n postion to m-1 position.

len(name) o/p 6  Note : lenght is not the python keyword
len('latesh sangani') o/p: 14

0   1    2    3   4   5 
10  20   30   40  50  60
-6 -5   -4   -3   -2  -1

[]  -> its for LIST
()  -> its for TUPLE 
{}  -> its for SET
{key1:value1,key2:value2} -> its for dictionary here keys must be unique

# [,,,] -> List Operator
mylist = [10,20,30,40,50,60]  #Assignment of the numbers list
mylist[0]  o/p 10
mylist[10]  IndexError: list index out of range
mylist[0:4]  o/p [10, 20, 30, 40]  # Things to remember : The [n:m] provides the output from n postion to m-1 position.
mylist[-1] o/p 60
mylist[3:] o/p [40, 50, 60]  # index 3 + index 3 onwards

names  = ['Latesh' , 'Ruchi' , 'Vaneesa']  #Assignment of the chars list
names[1] o/p 'Ruchi'

val = [10 , 'Latesh' , 45.56] # Mixed list

new_list = [names , mylist]     #Assignment of the two list in the single list and mix of datatypes list.
o/p : [['Latesh', 'Ruchi', 'Vaneesa'], [10, 20, 30, 40, 50, 60]]

mylist.append(10) #Assignment of the extra new index VALUE items at last, append(VALUE or LIST)
mylist
o/p : [10, 20, 30, 40 , 50 , 60 , 10]

# Here again printing the new_list will give the extra appended value of the mylist list.

mylist.insert(2,30) #Assignment of the new value 30 , after 2nd index position. insert(INDEX,VALUE)
o/p : [10, 20, 30, 30, 40, 50, 60, 10]

mylist.remove(10)  #removed the value 10 from the list 
                   #note : if multiple 10 values present in the list only the 1st occurance will be deleted.
                   # remove(VALUE)
o/p : [20, 30, 30, 40, 50, 60, 10]

mylist.pop(6) # remove the 6th position value.  o/p: 10  pop(INDEX)

mylist.pop() #remove the last index postion value.

# using single line for loop to return list

squares = [i**2 for i in range(10)]
print(squares)

#using for loop for multiple line list population
a=[]
for i in range(10):
    a.insert(i,i ** 2)
print(a)

#DIFF BETWEEN POP AND REMOVE -> POP accept the input INDEX and REMOVE accept the input VALUE.

mylist o/p : [20, 30, 30, 40, 50, 60]

mylist[0] = 21     o/p : [21, 30, 30, 40, 50, 60]   #over write the values

del mylist[2:]  # delete the list from position 2 onwards  , so 0.1 are safe and 2 onwards all the index deleted. del is the keyword.
o/p : [21, 30]

mylist.extend([11,22,33]) # Extend the values in the existing list , NOTE : EXTEND only need the input LIST
o/p : [21, 30, 11, 22, 33]

mylist.append([44,55])  # If Append is used with LIST , List will be appended to the existing list.
o/p: [21, 30, 11, 22, 33, [44, 55]]

max(mylist)  o/p : 33
min(mylist)  o/p : 11
sum(mylist) o/p : 116
len(mylist) o/p : 5
mylist.sort()  
#No Output immediate but after that agian has to give mylist. even print(mylist.sort()) will not give immediate output.
print(mylist.sort())  o/p: None
mylist
[11, 20, 22, 30, 33]

#List operations : insert,append,delete,pop,extend,max,min,sum,sort and del
# count(mylist)  this opetation is not working  , but its replacement is len(mylist)

List(Collection) Vs Tuple :

List is mutable , means we can change the values read+write. Tuple is not mutable , means values are read only.
Iteration or Processing of the Tuple is faster than List as values does not changed.
Square Bracket [] is for list and Round Bracket () is for Tuple.
       0  1  2  3  4  5
tup = (11,22,33,44,55,66)  #Assignment of the tuple.
tup[1]   o/p: 22
tup[5] = 100  #Error as Tuple does not support it.
tup[0] = 12   #Error as Tuple does not support it.
tup(0) = 12   #Error as Tuple does not support it.

Set

a = {11,22,33,44,55,66}   #SET assignement to varaible s
a  # Random order values without compromising the values count and actual values.
a[1] # o/p error as SET does not have fix sequence of the values.

# Whether its LIST or TUPLE or SET in all the cases the [] is used for all the operations. 

help()  :  it will open the help terminal where we get python command specific help

id(varible_name) used to get the address of the variable. variable datatype can be number , char or float

a = 10
id(a)   o/p : 34556783787686

b = a 
id(b)  o/p : 34556783787686

id(10)  o/p : 34556783787686

#The addess is for the value , not for the variables. Each variable is consider as tag and tags stick to values.
#Hence python occupied the less memory. The number of variables can increase but value+address remain static

a = 9
id(a)   o/p : 34534576325809
id(b)   o/p : 34556783787686 

#here a new value is 9 , hence the new address generated but b address is untouched because b is just tagged to 10
#and a is now tagged to 9.

#Python does not have CONSTANT feature but with capital letters we can make interpretion its constant.
PI = 3.14

type(variable_name)  # o/p : it will tell the value is of datatype FLOAT, INT , STRING , SET , LIST ,TUPLE ,DIST

Datatypes:
1) None  #None is the similar of NULL in other languages. PySpark has NaN
2) Numeric #Float
3) List      []#subtype = sequence
4) Tuple     ()#subtype = sequence
5) Set       {}#subtype = sequence
6) String    #subtype = sequence
7) Range     #subtype = sequence
8) Dictionary {}

a = 10 
type(a) 
class -> int

a = 10.34 
type(a) 
class -> float

a = 5+7j        # j is reserved. i cannot use, it will give error.
type(a) 
class -> complex

a = 10.545
b = int(a)
type(b)
class -> int
b o/p: 10

a = 10
b = float(a)
type(b)
class -> float
b o/p: 10.0

x = 9
y = 5
z = complex(x,y)
type(z)
z    o/p :  (9+5j)
class -> complex

a = 56
b = 67
c = a<b
c  o/p: True
type(c)
class -> bool  # note bool is the only keyword

int(True)
o/p : 1

int(False)
o/p : 0

mlist = [10,20,40]
type(mlist) 
class -> list

mset = {10,20,30}
type(mset)
class -> set

mtup = (10,20,30,50)
type(mtup)
class -> tuple

#in python char and string both are same and class will be str only.

range(14) #count of values will be 14 but index from 0..13
o/p : range(0,14)

list(range(14)) #count of values will be 14 but index from 0..13 , now because of list the index become VALUES.
o/p : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

list(range(1,25,3))
o/p : [1, 4, 7, 10, 13, 16, 19, 22]

list(range(1,26,3))
o/p : [1, 4, 7, 10, 13, 16, 19, 22, 25]

#first parameter is the start of the range 
#second parameter is the end of the range 
#third paramater is to give difference in the range of values

type(range(3))
class -> range

# DICTIONARY operations : dict_keys , dict_values , get
# make sure the key is unique in the dictionary 
mydist = {1:'latesh',2:'ruchi',3:'vaneesa'}
type(mydist)
class -> dist

mydist.keys()
o/p : dict_keys([1, 2, 3])

mydist.values()
o/p : dict_values(['latesh', 'ruchi', 'vaneesa'])

mydist[2]  # alernate mydist.get(2)
o/p : 'ruchi'

mydist.get(2)
o/p : 'ruchi'


x = 9
y = 2
x-y o/p: 7
x+y o/p: 11
x/y o/p: 4.5
x*y o/p: 18

x=x+2  o/p : 11
x += 2 o/p : 13
x *= 2 o/p : 26

a,b = 2,3
a o/p : 2
b o/p : 3

n = 5
n = -n
n o/p : -5

#compare two variable with == sign.  single = is used to assigment.

a = 1
b = 2
a < b    o/p : True
a > b    o/p : False
a == b   o/p : False
a = 2
a == b   o/p : True

a = 2
b = 1
a <= b o/p : False
a >= b o/p : True

a = 2
b = 2
a != b o/p : False
a = 3
a != b o/p : True

a = 5 
b = 10

a < 6 and b > 11   o/p : False
a < 6 and b > 9    o/p : True

x = True
not x   o/p : False
x   o/p : True

x = not x 
x  o/p : False

#not operator is used for the boolean transformation

Convert decimal into binary:
bin(2)  o/p : '0b10'  #convert regular number to binary format.
bin(20)  o/p : '0b10100'  
0b10100   o/p : 20  
#here starting with 0b understood by python its binary number and hence it converted into the actual decimal number.
#Note : 0b at start is the indicater its binary number , the actual binary number starts after 0b only.

Convert decimal into Octal:
oct(2)  o/p : '0o2'    #convert value 2 in the octal number
oct(20)  o/p : '0o24'  
0o24   o/p : 20  
#here starting with 0o understood by python its octal number and hence it converted into the actual decimal number.
#Note : 0o at start is the indicater its octal number , the actual octal number starts after 0o only.

Convert decimal into Hexadecimal:
hex(2)  o/p : '0x2'   #convert value 2 in the hexadecimal number
hex(20) o/p : '0x14' 
0x14 o/p : 20    
#here starting with 0x understood by python its hexadeciaml number and hence it converted into the actual decimal number.
#Note : 0x at start is the indicater its hexadecimal number , the actual hexadecimal number starts after 0x only.

#Zero [b|o|x]

6 bit wise operators:
1) Complement(~)
2) And(&)
3) OR(|)
4) XOR(^) 
5) Left Shift(<<)
6) Right Shift(>>)

~12  o/p : -13
#complement convert the decimal value into binary then with binary value replaced 0 with 1 
#and 1 with 0 and last do +1 

12 & 13  o/p : 12
25 & 45  o/p : 9
# & convert decimal number to binary and apply the AND conditions of the 0,1
12 | 13  o/p : 13
25 | 45  o/p : 61
# | convert decimal number to binary and apply the OR conditions of the 0,1

12 ^ 13  o/p : 1
25 ^ 45  o/p : 52
# ^ convert decimal number to binary and apply 0,1 and 1,0 combination provide the value 0 
# also  1,1 and 0,0 provide the value 1.

12 << 13  o/p  :98304    
12 >> 13  o/p  :0

math libarary provides the different mathametics function which was useful for complex problem solving condition.
it was not loaded by default in python and it has to import in the code first.
we can use the math function with in the print and use to assign the value in to the variable also.

import math
math.sqrt(25)  o/p : 5
math.sqrt(5)   o/p : 2.23606797749979
a = math.sqrt(5)
a  o/p : 2.23606797749979

sequence of function:
ceil   -> give integer number greater value
roundoff  -> play with in the .5 range of the values
floor  -> give integer number lower value
pow -> power function
trunc -> remove the decimal values after .
factorial -> Find the factorial of the input number

for 2.5 value the roundoff is 2.5
for 2.4 value the roundoff is 2
for 2.6 value the roundoff is 3

for 2.5 value the ceil is 3
for 2.5 value the floor is 2

math.ceil(2.5) o/p : 3
math.floor(2.5) o/p : 2
print(math.floor(2.5))  o/p : 2

Power function:
math.pow(3,3) o/p: 27.0    # note: pow function added .0 at last
3 ** 3 o/p : 27

Trunc function:
math.trunc(10.44545)  o/p : 10
math.trunc(10.9999999)  o/p : 10

Factorial function:
math.factorial(5)  o/p : 120
math.factorial(9)  o/p : 362880

Exponentional function:
math.exp(2)  o/p : e rest to the power 2    7.38905609893065
math.exp(10) o/p : 22026.465794806718

#many other functions like log , log10, lcm , gcd , trignomery sin, cos function are part of the math libarary.

math.pi   o/p : 3.141592653589793    # pi is the constant value 
math.e    o/p : 2.718281828459045    # note : e is epsillion constrant 

import math as m   #note here m is the alias of math and 'as' keyword is mandatory.
m.pow(2,2) o/p : 4.0

#in case user wants to import the limited function from the math libary , use the below syntax.
#now no need to even write the math or alias in the code direct pow and sqrt function work.

from math import pow , sqrt 
pow(3,4) o/p : 81.0

help(math)  o/p  #details of all the available function 

-----------------------Python prompt code end ------------------------------------------------------
-----------------------Python Programming Start----------------------------------------- 

input() : #input function takes the user provied input with in the python program 
          #and by default in the form of the string. So even user has entered decimals its string for python.
          #hence for decimals the conversion of the data types is involved.
          #Run time user choice input dynamic parameter
          

a = int(input('Enter the value for a -> '))  #i/p:10
b = int(input('Enter the value for b -> '))  #i/p:20
c = a + b
print(c)    #o/p : 30


#note if user has not provided single char and inputted multiple chars or words or para.
#The index 0 will always give the first char.
ch = input('Enter the char')       #i/p:  aderecrtyyeyeyjee    
print(ch[0])    #o/p :   a            

Alternate way

ch = input('Enter the char')[0]  #i/p:  aderecrtyyeyeyjee    
print(ch)  #o/p :   a

#eval function is to evaluate the user provided computed expression
result = eval(input('Enter the maths expression'))  #i/p: 4+5-5+3/4*4
print(result)   #o/p : 7

sys.argv[]  : #the argv is  the sys libariry imported function which is used to take input from the outside of the python prompt.
              #and by default in the form of the string.So even user has entered decimals. its string for python.
              #hence for decimals the conversion of the data types is involved.
              # static parameter to accept input from the autosys or cronjob

#ex: 
#Write the below code in the python file and run the file from the command prompt.
#mytest.py 
import sys as s
a = int(s.argv[1])
b = int(s.argv[2])
print(a+b)

command : 
C:\Programs\anaconda3>python Command_Prompt.py 2 3
o/p : 5

IF Statments :

if False:
    print('Inside')
print('Outside')

o/p : Outside
#See if only work for the True condition and the second print is out of the scope of the if 
#because it does not holds any space before start.  
#The Default tab (4 space) avaiable for all the statement belongs to single if.

if False:
  print('Inside')
print('Outside')
#it will also work , even the first print has 2 or 1 space only.
o/p : Outside

if False:
    print('Inside')
  print('Outside')
#it will NOT work , as both print has different count of the space.
# error :  IndentationError: unindent does not match any outer indentation level
o/p : Error

IF.. ELSE Statments : 

a = 3
if a == 3:
    print('Yes')
else:
    print('No')

o/p: Yes

IF..NESTED IF.. ELSE Statments : 

a = 3
b = 2
if a == 3:
    print('If')
    if b == 2:
        print('nested if')
else:
    print('Else')

o/p:

If
nested if

IF..NESTED IF.ELSE. ELSE Statments : 

a = 3
b = 2
if a == 3:
    print('Yes')
    if b == 2:
        print('nested if')
    else:
        print('else of nested if')
else:
    print('No')

o/p:
Yes
nested if    
    
IF .. ELIF ..ELSE : 

a = 3
if a == 1:
    print('One')
elif a == 2:
    print('Two')
elif a == 3:
    print('Three')
else:
    print('Wrong Number')

o/p: Three

While loop :

a = 1
while a <= 6:
    print('Latesh')
    a = a+1

o/p:
Latesh
Latesh
Latesh
Latesh
Latesh
Latesh

Nested While loop :

#end=""   used  to print output in the single line till the new line i.e print() is not mentioed.
# by default print will print to next line.

a = 1
b = 1
while a <= 3:
    print("Latesh",end="")
    b = 1
    while b <= 2:
        print("Vaneesa",end="")
        b = b+1
    a = a+1
    print()    
 
o/p:
LateshVaneesaVaneesa
LateshVaneesaVaneesa
LateshVaneesaVaneesa
 
For loop :

a = [10,20,30,40,50]
for i in a:
    print(i)
    
o/p:
  
10
20
30
40
50
    
a = [10,'Latesh',3.5,'Sangani','3i']
for i in a:
    print(i) 
    
#alternate way

for i in [10,'Latesh',3.5,'Sangani','3i']:
    print(i)    
    
o/p:
10
'Latesh'
3.5
'Sangani'
'3i' 
 
a = 'LATESH'
for i in a:
    print(i)

alternate way 

for i in 'LATESH':
    print(i)
    
o/p:
L
A
T
E
S
H    

range(start, stop, step)
start : The beginning of the sequence default 0
stop : The end of the sequence , mandatory 
step : The difference between each number

#range starts from 0..n    
for i in range(11):  
        print(i)
        
o/p:
1
2
3
..
..
10        

for i in range(11,21,2):  
        print(i)

o/p:
11
13
15
17
19        

for i in range(5,0,-1):
        print(i)
        
o/p:

5
4
3
2
1

for i in range(5):
        print(-i)
        
o/p:
0
-1
-2
-3
-4
        
#for with if..else  

for i in range(20):
    if i%5 == 0:
        print(i,'Divide by 5 possible')
    else:
        print(i,'Divide by 5 not possible')
      
o/p:

0 Divide by 5 possible
1 Divide by 5 not possible
2 Divide by 5 not possible
3 Divide by 5 not possible
4 Divide by 5 not possible
5 Divide by 5 possible
6 Divide by 5 not possible
7 Divide by 5 not possible
8 Divide by 5 not possible
9 Divide by 5 not possible
10 Divide by 5 possible
11 Divide by 5 not possible
12 Divide by 5 not possible
13 Divide by 5 not possible
14 Divide by 5 not possible
15 Divide by 5 possible
16 Divide by 5 not possible
17 Divide by 5 not possible
18 Divide by 5 not possible
19 Divide by 5 not possible

#Break keyword
brk = 4
x = int(input('How many times loop need to run : '))   #i/p : 5
i = 1
print('start of program')
while i <= x:
    if i == brk:
        break
    print(i)
    i = i+1
print('end of program')      

o/p:

start of program
1
2
3
end of program


cont = 4
x = int(input('How many times loop need to run : '))   #i/p: 6
print('start of program')
print(list(range(x)))
for i in range(2,x):
    if i == cont:
        continue
    print(i)
print('end of program')

#note : the range will start default with 0...n-1
#but here in for loop it has been asked to start from index 2

o/p: 
start of program
[0, 1, 2, 3, 4, 5]
2
3
5
end of program



x = int(input('How many times loop need to run : '))   # i/p: 6
print('start of program')
print(list(range(x)))
for i in range(x):
    if i%2 == 0:
        pass
    else:
        print(i)
print('end of program')

o/p:
start of program
[0, 1, 2, 3, 4, 5]
1
3
5
end of program

#pass is same has null in the oracle , if nothing is required to compute 
#or nothing is required to print then pass will be helpful.
#break , continue , pass keyword in the While loop

print('program start')
for i in range(4):
    for j in range(4):
        print('*',end="") # end is giving intruction to print till the space is not coming. By default print("..." , end='\n') is present
    print("") 
print('program end')

o/p:
program start
****
****
****
****
program end


print('program start')
for i in range(1,5):
    print(i*'*')
print('program end')

o/p:

program start
*
**
***
****
program end

Alternate way:

print('program start')
for i in range(4):
    for j in range(i+1):
        print('*' , end="")
    print()
print('program end')

o/p:

program start
*
**
***
****
program end



print('program start')
for i in range(4,0,-1):
    print(i*'*')
print('program end')

o/p: 
program start
****
***
**
*
program end

#for..else statment

print('program start')
for i in [4,6,8,12]:
    if i%5 == 0:
        print('Number division by 0')
    else:
        print('Number not division by 5')
print('program end')

o/p:   see 4 times string printed which is not good programming
program start
Number not division by 5
Number not division by 5
Number not division by 5
Number not division by 5
program end

#With change in the intendition of the for else statement , now only single time output comes.
#now the else is the part of the for loop.

print('program start')
for i in [4,6,8,12]:
    if i%5 == 0:
        print('Number division by 0')
else:
    print('Number not division by 5')
print('program end')

o/p:
program start
Number not division by 5
program end

#to check the number is prime or not.
print('program start')
prime_num = 7
for i in range(1,prime_num):
    if i%prime_num == 0:
        print('Number is not prime')
else:
    print('Number is prime')
print('program end')

o/p:
program start
Number is prime
program end

Array:
#The array and list near about behave same way 
#but in the list we can have mix of the data types but in the array all the values has same data types.
#to use array different symbol present for each data types.
#both array and list start from the 0th Position.
#list comes by default in python , but array comes as seperate libarary in python.

array(typecode of the datatype , values to be part of the array)
ex: array('i',[10,20,30,40,50])
the type code is as below 

'b' -> int -> size in bytes 1
'B' -> int -> size in bytes 1
'u' -> Unicode character -> size in bytes 2
'h' -> int -> size in bytes 2
'H' -> int -> size in bytes 2
'i' -> int -> size in bytes 2
'I' -> int -> size in bytes 2
'I' -> int -> size in bytes 4
'L' -> int -> size in bytes 4
'f' -> float -> size in bytes 4
'd' -> float -> size in bytes 8


from array import *   
#thing line import all the functions constants of array 
#and good thing is we dont need need alias or use libarary. function name syntax. 
arr = array('i',[10,20,30,40,50])
print(arr)        #o/p:  array('i', [10, 20, 30, 40, 50])
print(arr.buffer_info())   #o/p: (2156790208656, 5)  it return the memory location and size of the array i.e. 5
print(arr.typecode)    #o/p : i
arr.reverse()
print(arr)  #o/p : array('i', [50, 40, 30, 20, 10])

for i in range(5):   #when  array length is known
    print(arr[i])  
    
#alternate way

for i in range(len(arr)):   #when array length is unknown
    print(arr[i]) 
    
#alternate way

for i in arr:   #dont worry about length, all the value of array comes , 
    print(i)    #as their is no fix length of the array in python.
        
#alternate way

for i in array('i',[10,20,30,40,50]):  # no need of the variable and range operation for index
    print(i)
    
o/p : #print array in reverse order but each value in the new row. NOTE above the reverse() function applied
50
40
30
20
10
   
o/p: 10..50 but in each row the value will comes.   

from array import *
for i in array('u',['a','b','c','d','e']):
    print(i) 
o/p: 
a
b
c
d
e

#How to derived array from the existing array

from array import *
arr = array('u',['a','b','c','d','e'])
new_arr = array(arr.typecode , (b for b in arr))    
#note : b for b or we can  write a for a or z or z ... 
#it can be anything only thing is matter both should be the same symbol.
for i in new_arr:
    print(i)

alternate way

from array import *
arr = array('u',['a','b','c','d','e'])
new_arr = array(arr.typecode , arr)
for i in new_arr:
    print(i)
    
alternate way

from array import *
arr = array('u',['a','b','c','d','e'])
new_arr = array(arr.typecode, arr)
i = 0
while i < len(new_arr):
    print(new_arr[i])
    i = i+1    
    
o/p: a..e but in each row the value will comes. 

     
#Filled the array values from the command prompt

from array import *
arr = array('i',[]) # initlized empty array
arr_len = int(input('Enter the length of the array: '))
for i in range(arr_len):
    arr_val = int(input('Enter the next value of array: '))
    arr.append(arr_val)
arr.append(0) # append(VALUE) , Value will always append at last
print(arr)  

o/p : 
Enter the length of the array: 3
Enter the next value of array: 1
Enter the next value of array: 2
Enter the next value of array: 3
array('i', [1, 2, 3, 0])    #0 is the extra value added not from the inputted value.

#Over ride the value of the array

from array import *
arr = array('i',[])
arr_len = int(input('Enter the length of the array: '))
for i in range(arr_len):
    arr_val = int(input('Enter the next value of array: '))
    arr.append(arr_val)
arr.insert(4,0) # insert(INDEX,VALUE)
print(arr)

o/p:

Enter the length of the array: 5
Enter the next value of array: 1
Enter the next value of array: 2
Enter the next value of array: 3
Enter the next value of array: 4
Enter the next value of array: 5
array('i', [1, 2, 3, 4, 0, 5])   #see the 4th index position value is override by value 0 in array.

#Searching the value in the array  . manual way with IF check
#Good to put break as 1st occurance is know to us. 
#In case we need to look for all the occurance then remove the break keyword.
#the usage of the break keyword is not visible in the output 
#but performance wise it will not check the iteration and go out of loop , not the program.

from array import *
arr = array('i',[])
arr_len = int(input('Enter the length of the array: '))
for i in range(arr_len):
    arr_val = int(input('Enter the next value of array: '))
    arr.append(arr_val)
ser_val = int(input('Enter the value to be search in the array: '))
x = 0
for i in arr:
    if i == ser_val:
        print('position',x)
        break        
    x = x+1

o/p:

Enter the length of the array: 3
Enter the next value of array: 100
Enter the next value of array: 200
Enter the next value of array: 300
Enter the value to be search in the array: 200
position 1
Process finished with exit code 0   

#same code with exit keyword logic:

from array import *
arr = array('i',[])
arr_len = int(input('Enter the length of the array: '))
for i in range(arr_len):
    arr_val = int(input('Enter the next value of array: '))
    arr.append(arr_val)
ser_val = int(input('Enter the value to be search in the array: '))
x = 0
for i in arr:
    if i == ser_val:
        print('position',x)
        exit(100)
    x = x+1
print('bye')

o/p:

Enter the length of the array: 2
Enter the next value of array: 1
Enter the next value of array: 2
Enter the value to be search in the array: 1
position 0

Process finished with exit code 100   
# this is line python shows that code is done exist and whatever value return is exit is return out. 
# default value 0

index function of the python array:


from array import *
arr = array('i',[])
arr_len = int(input('Enter the length of the array: '))
for i in range(arr_len):
    arr_val = int(input('Enter the next value of array: '))
    arr.append(arr_val)
ser_val = int(input('Enter the value to be search in the array: '))
print(arr.index(ser_val))
print(arr[arr.index(ser_val)])

o/p:
Enter the length of the array: 3
Enter the next value of array: 12
Enter the next value of array: 14
Enter the next value of array: 16
Enter the value to be search in the array: 14
1
14

Multidimension array:
#The defalut array() function in the array libarary does not support the multiple dimension 
#i.e 2D rows and columns and 3d cubes 
#hence numpy libarary i.e. third part libarary is required here.

The import for the numpy will not work as its not present by default. It need to install.
to install numpy the PIP command is used. (Package Installer) 

TO Update the PIP command itself run the command below from same python.exe command prompt path.

Requirement already satisfied: pip in c:\programs\python\lib\site-packages (22.0.4)
Collecting pip
  Downloading pip-23.3.2-py3-none-any.whl (2.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 5.6 MB/s eta 0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 22.0.4
    Uninstalling pip-22.0.4:
      Successfully uninstalled pip-22.0.4
Successfully installed pip-23.3.2


#Open the command prompt and go to the python path or go to any path as python is part of the PATH variable and install numpy.

C:\Programs\anaconda3>pip3 install numpy
Collecting numpy
  Downloading numpy-1.21.4-cp310-cp310-win_amd64.whl (14.0 MB)
     |████████████████████████████████| 14.0 MB 2.2 MB/s
Installing collected packages: numpy
Successfully installed numpy-1.21.4

#Now the numpy command is avaialble to use in the IDLE and Python prompt. but it will not available in the Pycharm.

#Install numpy in the Pycharm:
#Files -> settings -> Project:PyCharm_Project -> Python Interpreter -> Click + -> search numpy -> click intall and close the popup.
#OR
#Change the Python Interpreter and search the path where python was setup with Anaconda or Miniconda or Pycharm itself

#sample numpy program.

from numpy import *
arr = array([10,20,30,40,50])
print(arr)

o/p: [10 20 30 40 50]   

# array need the list as input parameter
#here no need to provide the type of the array like did in the normal array. 
#because still at last can write the type of array.
ex: arr = array([10,20,30,40,50],int)

#6 ways to make the array with numpy.

array()      # normal array with optional dtype i.e. data type.
linspace()   # lin space # divide the range of values into N part
logspace()   # apply the log function for the divide the range of values into N part
arange()     # a range # provide the range of values with gap of N
zeros()      # provide the N number of the 0
ones()       # provide the N number of the 1


from numpy import *
arr = array([10,20,30,40,50],int)
print(arr)
o/p: [10 20 30 40 50]

from numpy import *
arr = array([10,20,30,40,50],float)
print(arr.dtype)  # dtype i.e. datatype
print(arr)
o/p:  #here explict conversion by end user by telling python to convert into float.
float64
[10. 20. 30. 40. 50.]

from numpy import *
arr = array([10,20,30.33,40,50])
print(arr.dtype) # dtype i.e. datatype
print(arr)
o/p:   #here implict conversion done by python for entire array even because single value 30.33 of the float64
float64
[10.   20.   30.33 40.   50.  ]


from numpy import *
arr = linspace(0,99,10)
print(arr)

o/p:  #divide the range of 100 values, range 0 to 99 into 10 parts
 [0. 11. 22. 33. 44. 55. 66. 77. 88. 99.]
 
from numpy import *
arr = linspace(0,99)
print(arr) 

o/p:  #divide the range of 100 values, range 0 to 99 into default 50 parts

[ 0.          2.02040816  4.04081633  6.06122449  8.08163265 10.10204082
 12.12244898 14.14285714 16.16326531 18.18367347 20.20408163 22.2244898
 24.24489796 26.26530612 28.28571429 30.30612245 32.32653061 34.34693878
 36.36734694 38.3877551  40.40816327 42.42857143 44.44897959 46.46938776
 48.48979592 50.51020408 52.53061224 54.55102041 56.57142857 58.59183673
 60.6122449  62.63265306 64.65306122 66.67346939 68.69387755 70.71428571
 72.73469388 74.75510204 76.7755102  78.79591837 80.81632653 82.83673469
 84.85714286 86.87755102 88.89795918 90.91836735 92.93877551 94.95918367
 96.97959184 99.        ]
 
from numpy import *
arr = arange(0,99,2)
print(arr)

o/p: #create the range of the values between 0 to 99 and diffrence of the next number with previous number is 2.
[ 0  2  4  6  8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46
 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94
 96 98]
 
from numpy import *
arr = logspace(0,99,5)
print(arr)

o/p: #from the range of the values  , +00 , +24 , +49 , +74 ..are the 10 rest to power for the log of values.
#And divide into 5 parts.
[1.00000000e+00 5.62341325e+24 3.16227766e+49 1.77827941e+74
 1.00000000e+99] 
 
from numpy import *
arr = logspace(0,99,5)
print(arr)
print('%.2f' %arr[1])
o/p:  
#here from the above sql 1st position value 5.62341325e+24 is replaced by 5623413251903490271215616.00 
#i.e. the actual real value.
[1.00000000e+00 5.62341325e+24 3.16227766e+49 1.77827941e+74
 1.00000000e+99]
5623413251903490271215616.00


from numpy import *
arr = zeros(10)
print(arr)
arr = ones(10)
print(arr)
o/p: 
#default values comes in the float. the zeros and ones will give the array of the 0 and 1. 
#Input is number of the times 0 or 1 is required.

[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

Conversion into integer:

from numpy import *
arr = zeros(10,int)
print(arr)
arr = ones(10,int)
print(arr)

o/p:
[0 0 0 0 0 0 0 0 0 0]
[1 1 1 1 1 1 1 1 1 1]

#addition of the array
from numpy import *
a1 = array([1,2,3,4,5])
a2 = array([5,4,3,2,1])
print(a1+a2)
o/p: [6 6 6 6 6]

#concatenate of the 2 arrays
from numpy import *
a1 = array([1,2,3,4,5])
a2 = array([5,4,3,2,1])
print(concatenate([a1,a2]))
o/p: [1 2 3 4 5 5 4 3 2 1]


#numpy functions
from numpy import *
a1 = array([1,2,3,4,5])
print(sin(a1)) #[ 0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427]
print(cos(a1)) #[ 0.54030231 -0.41614684 -0.9899925  -0.65364362  0.28366219] 
print(tan(a1)) #[ 1.55740772 -2.18503986 -0.14254654  1.15782128 -3.38051501]
print(log(a1)) #[0.         0.69314718 1.09861229 1.38629436 1.60943791]
print(sum(a1)) #15
print(count_nonzero(a1)) #5   #count()  this function is not present in the numpy
print(sqrt(a1)) #[1.         1.41421356 1.73205081 2.         2.23606798]
print(min(a1)) #1
print(max(a1)) #5
print(sort(a1)) # [1 2 3 4 5]
print(unique(a1)) # [1 2 3 4 5]

#Array copy or assignment of one array to variable to make new array
from numpy import *
a1 = array([1,2,3,4,5])
a2 = a1
print(a1,id(a1))
print(a2,id(a2))

o/p: #array 1 copied into array 2 but both still hold the same memory address.
[1 2 3 4 5] 2608587820848
[1 2 3 4 5] 2608587820848

from numpy import *
a1 = array([1,2,3,4,5])
a2 = a1.view() #here view() function helped to make the new copy of the array with different memory location.
print(a1,id(a1))
print(a2,id(a2))

o/p:  
[1 2 3 4 5] 2320988327728
[1 2 3 4 5] 2320988327824

Three typs of the copy in python numpy array
1) Normal copy : both are alias to same memory location , same values , only technically 2 names.
2) Shallow Copy  : both array dependent to each other , value updated in array a2 will same replicated in the orignal a1. 
                   but memory location is diffrent because of view() function.
3) Deep copy : here the arrays are not dependent to each other value updated in array a2 will NOT replicated in the orignal a1. 
               but memory location is diffrent because of copy() function.


Normal Copy : #Both array updated but address are same
from numpy import *
a1 = array([1,2,3,4,5])
a2 = a1
a2[0]=100
print(a1,id(a1))
print(a2,id(a2))

o/p: 
[100 2 3 4 5] 2608587820848
[100 2 3 4 5] 2608587820848

Shallow Copy :  #Both array updated but address are differnt
from numpy import *
a1 = array([1,2,3,4,5])
a2 = a1.view()  # view : copy only values but address are different
a2[0] = 100
print(a1,id(a1))
print(a2,id(a2))

o/p:
[100 2 3 4 5] 2123973513680
[100 2 3 4 5] 2123978067760

Deep Copy:  #Both array and address are differnt
from numpy import *
a1 = array([1,2,3,4,5])
a2 = a1.copy() # copy : copy only values but address are different 
a2[0] = 100
print(a1,id(a1))
print(a2,id(a2))

o/p:
[1 2 3 4 5] 1489876668880
[100 2 3 4 5] 1489881222960


Two 2D dimension array:

from numpy import *
a1 = array( [
            [0,1,2,3,4],
            [5,6,7,8,9]
            ] )
print(a1)

o/p: 
[[0 1 2 3 4]
 [5 6 7 8 9]]
 
 
from numpy import *
a1 = array( [
            [0,1,2,3,4],
            [5,6,7,8,9],
            [1,0,1,0,1]
            ] )
print(a1.dtype)
print(a1.ndim)
print(a1.shape)
print(a1.size)
a2 = a1.flatten()
print(a2)
print(a1.reshape(5,3))  #reshape(rows,columns)
print(a1.reshape(3,1,5)) #reshape(rows,column,element per column)

o/p:
int32  #dtype gives the datatype of the array element
2      #tells the dimention of the array, 
(3, 5) #tells the row and column count.
15     #tell the number of items in the array.
[0 1 2 3 4 5 6 7 8 9 1 0 1 0 1]  #flatten the array from multiple dimension to single dimension.
[[0 1 2]   #here after the flattern function provided single dimension array
 [3 4 5]   #the reshape function takes the input new number of the rows and columns.
 [6 7 8]
 [9 1 0]
 [1 0 1]]
[[[0 1 2 3 4]]   #here after the flattern function provided single dimention array 
 [[5 6 7 8 9]]   #the reshape function convert into 3 rows ,1 column and each column has 5 elements i.e. single dimension
 [[1 0 1 0 1]]]  #and each array has 5 elements

 
#Matrix in numpy
 
from numpy import *
a1 = array( [
            [0,1,2,3,4],
            [5,6,7,8,9],
            [1,0,1,0,1]
            ] )
print(a1)            
print(matrix(a1))

o/p: #note the matrix looks here dispaly wise same as array but internally it has different meaning and use.
[[0 1 2 3 4]
 [5 6 7 8 9]
 [1 0 1 0 1]]
 
[[0 1 2 3 4]
 [5 6 7 8 9]
 [1 0 1 0 1]]

 
from numpy import *
print(matrix('1 2 3 4 ; 4 5 6 7'))

o/p: #2 dimension array prepared because of the two list of the values with semi colon.
[[1 2 3 4]
 [4 5 6 7]] 
 
 
from numpy import *
print(matrix('1 2 ;3 4 ; 4 5 ;6 7'))

o/p: #4 rows , 2 columns
[[1 2]
 [3 4]
 [4 5]
 [6 7]]
 
from numpy import *
m = matrix('1 2 3; 4 5 6 ;7 8 9')
print(m)
print(m.diagonal()) #multi dimension
print(diagonal(m))  #single dimension

o/p: 
[[1 2 3]
 [4 5 6]
 [7 8 9]]
 
[[1 5 9]]  #first diagonal function has return multidimension array
[1 5 9]    #second diagonal function has return the single dimention array.

from numpy import *
m = matrix('1 2 3; 4 5 6 ;7 8 9')
print(m.min())
print(m.max())

o/p:  #min and max number
1
9

from numpy import *
m1 = matrix('1 2 3; 4 5 6 ;7 8 9')
m2 = matrix('9 8 7; 6 5 4 ;3 2 1')
print(m1+m2)

o/p: #addition of the two matrix , do 1 to 1 mapping for each element. agian it return the miltidimension array
[[10 10 10]
 [10 10 10]
 [10 10 10]]
 
from numpy import *
m1 = matrix('1 2 3; 4 5 6 ;7 8 9')
m2 = matrix('9 8 7; 6 5 4 ;3 2 1')
print(m1*m2)

o/p: the multiplication is complex operation and its done in faster way.
[[ 30  24  18]
 [ 84  69  54]
 [138 114  90]]
 
Functions in Python:
1) Create function
2) Call the function

#function without input parameter
def func_test():
    print('Latesh Sangani')
    print('Bye')
    
func_test() 

o/p:
Latesh Sangani
Bye

#function with input parameter and no return output parameter.
def add(a,b):
    print(a+b)

add(1,2)

o/p: 3

#function with input parameter and return output parameter
def add(a,b):
    return(a+b)

o = add(1,2)
print(o)

o/p: 3

#function with multipe input and multiple return output parameters
def add_sub(a,b):
    return(a+b,a-b)  #return a+b,a-b    -> return with braces and without braces both will work.

o1,o2 = add_sub(1,2)
print(o1,o2)

o/p: 3 -1

#function override
def func_override(i):
    i = 6
    print(i)
    return i
o = func_override(10)
print(o)


o/p:
6    #inside the function
6    #outside of the function

#function override but source information untouched.
def func_override(i):
    i = 6
    print(i)
    return i

source = 10
o = func_override(source)
print(o)
print(source)


o/p:
6   #from function
6   #Outside of the function
10  #actual source untouched


#Function address changes based on the values updates.  
#For 1 values which holds by multiple variable, all points to same address in the memory.
#The int , float, string are the inmutable. means each value occupied own address.
#both variable , both value holds different address.
def func_override(i):
    print('Before update in function ', id(i), i)
    i = 6
    print('After update in function ',id(i),i)
    return i

source = 10
print('Function entry point ',id(source),source)
o = func_override(source)
print('Function exit point',id(o) ,o)


o/p:
Function entry point  1591447153232 10
Before update in function  1591447153232 10
After update in function  1591447153104 6
Function exit point 1591447153104 6

#Same above function but in stead of the variable , the mutable list is provided input.
#here after update and before update , the list always holds the same memory address.
#here address will remain same always but both source value is automatacally overwritten by destination value.

def func_override(i):
    print('Before update in function ', id(i), i)
    i[2] = 25
    print('After update in function ',id(i) , i)
    return i

source = [10,20,30,40,50]
print('Function entry point ',id(source), source)
o = func_override(source)
print('Function exit point',id(o) , o)

o/p:
Function entry point  1554034534784 [10, 20, 30, 40, 50]
Before update in function  1554034534784 [10, 20, 30, 40, 50]
After update in function  1554034534784 [10, 20, 25, 40, 50]
Function exit point 1554034534784 [10, 20, 25, 40, 50]



def add(a,b):    #formal arguments
    print(a+b)

add(1,2)  #actual aurgements both formal and actual has same positions.

o/p: 3

#change in the argument postion.
def add(a,b):
    print(a+b)

add(b=1,a=2)

o/p: 3

#defalt value 10 for each addition and second argument not passed.
def add(a,b=10):
    print(a+b)

add(2)

o/p: 12
#default value override.
def add(a,b=10):
    print(a+b)

add(2,20)

o/p: 22

#default is always used when input is not passed , else input take 1st preference over default.

#multipe arguments or vary number of the arguments.
#input 10 is assinged to a and remaning all the values are accepted by b. hence the syntax is *b
#value of a stored in variable and value of the b will added in the form of the loop.
#The ()  indicates its tuple. where value does not possible to change and random order will not generated.

def add(a,*b):
    print(a)
    print(b)
    c = a
    for i in b:
        c = c+i
    print(c)

add(10,20,30,40,50)

o/p:
10    # a
(20, 30, 40, 50)  # *b
150   # c


#without using the a variable. just use *b and added all of them.
#*varaible is requried to use when we dont know the input number of values.

#*args and **kwargs in Python let functions accept a variable number of arguments: 
#*args packs any extra positional arguments into a tuple, 
#while **kwargs packs extra keyword arguments (like name='Alice') into a dictionary, making functions flexible for unknown inputs. 
#The * unpacks iterables (tuples, lists), 
#and ** unpacks dictionaries when calling functions, enabling powerful argument handling and decorators

def add(*b):
    print(b)
    c = 0
    for i in b:
        c = c+i
    print(c)

add(10,20,30,40,50)

o/p:
(10, 20, 30, 40, 50)
150

#Multiple arguments but without knowing the number of the arguements and which arguement belongs to what column name.
# **varaible indicate the column = values is the incoming pattern.



def store(PK,**basicinfo):
    print(PK)
    print(basicinfo)
    print(type(basicinfo))

store(1,name = 'Latesh Sangani' , gender = 'Male' , age = 35 , weight = 65 , city = 'Pune')

o/p:
1
{'name': 'Latesh Sangani', 'gender': 'Male', 'age': 35, 'weight': 65, 'city': 'Pune'}
<class 'dict'>

o/p: # in the correct form with the help of the items() function.
def store(PK,**basicinfo):
    print(PK)
    print(basicinfo)
    for i,j in basicinfo.items():    # for i,j in basicinfo:         syntax error , The items() is the mandatory function.
                                     # for i in basicinfo: it will work but it will return key only.
        print(i + ' is' ,j)

store(1,name = 'Latesh Sangani' , gender = 'Male' , age = 35 , weight = 65 , city = 'Pune')

o/p:
1
{'name': 'Latesh Sangani', 'gender': 'Male', 'age': 35, 'weight': 65, 'city': 'Pune'}
name is Latesh Sangani
gender is Male
age is 35
weight is 65
city is Pune

#scope of the variable

scope_ = 10
def scope():
    scope_ = 20
    print('Inside Function',scope_)

scope()
print('Outside Function',scope_)

o/p:
Inside Function 20
Outside Function 10


#global variable use within the function 
#the global variable is used which tells that scope_ variable is global variable
#hence outside of the function it will also holds the new values.
scope_ = 10
print('Before Function',scope_)
def scope():
    global scope_
    scope_ = 20
    print('Inside Function',scope_)
    print(id(scope_))
    x = scope_
    print('Inside Function',x)
    print(id(x))    

scope()
print('Outside Function',scope_)
print(id(scope_))

o/p:
Before Function 10
Inside Function 20
2018513453904
Inside Function 20
2018513453904
Outside Function 20
2018513453904

# global scope override

global scope_
scope_ = 10           #First time global
print('Before Function',scope_)
def scope():
    global scope_
    scope_ = 20  # second time global overside
    print('Inside Function',scope_)
    print(id(scope_))
    x = scope_
    print('Inside Function',x)
    print(id(x))

scope()
print('Outside Function',scope_)  # return the second time global over written value
print(id(scope_))

o/p:
Before Function 10
Inside Function 20
2426744826768
Inside Function 20
2426744826768
Outside Function 20
2426744826768

#globals() function is used to get the actual value outside of the function and its corrosponsing address.
#globals()[out side of local scope varibles]  
#it can be use for many of the variable declared outside of the function scope.


scope_ = 10
print(id(scope_))
def scope():

    x = globals()['scope_']
    print(id(x))
    print('Inside Function -> scope_',scope_)
    print('Inside Function -> x', x)

scope()
print('Outside Function',scope_)

o/p:

2024014610960                   #address of the scope_
2024014610960                   #address of the x
Inside Function -> scope_ 10    #scope_ values does not changed
Inside Function -> x 10         #x derived the value from the scope_ and its address.
Outside Function 10             #values same as original.



scope_ = 10
print(id(scope_))
def scope():

    x = globals()['scope_']
    print(id(x))
    print('Inside Function -> scope_',scope_)
    print('Inside Function -> x', x)
    globals()['scope_'] = 25                         #global variable value modifed

scope()
print('Outside Function',scope_)

o/p:
2024014610960                   #address of the scope_
2024014610960                   #address of the x
Inside Function -> scope_ 10    #scope_ values does not changed
Inside Function -> x 10         #x derived the value from the scope_ and its address.
Outside Function 25             #values updated because now global variable value override.



#array to accept the user input values and provide the old and even count.
from array import *
def count(list_):
    e=0
    o=0
    for i in list_:
        if i%2 == 0:
            e += 1
        else:
            o += 1
    return e,o
#step 1
arr = array('i',[])
arr_len = int(input('Enter the length of the array: '))
#step 2
for i in range(arr_len):
    arr_val = int(input('Enter the next value of array: '))
    arr.append(arr_val)
#step 3    
even,odd = count(arr)
#step 4
print("Count of even is {} and Count of odd is {}".format(even,odd))
print(f"Count of even is {even} and Count of odd is {odd}")

o/p:
Enter the length of the array: 4
Enter the next value of array: 1
Enter the next value of array: 2
Enter the next value of array: 3
Enter the next value of array: 4
Count of even is 2 and Count of odd is 2


#fibonacci sequence and apply condition dont go beyond 100 number.:
0,1,1,2,3,5,8,13,21,34,55,89 #till 12 count numbers
a,b,c
  a,b,c
    a,b,c


def fib(n):
    if n <= 0:
        print('invalid number')
        return -1
    a = 0
    b = 1

    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            if c > 100:
                return            
            print(c)

fib(12)
fib(1)
fib(-4)

#factorial of the number.
def fact(n):
    f = 1
    for i in range(1,n+1):  #0,1,2,3,4  -> 1,2,3,4 .. n+1
        f = f*i
    return f

r = fact(5)
print(r)

o/p: 120 

#The default limit of the recursion is 1000 when function call itself.
#The default limit can override by using the below code , here 2000 is the new limit for the recursion.

import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

#factorial using recursion.
def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)  # 5*fact(4) 

op = fact(5)
print(op)

o/p: 120

#Basic Lamda Function with 1 input argument and 1 output:
funct = lambda x : x * x
print(funct(30))

o/p: 900

#Basic Lamda Function with n input arguments:  only thing matter the o/p should be the single expression.
funct = lambda x,y : x + y
print(funct(30,20))

o/p: 50

max_value = lambda a, b: a if a > b  else b
print(max_value(10, 20)) 
# Output: 20

#basic syntax of lambda =>  

#lambda arguments: expression
#lambda: The keyword to define the anonymous function.
#arguments: Zero or more arguments passed to the function, separated by commas.
#expression: A single expression that is evaluated and returned when the lambda is called. 

Map-Reduced 3 functions
filter()   : it takes input the function name and the list , function can be actual function or lambda function.
map()
reduce()

#lamda function : this are the No Name Functions and it does not store the compile object in memory

def is_even(n):
    if n%2 == 0:
        return n

my_list = [10,11,12,13,14,15,16,17,18,19]
print(filter(is_even,my_list))  # it will return <filter object at 0x000001EFC1BB9D20>
print(list(filter(is_even,my_list)))  # the above output need to translate with list() function to see correct result.

o/p:  
<filter object at 0x000001EFC1BB9D20>
[10, 12, 14, 16, 18]

#shorten the code and use the lambda function.
my_list = [10,11,12,13,14,15,16,17,18,19]
print(list(filter(lambda n : n%2 == 0,my_list)))

o/p: [10, 12, 14, 16, 18]


# usage of the filter , map and reduce function with lambda.

from functools import reduce
my_list = [10,11,12,13,14,15,16,17,18,19]
f_out = list(filter(lambda n : n%2 == 0,my_list))  # filter the valid values
print(f_out)
print(type(f_out))
f_map = list(map(lambda n : n*2,f_out)) # apply mapping to all the filter values , the count of filter and map is same.
print(f_map)
print(type(f_map))
f_reduce = reduce(lambda a,b : a+b,f_map)  #reduced with mapping values make single output
print(f_reduce)
print(type(f_reduce))

o/p:
[10, 12, 14, 16, 18]
<class 'list'>
[20, 24, 28, 32, 36]
<class 'list'>
140
<class 'int'>


#decoraters used to add extra feature in the exising readymade function or user custom function.
#Here div original function is passed as input to smart_div user choice customization function.
#The user choice customization function used the another function Inner
#( Inner is not the keyword , we can use any other name) 
#dev2 is the final modified function takes output of the orignal div function.
#expected output is 2/4 = 0.5 but because of decoarters layer added its now 4/2 = 2.0
# funct and inner both are NOT the keywords, it can be test1 or test2 also.

#In Python, a decorator is a function that takes another function (or class) as an argument 
#and extends or modifies its behavior without explicitly changing its source code. 
#This is a powerful feature for adding reusable functionality like logging, timing, 
#or authentication to existing code in a clean and readable way.

#The call to the decorater function return the function object only. 


def smart_div(funct):
    def inner(a,b):
        if a < b:
            a,b = b,a
        return funct(a,b)
    return inner

def div(a,b):
    return a/b
    
div2 = smart_div(div)
print(div2(2,4))         # div2 is replaced by smart_div(div) in the below example

o/p:
2.0


#Short cut for the print and function calling

def div(a,b):
    return a/b
def smart_div(funct):
    def inner(a,b):
        if a < b:
            a,b = b,a
        return funct(a,b)
    return inner

print(smart_div(div)(2,4))

o/p:
2.0

def uppercase_decorator(func):
    def wrapper():
        return func().upper()
    return wrapper

def say_hello():
    return "Hello, world!"

output = uppercase_decorator(say_hello)
print(output())
# Output: HELLO, WORLD!


#importing the local modules

#let say calc.py is one exisitng file which contains all the application related functions.

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b
    
#Now use the calc.py file imported into Latesh_Learning.py file
#here calc is the python file name

from calc import *
print(add(3,4))
print(sub(3,4))
print(multi(3,4))
print(div(3,4))

o/p:
7
-1
12
0.75

#Use of the __name__ variable. The main is the starting point of execution like C has main function.
#If the script is run directly, the Python interpreter sets the __name__ variable to the string "__main__"
#If the script is imported as a module into another script, __name__ is set to the module's actual name (e.g., if the file is named helper.py, __name__ becomes "helper"). 
#Write the below print line in the Latesh_Learning.py and get the output __main__

print(__name__)
o/p:  __main__

#now new file variables_test.py is the new file and it has below content

print("variables_test.py  " + __name__)

#import the variables_test.py in the Latesh_Learning.py , below is the code for the Latesh_Learning.py

import variables_test
print("Latesh_Learning.py  " + __name__)

#running just variables_test.py gives below output:
o/p:  variables_test.py   __main__

#running Latesh_Learning.py gives below output:

variables_test.py  variables_test     #> coming from variables_test.py
Latesh_Learning.py  __main__          #> coming from Latesh_Learning.py


#new set of example 

#Latesh_Learning.py code

def main():
    print("I am the parent function")

if __name__ == '__main__':
    main()


o/p: "I am the parent function"

#variables_test.py  code 

import Latesh_Learning

print("I am the child function")

o/p: I am the child function

here even the Latesh_Learning module was imported in the code of variables_test.py
only "I am the child function" printed and parent code "I am the parent function" output does not came.
because the condition wrote  __name__ == '__main__' and it will evaluated as Latesh_Learning == '__main__' which is false.


#standard use of the main function 

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b
def main():
    print(add(4,5))
    print(sub(4,5))
    print(multi(4,5))
    print(div(4,5))
main()

o/p:
9
-1
20
0.8


#Latesh_Learning.py   , call the fun3 function from the inside of fun1

# File1 :  variables_test.py

def fun3():
    print('fun3', __name__)

def fun4():
    print('fun4', __name__)

def main():
    print('In main of the variables_test.py')
    fun3()
    fun4()
    
main() 

   
# File 2 : Latesh_Learning.py
from variables_test import fun3
def fun1():
    fun3()
    print('fun1',__name__)
def fun2():
    print('fun2',__name__)
def main():
    fun1()
    fun2()

main()


Output : 
Running variables_test.py
o/p:
In main of the variables_test.py
fun3 __main__
fun4 __main__

Running Latesh_Learning.py
o/p:  #first imported function output printed and then own output printed.  
      #because when module variables_test loaded and even we just asked to load fun3 function 
      #but python loaded internally entire all the module because main() function is getting called.
      #and main called both fun3 and fun4 function.

In main of the variables_test.py   # coming from the variables_test.py
fun3 variables_test # coming from the variables_test.py -> main() -> fun3
fun4 variables_test # coming from the variables_test.py -> main() -> fun4
fun3 variables_test # coming from the variables_test.py -> main() -> fun3 because of import of module
fun1 __main__
fun2 __main__

#to over come from this problem , use the extra lines of the code in the variables_test.py

def fun3():
    print('fun3', __name__)

def fun4():
    print('fun4', __name__)

def main():
    fun3()
    fun4()

if __name__ == '__main_':
    main()


#now again run the Latesh_Learning.py  , the first 3 lines from the previous output of the main are skipped.
#See this logic __name__ == '__main_' skipped entire excution of the all the functions 
#but the Latesh_Learning.py has imported fun3 only then only fun3 code executed and fun4 gets skipped out.

o/p:

fun3 variables_test
fun1 __main__
fun2 __main__

#Lesson:
#1) use the if __name__ == '__main_': logic in the imported child files only.
#2) the parent or orcherestraor file should avoid point 1 if condition.

key point of the python selling , becasue it supports 
1) Function Programming
2) Procedure programming
3) Very Important Object oriented programming.

OOPs concept has below behaviours
1) Object
2) Class
3) Encapsulation
4) Polymorphism
5) Abstraction
6) Inheratance

#class is called as design or blueprint 
#object is called as instance or production of the class.
#class declaration does not accept intput parameter like class myclass(i,j) 
# but the __init__ method of the class takes input values.
#but while calling the contructor of the class values can be pass as input.
#inside class the ready made function like print or user made function both can call and declare.

#Basic Class code:

#CLASS vs FUNCTION Syntax Diff
class my(): #class
    print('inside my class')

c = my()             # this is the constructor initilization.
print(type(c))

def my(): #function
    print('inside my function')

c = my()             # this is the function initilization.
print(type(c))

o/p:
inside my class
<class '__main__.my'>
inside my function
<class 'NoneType'>

#calling object method , self is the keyword in the python.

class myclass():
    print('My First class')
    def class_method(self):
        print('I am class method')

c = myclass()
myclass.class_method(c)    # input object variable is provided

o/p: 
My First class
I am class method

Alternate Way and very common syntax to follow.

class myclass():
    print('My First class')
    def class_method(self):
        print('I am class method')

c = myclass()
c.class_method()    # object.method()

o/p: 
My First class
I am class method

# If we dont write the self ,in the call method , its gives the error.
class myclass():
    print('My First class')
    def class_method():
        print('I am class method')

c = myclass()
c.class_method()    # object.method()

o/p:
TypeError: class_method() takes 0 positional arguments but 1 was given

#sample program to call integer class.

a = 5
print(a.bit_length())
o/p: 3

#class with use of the variables in it.
#the input need to provide while making object from the constructor.
#While making the object from Computer('8','i7') we just write the vales in it but call to method is still not involved.
#the c1.config() is the final call which is method calling and internally its being translted to config(c1,'8','i7')
#config(c1,'8','i7')  here c1 is referring to the self keyword of the __init__(self,ram,cpu)
#__init__  is the constructor initilization first called to set some default values
# and later if required this value can override

class Computer():
    def __init__(self,ram,cpu):
        self.ram = ram  # the input varaible can be copied to any self.variable. ex:  self.a = ram also fine
        self.cpu = cpu  # the self keyword is mandatory

    def config(self):
        print("The configuration is " ,self.ram , self.cpu)


c1 = Computer('8','i7')
print(c1.ram,c1.cpu)
c1.config()

c2 = Computer('10','i6')
print(c2.ram,c2.cpu)
c2.config()

o/p:
8 i7
The configuration is  8 i7
10 i6
The configuration is  10 i6


#Object does not refer to same memory location like int do.

class Computer:
    pass

c1 = Computer()
print(id(c1))
c2 = Computer()
print(id(c2))
a=5
print(id(a))
b=5
print(id(b))

o/p: 
1842392046160  #memory of the c1
1842392046208  #memory of the c2
1842390565232  #memory of the a=5
1842390565232  #memory of the b=5

# rerunning same above code will give the new address.

#The size of the object is depends on the size of the variables.

#Constructor default value overwriting OUTSIDE of Class
class Computer:
    def __init__(self):
        self.name = 'Latesh'
        self.surname = 'Sangani'

c1 = Computer()
c1.name = 'Ram'
print(c1.name , c1.surname)

c2 = Computer()
c2.surname = 'Gaglani'
print(c2.name , c2.surname)

o/p:
Ram Sangani
Latesh Gaglani

#updating the values from the other method of the class.
#the value get modifed for that object values only 
#the other object that does not call the update function and hence its value will be inact.
#Constructor default value overwriting INSIDE of Class
class Computer:
    def __init__(self):
        self.name = 'Latesh'
        self.surname = 'Sangani'
    def update(self):
        self.name = 'Jay'

c1 = Computer()
c1.name = 'Ram'
print(c1.name , c1.surname)
c1.update()
print(c1.name , c1.surname)

c2 = Computer()
c2.surname = 'Gaglani'
print(c2.name , c2.surname)
c2.update()
print(c2.name , c2.surname)

o/p:
Ram Sangani
Jay Sangani
Latesh Gaglani
Jay Gaglani

#compare the values for the 2 objects.
class Computer:
    def __init__(self):
        self.name = 'Latesh'
        self.surname = 'Sangani'
    def compare(self,object2):
        if self.name == object2.name:
            print("Matching")
        else:
            print("Not Matching")

c1 = Computer()
c2 = Computer()
c1.compare(c2)     # internally its call this way compare(c1,c2) and c1 will replace by self and c2 will replace by object2

o/p: Matching

#if c2 value gets override then output will be differ.

c1 = Computer()
c2 = Computer()
c2.name = 'Rocky'
c1.compare(c2)

o/p: Not Matching


# class variables are stored in the "class namespace".
# method variables(or instance variables) are stored in the "instance namespace".

class Computer:
    common_variable = 'Human'
    def __init__(self):
        self.name = 'Latesh'  #contructor initilization does not pass any value 
        self.surname = 'Sangani'  #but default value is fixed for all the objects

c1 = Computer()
c2 = Computer()
c2.common_variable = 'Animal'
print(c1.name , c1.surname , c1.common_variable)
print(c2.name , c2.surname , c2.common_variable)
Computer.common_variable = 'Animal'
print(c1.name , c1.surname , c1.common_variable)
print(c2.name , c2.surname , c2.common_variable)


o/p:  
#here even c2.common_variable = 'Animal' override the values , but the value for the c1.common_variable does not changed.
#Computer.common_variable = 'Animal'  : here class_name.common_variable will affect for all the objects using it.

Latesh Sangani Human
Latesh Sangani Animal
Latesh Sangani Animal
Latesh Sangani Animal



class student():  # () this is optional
    school = 'Manibai'
    def __init__(self,Eng,Mat,Sci):  # default value passed from the constructor initilzation.
        self.Eng = Eng
        self.Mat = Mat
        self.Sci = Sci
    def avg_marks(self):
        return (self.Eng + self.Mat + self.Sci)/3
    def get_Eng(self):
        return self.Eng
    def set_Eng(self,new_value):
        self.Eng = new_value
        print(self.Eng)

s1 = student(23,45,34)
s2 = student(12,43,40)
print(s1.avg_marks())
print(s2.avg_marks())
print(s1.get_Eng())
s1.set_Eng(50)
print(s1.Eng)
print(s1.set_Eng(50))

o/p:
34.0    # s1.avg_marks()
31.666666666666668    # s2.avg_marks()
23   # s1.get_Eng()
50   # s1.set_Eng(50)
50   # print(s1.Eng)
None # print(s1.set_Eng(50))



#use of the cls keyword like self,cls is also the keyword.
#avg_marks is the instance method
#school_ is the class method.
#info is  the static method.
#@classmethod and @staticmethod are the decoraters.
#The @classmethod decorator in Python defines a method that is bound to the class rather than a specific instance of the class. 
#When a class method is called, the class itself is passed as the first argument to the method, conventionally named cls

class student():
    school = 'Manibai'
    def __init__(self,Eng,Mat,Sci):  #default class initilization
        self.Eng = Eng
        self.Mat = Mat
        self.Sci = Sci
    def avg_marks(self):  # class object method
        return (self.Eng + self.Mat + self.Sci)/3
    @classmethod
    def school_(cls):  # class own method
        return cls.school
    @staticmethod # decorator in Python defines a method that belongs to a class but does not require access to instance-specific data (self) or class-specific data (cls)
    def info(): # generic method , does not need the self or cls as input.
        print('Welcome to the school')

#way1
s1 = student(23,45,34)
print(s1.avg_marks())
print(student.school_())
student.info()

#way2
s1 = student(23,45,34)
print(s1.avg_marks())
print(s1.school_())
s1.info()

o/p:
34.0
Manibai
Welcome to the school


#Main Class ( Outer class ) and Child class ( Inner class) example.  
#both inner class object has 2 different memory location.

class Student():
    def __init__(self,name,roll_no,standard):
        self.name = name
        self.roll_no = roll_no
        self.standard = standard
        self.lap_obj = Student.Laptop()         #initilized inner class.

    def display(self):
        print(self.name , self.roll_no , self.standard)

    class Laptop():                            #inner class on same level of the methods.
        def __init__(self):
            self.brand = 'Lenova'

s1 = Student('Latesh Sangani',23,'BE COMS')   #initilized outer class.
s1.display()
s2 = Student('Vaneesa Sangani',45,'BE Space')
s2.display()
print(s1.lap_obj.brand)
print(s2.lap_obj.brand)
print(id(s1.lap_obj))
print(id(s2.lap_obj))

o/p:
Latesh Sangani 23 BE COMS
Vaneesa Sangani 45 BE Space
Lenova
Lenova
3058560450128
3058560449888



#intialized innner class in the main program , insted of the outer class.
#both class has same method name ( Method : display ) but both has 2 different scope.

class Student():
    def __init__(self,name,roll_no,standard):
        self.name = name
        self.roll_no = roll_no
        self.standard = standard

    def display(self):
        print(self.name , self.roll_no , self.standard)

    class Laptop():
        def __init__(self):
            self.brand = 'Lenova'
            
        def display(self):
            print(self.brand)

s1 = Student('Latesh Sangani',23,'BE COMS')   #outer class initilization
s1.display()
s2 = Student.Laptop()                         #inner class initilization , Here Student() class is not initilized.
s2.display()
s3 = Student('Latesh Sangani',23,'BE COMS').Laptop()  #both Inter and Outer are initilized. But Inner class object will only return.
s3.display()
s4 = Student().Laptop() # Note this line will failed as Student Class Failed to Initilaied.

o/p:
Latesh Sangani 23 BE COMS
Lenova
Lenova


#initilization and do all the operation of the inner class inside the outerclass
class Student():
    def __init__(self,name,roll_no,standard):
        self.name = name
        self.roll_no = roll_no
        self.standard = standard
        self.lap_obj = self.Laptop()                    or     self.lap_obj = Student.Laptop()

    def display(self):
        print(self.name , self.roll_no , self.standard)
        self.lap_obj.display()

    class Laptop():
        def __init__(self):
            self.brand = 'Lenova'
        def display(self):
            print(self.brand)

s1 = Student('Latesh Sangani',23,'BE COMS')
s1.display()

o/p:
Latesh Sangani 23 BE COMS
Lenova

#Inheratance : A is the super class( or Parent class)  And B is the subclass( or child class) 
#all the feature of the class A is inherated by class B.
#below is the example of the single level inheratance.

class A:
    def method1(self):
        print('Inside A.method1')
    def method2(self):
        print('Inside A.method2')

class B(A):  #input is parent class A
    def method3(self):
        print('Inside B.method3')
    def method4(self):
        print('Inside B.method4')

a = A()
a.method1()
a.method2()
b = B()
b.method1()
b.method2()
b.method3()
b.method4()

o/p:
Inside A.method1
Inside A.method2
Inside A.method1
Inside A.method2
Inside B.method3
Inside B.method4


#below is the example of the Multiple level inheratance. 
#Where class C inhireted from Class B and Class B inherated from Class A.

class A:
    def method1(self):
        print('Inside A.method1')
    def method2(self):
        print('Inside A.method2')

class B(A):
    def method3(self):
        print('Inside B.method3')
    def method4(self):
        print('Inside B.method4')

class C(B):
    def method5(self):
        print('Inside C.method5')
    def method6(self):
        print('Inside C.method6')

a = A()
b = B()
c = C()
c.method1()
c.method2()
c.method3()
c.method4()
c.method5()
c.method6()


o/p:
Inside A.method1
Inside A.method2
Inside B.method3
Inside B.method4
Inside C.method5
Inside C.method6

#below is the example of the Multiple's inheratance. Where Class C inhireted from both Class A and B.


class A:
    def method1(self):
        print('Inside A.method1')
    def method2(self):
        print('Inside A.method2')

class B:
    def method3(self):
        print('Inside B.method3')
    def method4(self):
        print('Inside B.method4')

class C(A,B):
    def method5(self):
        print('Inside C.method5')
    def method6(self):
        print('Inside C.method6')

c = C()
c.method1()
c.method2()
c.method3()
c.method4()
c.method5()
c.method6()

o/p:
Inside A.method1
Inside A.method2
Inside B.method3
Inside B.method4
Inside C.method5
Inside C.method6

#here Class B is initilized and immedetaly it called the initilization of class A. 
#because __init__ is initilization method , not the user defined method.
#here class B has missing own __init__ method and goes to loop up at A
class A:
    def __init__(self):
        print('Inside A.init')

class B(A):
    def method(self):
        print('Inside B.method')

b = B()
b.method()

o/p:
Inside A.init
Inside B.method


#Now class B has own __init__ method and class A has also own __init__ method.

class A:
    def __init__(self):
        print('Inside A.init')

class B(A):
    def __init__(self):
        print('Inside B.init')

    def method(self):
        print('Inside B.method')

b = B()
b.method()


o/p:
Inside B.init
Inside B.method


#Now to get the __init__ method of the both class A from class B, The super() will be invoke from the __init__ method of the class B.


class A:
    def __init__(self):
        print('Inside A.init')

class B(A):
    def __init__(self):
        super().__init__()
        print('Inside B.init')

    def method(self):
        print('Inside B.method')

b = B()
b.method()

o/p:
Inside A.init
Inside B.init
Inside B.method

#Now Class C has its own init and it inherated both A and B
class A:
    def __init__(self):
        print('Inside A.init')

class B:
    def __init__(self):
        print('Inside B.init')

class C(A,B):
    def __init__(self):
        print('Inside C.init')

c = C()

o/p:
Inside C.init

#Class C called the super() class but class C has both A and B two superclass. and it took the init() value of A class only.
#Here if class C(B,A) was wrote then output of the B.__init__ will be taken first, As it will go from left to right.
class A:
    def __init__(self):
        print('Inside A.init')

class B:
    def __init__(self):
        print('Inside B.init')

class C(A,B):
    def __init__(self):
        super().__init__()
        print('Inside C.init')

c = C()

o/p:
Inside A.init
Inside C.init

#same init logic applied to user defined method also
#Class C called the super() class but class C has both A and B two superclass. 
#and it took the method() value of A class only.
#Here if class C(B,A) was wrote then output of the B.method will be taken first, As it will go from left to right.

class A:
    def __init__(self):
        print('Inside A.init')
    def method(self):
        print('Inside A.method')

class B:
    def __init__(self):
        print('Inside B.init')
    def method(self):
        print('Inside B.method')

class C(A,B):
    def __init__(self):
        super().__init__()
        print('Inside C.init')

c = C()
c.method()

o/p:
Inside A.init
Inside C.init
Inside A.method

#the above problem can fixed with MRO( Method resolution order ) 

# The super() function can be used for the __init__ and regular user defined method.
class A:
    def __init__(self):
        print('Inside A.init')
    def method(self):
        print('Inside A.method')

class B:
    def __init__(self):
        print('Inside B.init')
    def method(self):
        print('Inside B.method')

class C(A,B):
    def __init__(self):
        super().__init__()
        print('Inside C.init')
    def method(self):
        super().method()
        print('Inside C.method')

c = C()
c.method()

o/p:
Inside A.init
Inside C.init
Inside A.method
Inside C.method


Polymorphism in Python is the ability of a single function, method, or operator to behave differently depending on the type or class of object it is operating on

Polymorphisim has 4 types:
1) Duck Typing
2) Operator Overloading  ex: operator like + , - , / , * , < , > etc...
3) Method Overloading
4) Method Overriding

1) Duck Typing
#Example  for the python code development have Laptop is required 
#but we can have single or multiple IDE present to work on it.
#input object is passed to call method of another class.

class Pycharm:
    def showcase(self):
        print('Python Code Development Platform')

class Laptop:
    def Lap_Method(self,ide_object):
        ide_object.showcase()

p = Pycharm()
l = Laptop()
l.Lap_Method(p)

o/p:
Python Code Development Platform

#now second IDE IDLE is present and it has different purpose but same method.
class Pycharm:
    def showcase(self):
        print('Python Code Development Platform')
        
class IDLE:
    def showcase(self):
        print('Python Command Prompt Code Development Platform')

class Laptop:
    def Lap_Method(self,ide_object):
        ide_object.showcase()     #it will go to the Pycharm class or IDLE class it will be decided what object you are passing.

p = Pycharm()
i = IDLE()
l = Laptop()
l.Lap_Method(p)
l.Lap_Method(i)

o/p:
Python Code Development Platform
Python Command Prompt Code Development Platform

2) Operator Overloading  
#here a and b are operands and + is operator . The existing python operator are override.
#both a and b of class int , hence print(a+b) internally convert into print(int.__add__(a,b)) , 
#as the __add__ is the method of the class int.
a = 4
b = 5
print(a+b)
print(int.__add__(a,b))

o/p:
9
9

#same applies for the string (str) class datatypes also.

a = '4'
b = '5'
print(a+b)
print(str.__add__(a,b))

o/p:
45
45

#+ is the python standard operator for datatypes but when we do SUM of the two objects 
#it will NOT work because private method of the class does not know the __add__ 

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, object2):
        m1 = self.m1 + object2.m1
        m2 = self.m2 + object2.m2
        s3 = Student(m1,m2)
        return s3

s1 = Student(10,20)
s2 = Student(20,10)
s3 = s1+s2                          #internally it will translate into __add__(s1,s2)
print(s3.m1 , s3.m2)

o/p:
30 30

# > (Greater than) is the python standard operator for datatypes 
#but when we do > of the two objects it will NOT work because private method of the class does not know the __gt__ 
class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __gt__(self, object2):
        r1 = self.m1 + self.m2   #19
        r2 = object2.m1 + object2.m2  #32

        if r1 > r2:   # 19>32
            return True
        else:
            return False

s1 = Student(11,8)
s2 = Student(21,11)
if s1>s2:                             #internally it will translate into __gt__(s1,s2)
    print('s1 is greater')
else:
    print('s2 is greater')
    
o/p:
s2 is greater


#While prining the value of the variable , it will show actual value 
#but for the the object it shows its location address

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

a = 5
print(a)
print(a.__str__())       # internally print(a) is replaced by print(a.__str__())
s1 = Student(11,8)
print(s1)
print(s1.__str__())      # internally print(s1) is replaced by print(s1.__str__()) 

o/p:
5
5
<__main__.Student object at 0x000001E2586FBFD0>
<__main__.Student object at 0x000001E2586FBFD0>


#to print the values of the object s1 , the __str__ defined and it will the object specific operation.
class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __str__(self):
        return self.m1, self.m2

s1 = Student(11,8)
print(s1.__str__())
print(s1) # this line will be failed with error "__str__ returned non-string (type tuple)"
o/p:
(11, 8)

#another enhancement to get the string value instead of the tuple(11,8)
class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)

s1 = Student(11,8)
print(s1.__str__())
print(s1)

o/p:
11 8
11 8


3) Method Overloading :  Same method name but number of arguments varied or data types of the argumuments varied.
4) Method Overriding  :  Same method name , same number of arguments varied ,same data types of the argumuments 
                         but both methods are in the form of parent and child class.

#Method overloading does not directely support in the python but it will support programatacally with multiple conditions.

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def plus(self,m1=None,m2=None,m3=None):                        #in case less value passed the None will be accepted.
        s=0
        if m1 != None and m2 != None and m3 != None:
            s = m1+m2+m3
        elif m1 != None and m2 !=None and m3 == None:
            s = m1+m2
        else:
            s = m1
        return s

s1 = Student(11,8)     #default values are inilitiezed but it was not use because plus method is not using it self.m1...
print(s1.plus(5))        
print(s1.plus(5,3))
print(s1.plus(5,3,7))

o/p: 
5
8
15


4) Method overriding:
#if Latesh class does not have phone method , it will use from the Kishor class phone method
#but because Latesh class got the same method, Python given first preference to it.

class Kishor:
    def phone(self):
        print("RedMi Phone")
class Latesh(Kishor):
    def phone(self):
        print('Samsung M21')
a = Kishor()
a.phone()
b = Latesh()
b.phone()

o/p:  
RedMi Phone
Samsung M21



# Multiple ways of printing list values but special function iter is available to hold the previous value
# __next__ method used to get next values, this is python readymade method.

my_list = [10,20,30,40,50]
print('--------counter logic--------')
print(my_list[0],my_list[1],my_list[2],my_list[3],my_list[4])
print('--------for loop logic--------')
for i in my_list:
    print(i)
print('--------for loop with range logic--------')
for i in range(0,5):
    print(my_list[i])
print('--------iterator logic--------')
it = iter(my_list)
print(it)   # <list_iterator object at 0x00000267EE3D8310>
print(it.__next__()) # 10
print(next(it)) # 20
print(next(it)) # 30


o/p:
--------counter logic--------
10 20 30 40 50
--------for loop logic--------
10
20
30
40
50
--------for loop with range logic--------
10
20
30
40
50
--------iterator logic--------
10
20
30

#Persoanlized iterator logic where next values before coming available to dispay
# or use is calculated in the current call only.
#note here __init__  __iter__ __next__ are the python own function where we are overwriting own logic.
#StopIteration python exception value is used to stop the for loop logic.
#let say iteration is for the 10 know set of values.


class my_iteration:
    def __init__(self):
        self.n = 1
    def __iter__(self):
        return  self
    def __next__(self):

        if self.n <= 10:
            old_value = self.n
            self.n = self.n + 1
            return old_value
        else:
            raise StopIteration

obj = my_iteration()
print(obj.__next__())
print(obj.__next__())

o/p:  #here two times print wrote and hence next 2 values came up
1
2

# but here for loop is used to see all the possible values.

class my_iteration:
    def __init__(self):
        self.n = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.n <= 10:
            old_value = self.n
            self.n = self.n + 1
            return old_value
        else:
            raise StopIteration

obj = my_iteration()
for i in obj:
    print(i)

o/p:
1
2
3
4
5
6
7
8
9
10


#Generators : it has similarites with iterators , generators return the iterators.
#function with RETURN Vs YIELD. 
# RETURN send the single calcualted value but YIELD send the pre-calculated for all the next iteration.


def my_function():
    return 5
def my_generators():
    yield 5

f = my_function()
print(f)
g = my_generators()
print(g)

o/p:
5
<generator object my_generators at 0x0000024DF94299A0>

# to get the values from the generators used the next function.

def my_function():
    return 5
def my_generators():
    yield 5

f = my_function()
print(f)
g = my_generators()
print(next(g))                   #  or    print(g.__next__())

o/p:
5
5

#Multiple times writing the yield keyword , with each print() value , it shows the new value.
def my_generators():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

g = my_generators()
print(next(g))
print(next(g))

o/p:
1
2


#the first two values coming from the first(1) and second(2) print and rest of the values(3,4,5) coming from the for loop.
def my_generators():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

g = my_generators() # all the values of the generators are preloaded in the memory with FUNCTION initilization.
print(next(g)) #1
print(next(g)) #2
print('----------------')
for i in g:
    print(i) #3,4,5
    
o/p:
1
2
----------------
3
4
5
    
#return after sending the values it will stop but yield will still hold the values.

def gen_sqre():
    i = 0
    while i <= 10:
        sq_ = i*i
        yield sq_
        i = i+1

g_obj = gen_sqre() # all the Square Root are preloaded in the memory with function all 
for i in g_obj:
    print(i)

o/p:
0
1
4
9
16
25
36
49
64
81
100

#with for loop

def gen_sqre():
    for i in range(11):  #0..10
        sq_ = i*i
        yield sq_
        
g_obj = gen_sqre()
for i in g_obj:
    print(i)

o/p:
0
1
4
9
16
25
36
49
64
81
100

#to confirm return will come back to original call and does not move to next values , replaced yield with return.

def gen_sqre():
    i = 2
    while i <= 10:
        sq_ = i*i
        return sq_
        i = i+1

g_obj = gen_sqre()
print(g_obj)

o/p: #here loop started from 2 because square of the 0 and 1 will be 0 and 1 only. to make sure new values is coming started with 2.
4

#with return keyword the for loop cannot be used because python throw  the error.
#error 

for i in g_obj:
    print(i)
   
error :
    for i in g_obj:
TypeError: 'int' object is not iterable   



# Python has 3 types of the errors
1) Compile time error  : Syntax or incorrect spelling of the keyword.
2) Logical error  : incorrect output ex: 2+2 = 5 
3) Run time error : ex: 6/0 


#Basic Exception block

a=3
b=0
try:
    print(a/b)
except Exception:
    print("Number cannot be divide by 0")
print("bye")

# alias of the Exception e or any user defined letter. 
a=3
b=0
try:
    print(a/b)
except Exception as e:
    print("Number cannot be divide by 0 : " , e)
print("bye")

o/p:
Number cannot be divide by 0 :  division by zero
bye


#use of the finally keyword: 
#except Exception only executed only when errors are coming.
#finally always will execute in case of error , in case of non-errors.
a=3
b=0
try:
    print("database connection open")
    print(a/b)
except Exception as e:
    print("Number cannot be divide by 0 : " , e)
finally:
    print("database connection closed")
print("bye")

o/p:
database connection open
Number cannot be divide by 0 :  division by zero
database connection closed
bye


a=3
b=0
i = int(input('Enter the string value for testing purpose : '))
print(i)
try:
    print("database connection open")
    print(a/b)
except Exception as e:
    print("Number cannot be divide by 0 : " , e)
finally:
    print("database connection closed")
print("bye")

o/p: let say input value given is 'r'
i = int(input('Enter the string value for testing purpose : '))
ValueError: invalid literal for int() with base 10: 'r'

#see here division by zero  and ValueError are the python defined errors.

#good program with all the possible handellings
#try with b=0 , try with integer values as s.
try:
    a = 3
    b = 2
    print("database connection open")
    print(a/b)
    i = int(input('Enter the string value for testing purpose : '))
    print(i)
except ValueError as v:
    print("Invalid Number : " , v)
except ZeroDivisionError as z:
    print("Number cannot be divide by 0 : " , z)
except Exception as e:
    print("Unknown Exception : " , e)
finally:
    print("database connection closed")
print("bye")

o/p:  #input integer is s
Enter the string value for testing purpose : s
Invalid Number :  invalid literal for int() with base 10: 's'
database connection closed
bye

o/p: #value of b = 0
database connection open
Number cannot be divide by 0 :  division by zero
database connection closed
bye


Multi Threading :  Dividing big task into small task and again small task into its subtask.
by default any execution has 1 thread. 
The run() and the start() are the two readymade methods for the multi threading.

from threading import *
class thread_1(Thread):
    def run(self):
        for i in range(500):
            print('Latesh')


class thread_2(Thread):
    def run(self):
        for i in range(500):
            print('Sangani')

t1 = thread_1()
t2 = thread_2()
t1.start()   # invoke start even its not in the class
t2.start()

o/p:
#here in output multiple times Latesh and Sangnai is coming in output. 
#and many of the places "Sangani Latesh" and "Latesh Sangani" combine string are coming. 
#This combine output is called as collision.

#To make the both methods running in parallel 1 by 1 , use the sleep keyword to make them running.
#Sleep here just to replicate behavior. in real world the process takes much time and hence automatacally with below code the threads gets opened.
#because the entire execution is very fast in the milli seconds. Hence sleep applied to provide some break.

from time import sleep
from threading import *
class thread_1(Thread):
    def run(self):
        for i in range(500):
            print('Latesh')
            sleep(1)

class thread_2(Thread):
    def run(self):
        for i in range(500):
            print('Sangani')
            sleep(1)

t1 = thread_1()
t2 = thread_2()
t1.start()
sleep(0.2)
t2.start()




#in the above code 3 threads gets opened
t1.start()  #Main thread
sleep(0.2)  #t1 thread
t2.start()  #t2 thread


#with below exmaple ,the bye is the last code to be run , but it running also in between t1 and t2 because main thread is printing it.

from time import sleep
from threading import *
class thread_1(Thread):
    def run(self):
        for i in range(500):
            print('Latesh')
            sleep(1)


class thread_2(Thread):
    def run(self):
        for i in range(500):
            print('Sangani')
            sleep(1)

t1 = thread_1()
t2 = thread_2()
t1.start()
sleep(1)
t2.start()
print('bye')

o/p:
Latesh
Latesh
Sanganibye
- - - - 

#to over come from the above problem,  the join() method is used , it will tell main thread to let over the t1 and t2.


from time import sleep
from threading import *
class thread_1(Thread):
    def run(self):
        for i in range(5):
            print('Latesh')
            sleep(1)


class thread_2(Thread):
    def run(self):
        for i in range(5):
            print('Sangani')
            sleep(1)

t1 = thread_1()
t2 = thread_2()
t1.start()
sleep(1)
t2.start()
t1.join()
t2.join()
print('bye')


#file reading in python.
#let say 1 file is present in the path C:\Users\Lenovo\OneDrive\Technology\Python\PyCharm_Project\FileOperations.txt
#it has below content 

Latesh    self
Sangani   Surname
Manibai - School
Amravai - School
Pune  >   Hometown
Mumbai >   City

f = open("FileOperations.txt",'r')
print(f)

o/p:
<_io.TextIOWrapper name='FileOperations.txt' mode='r' encoding='cp1252'>


f = open("FileOperations.txt",'r')
print(f.read())

o/p:  #print the entire line content.
Latesh    self
Sangani   Surname
Manibai - School
Amravai - School
Pune  >   Hometown
Mumbai >   City


f = open("FileOperations.txt",'r')
print(f.read())

f = open("FileOperations.txt",'r')
print(f.readline())
print(f.readline())
print(f.readline())

#print the first three lines , each readline holds the value and pointer points to new location.
o/p:
Latesh    self
Sangani   Surname
Manibai - School

f = open("FileOperations.txt",'r')
print(f.readline(3))

#here readline expected to print 3rd line but this function gives 3 chars in the output for the first line.
# So it expect input number of the char are required to print
o/p:
Lat

f = open("FileOperations.txt",'r')
print(f.readlines())

o/p:
here all the lines will converted into the list 
['Latesh    self\n', 'Sangani   Surname\n', 'Manibai - School\n', 'Amravai - School\n', 'Pune  >   Hometown\n', 'Mumbai >   City\n']

f = open("FileOperations.txt",'r')
print(f.readable())

o/p: it provide the boolean value , the file is readable yes or no.
True

# File Writing
# First here it will check  FileWrite.txt is present , if yes then it will open for the writing, 
#in case file does found , it will make new file and write in it.

f = open("FileWrite.txt",'w')
f.write('latesh first python write')
f.write('latesh second python write')

#new file FileWrite.txt prepared in same path and it has below content.  
#all in the single line.
#one problem with write , all the previos text will be loose out with new execution of the same python file 
#with different write line of text.

o/p:
latesh first python writelatesh second python write

#to over come from the Write operation problem, use the append mode.

f = open("FileWrite.txt",'a')
f.write('latesh third python write in append mode')

#Already the file FileWrite.txt has this line of the content "latesh first python writelatesh second python write"
#and now with append mode , the new content 3rd line added 

o/p:
latesh first python writelatesh second python writelatesh third python write in append mode

#Copy operation from 1 file to read and on second file to write.
#Assume the source.txt file exists and it has below content to read.

a|b|c|d|1|2|3|4
x|y|z|oo|1|2|3|4
12.4|ft5|_45|sdf|1234|5ft6|5#5|6_7


f1 = open("source.txt",'r')
f2 = open("write.txt",'w')
for i in f1:
    print(i)
    f2.write(i)

o/p:  #each print by default open the new line , hence gap can be seen.
a|b|c|d|1|2|3|4

x|y|z|oo|1|2|3|4

12.4|ft5|_45|sdf|1234|5ft6|5#5|6_7

#if the file is image then rb ( read binary) is required to use to read the binary content of the file.

f1 = open("Latesh.jpg",'rb')
for i in f1:
    print(i)
    
o/p:
b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00`\x00`\x00\x00\xff\xe1\x00ZExif\x00\x00MM\x00*\x00\x00\x00\x08\x00\x05\x03\x01\x00\x05\x00\x00\x00\x01\x00\x00\x00J\x03\x03\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00Q\x10\x00\x01\x00\x00\x00\x01\x01\x00\x00\x00Q\x11\x00\x04\x00\x00\x00\x01\x00\x00\x0e\xc3Q\x12\x00\x04\x00\x00\x00\x01\x00\x00\x0e\xc3\x00\x00\x00\x00\x00\x01\x86\xa0\x00\x00\xb1\x8f\xff\xdb\x00C\x00\x02\x01\x01\x02\x01\x01\x02\x02\x02\x02\x02\x02\x02\x02\x03\x05\x03\x03\x03\x03\x03\x06\x04\x04\x03\x05\x07\x06\x07\x07\x07\x06\x07\x07\x08\t\x0b\t\x08\x08\n'
b'\x08\x07\x07\n'
b'\r\n'
b'\n'
- - -  -
- - -  -  -

#Code to copy the image , read from Latesh.jpg and write into Copy_Image.jpg

f1 = open("Latesh.jpg",'rb')
f2 = open("Copy_Image.jpg" , 'wb')
for i in f1:
    f2.write(i)
    
# Close() method used to close the file whether its in read or write mode.
# in the below code after writing in the file write.txt , we cannot immedetaly read the file because file is still open and its in write mode.
# first the file is required to closed and then again open in the read mode , after this only file content will be readable.
f1 = open("source.txt",'r')
f2 = open("write.txt",'w')
for i in f1:
    print(i)
    f2.write(i)
f1.close()
f2.close()
f2 = open("write.txt",'r')
f2.read()

# Traditional try...finally method (less concise)
file = open('example.txt', 'w')
try:
    file.write('Hello, World!')
finally:
    file.close() # Manual closing required

# Using the with statement (recommended) -------------> WITH
with open('example.txt', 'w') as file:
    file.write('Hello, World!') # File is automatically closed when the block ends




# program to find the list of the files in the folder with name has string "File"  ls -ltr C:/Users/*File*
import os    # optional
import fnmatch # optional
import glob # optional
from pathlib import Path  # mandatory

folder = r"C:\Users\Lenovo\OneDrive\Technology\Python\PyCharm_Project"
print(folder)
p = Path(folder)

for file in p.glob('*File*'):
    print(file)
    
Output:
C:\Users\Lenovo\OneDrive\Technology\Python\PyCharm_Project
C:\Users\Lenovo\OneDrive\Technology\Python\PyCharm_Project\FileOperations.txt
C:\Users\Lenovo\OneDrive\Technology\Python\PyCharm_Project\FileWrite.txt    
    
# program to copy file from source folder  to destination folder
import shutil

src=r"C:\Users\Lenovo\OneDrive\Technology\Python\PyCharm_Project\source\my_csv.csv"
dst=r"C:\Users\Lenovo\OneDrive\Technology\Python\PyCharm_Project\destination"
shutil.copy(src,dst)  # copy will work , but meta data will not copied
shutil.copy2(src,dst)  # copy will work and meta data will copied

# copy source Apple folder and its content to destination folder.
# here in advanced the new destination folder name i.e. Apple is required to write
import shutil

src="C:\Users\Lenovo\OneDrive\Technology\Python\source\Apple"
dst="C:\Users\Lenovo\OneDrive\Technology\Python\destination/Apple"
shutil.copytree(src,dst)

# move the file  graps.txt from source to destination.
import shutil

src=r"C:\Users\Lenovo\OneDrive\Technology\Python\PyCharm_Project\source\Apple\my_csv.csv"
dst=r"C:\Users\Lenovo\OneDrive\Technology\Python\PyCharm_Project\destination\Apple\my_csv.csv"
shutil.move(src,dst)

# move the folder from the source to destination.
import shutil

src=r"C:\Users\Lenovo\OneDrive\Technology\Python\PyCharm_Project\source\Apple\test_folder"
dst=r"C:\Users\Lenovo\OneDrive\Technology\Python\PyCharm_Project\destination\Apple\test_folder"
shutil.move(src,dst)

#rename the file name
import os

old_name=r"C:\Users\Lenovo\OneDrive\Technology\Python\PyCharm_Project\source\my_csv.csv"
new_name=r"C:\Users\Lenovo\OneDrive\Technology\Python\PyCharm_Project\source\my_new_csv.csv"
os.rename(old_name,new_name)

#rename the Apple folder to Orange folder
import os

old_name=r"C:\Users\Lenovo\OneDrive\Technology\Python\PyCharm_Project\source\Apple"
new_name=r"C:\Users\Lenovo\OneDrive\Technology\Python\PyCharm_Project\source\Orange"
os.rename(old_name,new_name)






#The python has single line comment only
print('1')
#print('2')
print('3')

o/p:
1
3

#Multiple line comment can be achive with below way but its not recommended to use " " " as it not as per standard 

print('0')
"""
print('1')
#print('2')
print('3')
"""
#print('4')
print('5')
print('6')

o/p:
0
5
6

#The objective of the " " " is for the documentation purpose and its for all the readymade method made in the python.
#In Pycharm the 'Control' + '/'       Help to comment single line or chunk of block




from datetime import datetime
now = datetime.now()
print(now , now.strftime("%Y-%m-%d")) # convert date into string format


2026-01-15 15:49:22.375929 2026-01-15

from datetime import datetime
date_str = "15-01-2026 10:30"
dt_object = datetime.strptime(date_str, "%d-%m-%Y %H:%M")
print(type(dt_object),dt_object)
<class 'datetime.datetime'> 2026-01-15 10:30:00



#The basic logic to swap the variable values is as below
a=3
b=2
c=a
a=b
b=c
print(a,b)

o/p: 2 3

Twisted logic without using the 3rd variable.

a=3
b=2
a = a+b  # 3+2 = 5
b = a-b  # 5-2 = 3
a = a-b  # 5-3 = 2
print(a,b)

o/p: 2 3

Another alternate way is the XOR logic.

a=3
b=2
a = a^b
b = a^b
a = a^b  
print(a,b)

#Python Provided simple way : Note as a,b = b,a  
#this is in the single line, python solved the problem but if same write in two lines then 1 variable value lost. 
#internally python used the ROT_TWO() such types of the method to solve the problem.

a=3
b=2
a,b = b,a
print(a,b)


#Linear search of the element from the from the list. WHILE LOOP..And ELSE is for WHILE.
# here i holds the index
def f_search(s_list,s):
    i=0
    while i < len(s_list):
        if s_list[i] == s:
            print('Search found', 'index ->' , i )
            return True
        i = i + 1
    else:
        print('ELSE Search not found')
        return False

s_list = [10,20,30,40,50]
print(len(s_list))
if f_search(s_list,50):
    print('Found')
else:
    print('Not Found')


o/p:
5
Search found index -> 4
Found


#Linear search of the element from the from the list. FOR LOOP..ELSE
# here i holds the actual list of the values
def f_search(s_list,s):
    j=0
    for i in s_list:
        if i == s:
            print('Search Found' , 'Index Positon ->',j)# as i holds the actual value,j is required for the index counter
            return True
        j = j + 1
    else:  # If we skip the else part then Function will give the return value as "None"
        print('Search Not Found')
        return False

s_list = [10,20,30,40,50]
if f_search(s_list,40):
    print('Found')
else:
    print('Not Found')
    
o/p:
Search Found Index Positon -> 3
Found
    
#Binary search of the element from the from the list. WHILE LOOP
#Note for the Binary search the values in the list must be in the SORTED order.
# // return the integer values
def f_search(s_list,s):
    lower = 0
    upper = len(s_list)-1
    while lower <= upper:
        mid = (lower+upper) // 2          #0+4//2 = 2       // it will return the INT value
        print('WHILE:', 'upper -> ', upper, 'lower -> ', lower, 'mid -> ', mid)
        if s_list[mid] == s:
            print('Search Found at mid index position ->', mid)
            return True
        elif s_list[lower] == s:
            print('Search Found at lower index position ->', lower)
            return True
        elif s_list[upper] == s:
            print('Search Found at upper index position ->', upper)
            return True
        elif s > s_list[upper] or s < s_list[lower]:
            print('Out of range value')
            return False
        else:
            if s < s_list[mid]:  # it will work only when list in the sorted order.
                upper = mid
                print('IF:', 'upper -> ' , upper , 'lower -> ',lower , 'mid -> ', mid)
            else:
                lower = mid
                print('ELSE:', 'upper -> ', upper, 'lower -> ', lower, 'mid -> ', mid)

s_list = [10,20,30,40,50]
if f_search(s_list,30):
    print('Found')
else:
    print('Not Found')
    
o/p:
WHILE: upper ->  4 lower ->  0 mid ->  2
ELSE: upper ->  4 lower ->  2 mid ->  2
WHILE: upper ->  4 lower ->  2 mid ->  3
Search Found at mid index position -> 3
Found    

#With some minor changes for the upper and lower limites values
def f_search(s_list,s):
    lower = 0
    upper = len(s_list)-1
    while lower <= upper:
        mid = (lower+upper) // 2
        print('WHILE:', 'upper -> ', upper, 'lower -> ', lower, 'mid -> ', mid)
        if s_list[mid] == s:
            print('Search Found at mid index position ->', mid)
            return True
        elif s > s_list[upper] or s < s_list[lower]:
            print('Out of range value')
            return False
        else:
            if s < s_list[mid]:
                upper = mid-1
                print('IF:', 'upper -> ' , upper , 'lower -> ',lower , 'mid -> ', mid)
            else:
                lower = mid+1
                print('ELSE:', 'upper -> ', upper, 'lower -> ', lower, 'mid -> ', mid)

s_list = [10,20,30,40,50]
if f_search(s_list,30):
    print('Found')
else:
    print('Not Found')   

o/p:
WHILE: upper ->  4 lower ->  0 mid ->  2
IF: upper ->  1 lower ->  0 mid ->  2
WHILE: upper ->  1 lower ->  0 mid ->  0
ELSE: upper ->  1 lower ->  1 mid ->  0
WHILE: upper ->  1 lower ->  1 mid ->  1
Search Found at mid index position -> 1
Found



#Bubble sort , above was for search
def f_sort(s_list): # sort in the ascending order 0..n
    for i in range(len(s_list)-1,0,-1): #range(9-1,0,-1)
        for j in range(i): # range(8)
            print(s_list[j],s_list[j+1])  #s_list[0] , s_list[1]
            if s_list[j] > s_list[j + 1]: #s_list[0] > s_list[1]
                t = s_list[j]
                s_list[j] = s_list[j + 1]
                s_list[j + 1] = t
    print(s_list)


s_list = [4,3,6,2,1,5,9,8,7]
f_sort(s_list)

o/p:  [1, 2, 3, 4, 5, 6, 7, 8, 9]

#alternate  and GOOD way of Bubble sort
#for 1 iteration of the i , run the i-1 times loop and do shifting of the bigger element to last.

def f_sort(s_list):
    for i in range(len(s_list)):
        for j in range(len(s_list)-1):
            if s_list[j] > s_list[j + 1]:
                t = s_list[j]
                s_list[j] = s_list[j + 1]
                s_list[j + 1] = t
    print(s_list)


s_list = [4,3,6,2,1,5,9,8,7]
f_sort(s_list)

s_list = [45,34,67,121,2,768,23,98]
f_sort(s_list)

o/p:  [1, 2, 3, 4, 5, 6, 7, 8, 9]
[2, 23, 34, 45, 67, 98, 121, 768]




#Selection Sort
def f_sort(s_list):
    for i in range(len(s_list)-1): #range(6-1)
        minpos = i  #minpos = 0
        for j in range(i,len(s_list)):  #range(0,6)
            if s_list[j] < s_list[minpos]:  #s_list[0] < s_list[0]
                minpos = j #minpos = 0
        t = s_list[i]
        s_list[i] = s_list[minpos]
        s_list[minpos] = t
        print(s_list)

s_list = [6,5,4,3,2,1]
f_sort(s_list)

o/p:
[1, 5, 4, 3, 2, 6]
[1, 2, 4, 3, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]

#Assume that mySql is installed in your machine
#and database name : latesh exists 
#and latesh database has 1 table name : student with 3 values in it.

create database latesh;
use latesh;
create table student(name varchar(25),college varchar(25));
insert into student values('Latesh','Manibai');
insert into student values('Ruchi','RM Tekrawal');
insert into student values('Vaneesa','Indira');
select * from student;

#Installed the connector which is required to make the connection between Python and mySQL database.
#Direct connection is not possible, connector required mandatory.

C:\Users\latesh.sangani>pip3 install mysql.connector
Collecting mysql.connector
  Downloading mysql-connector-2.2.9.tar.gz (11.9 MB)
     |████████████████████████████████| 11.9 MB 1.7 MB/s
  Preparing metadata (setup.py) ... done
Using legacy 'setup.py install' for mysql.connector, since package 'wheel' is not installed.
Installing collected packages: mysql.connector
    Running setup.py install for mysql.connector ... done
Successfully installed mysql.connector-2.2.9


#Open the Sublime editor for the mysql connection test and coding.
#By default with PyCharm this DB connection is not working.
#May be PyCharm need some settings.

#cx_Oracle oracle library
#pyodbc    sql server
#pymysql  mysql
#Psycopg2  postgre

#Basic connection of the Python with mysql
#Run the below command with Control + B command in the Sublime.

import mysql.connector
mydb = mysql.connector.connect(host= "localhost",user = "lsangani" , passwd = "lsangani")

o/p: [Finished in 1.2s]

import mysql.connector
mydb = mysql.connector.connect(host= "localhost",user = "lsangani" , passwd = "lsangani")

mycursor = mydb.cursor()
mycursor.execute("show databases")

for i in mycursor:
	print (i)
    
o/p:  #see here along with default installed database , the latesh database also installed.

('information_schema',)
('latesh',)
('mysql',)
('performance_schema',)
('sakila',)
('sys',)
('world',)
[Finished in 1.0s]



import mysql.connector
mydb = mysql.connector.connect(host= "localhost",user = "lsangani" , passwd = "lsangani",database = 'latesh')

mycursor = mydb.cursor()
mycursor.execute("select * from latesh.student")

for i in mycursor:
	print (i)
    
o/p:
('Latesh', 'Manibai')
('Ruchi', 'RM Tekrawal')
('Vaneesa', 'Indira')
[Finished in 1.3s]
   

#Alternate Way to store output in the Python and print it: fetchall is the method for mysql libarary.

import mysql.connector
mydb = mysql.connector.connect(host= "localhost",user = "lsangani" , passwd = "lsangani",database = 'latesh')

mycursor = mydb.cursor()
mycursor.execute("select * from latesh.student")

output = mycursor.fetchall()

for i in output:
	print (i)
    
o/p:

('Latesh', 'Manibai')
('Ruchi', 'RM Tekrawal')
('Vaneesa', 'Indira')
[Finished in 1.2s]

#Alternate Way to store output in the Python and print only 1st record:fetchone()

import mysql.connector
mydb = mysql.connector.connect(host= "localhost",user = "lsangani" , passwd = "lsangani",database = 'latesh')

mycursor = mydb.cursor()
mycursor.execute("select * from latesh.student")

output = mycursor.fetchone()

for i in output:
	print (i)   

o/p:

Latesh
Manibai
[Finished in 1.1s]


# oracle connection and testing
import cx_Oracle
connection = cx_Oracle.connect('userid/password@hostname:port/sid')
print(connection.version)
cursor = connection.cursor()
sql_create = """ 
CREATE TABLE EMPLOYEE
(
NAME VARCHAR2(100),
AGE NUMBER,
GENDER CHAR(1)
)
"""
cursor.execute(sql_create)

cursor.execute()  # execute the single query
cursor.executemany() # execute the parameterized query
cursor.fetchone() # fetch single row
cursor.fetchall() # fetch all rows
cursor.fetchmany(n)  #fetch n number of rows

connection.commit()
connection.rollback()

cursor.close()
connection.close()


#Zip Function in the python , make 1 to 1 mapping with 2 list.
zip1 = ['1','2','3','4','5']
zip2 = ['Latesh','Ruchi','Vaneesa','Kishor','Sangita']
print(type(zip(zip1,zip2)))
zip_output = list(zip(zip1,zip2))
print(zip_output)

o/p: #its list output
<class 'zip'>
[('1', 'Latesh'), ('2', 'Ruchi'), ('3', 'Vaneesa'), ('4', 'Kishor'), ('5', 'Sangita')]

#Set Function.  make 1 to 1 mapping with 2 list but ignore duplicate values.
zip1 = ['1','2','3','4','5','6']
zip2 = ['Latesh','Ruchi','Vaneesa','Kishor','Sangita','Latesh']
zip_output = set(zip(zip1,zip2))
print(zip_output)


o/p:  #its tuple output
{('1', 'Latesh'), ('6', 'Latesh'), ('4', 'Kishor'), ('3', 'Vaneesa'), ('2', 'Ruchi'), ('5', 'Sangita')}


# dict function to provide output in : format to make JSON files.

zip1 = ['1','2','3','4','5','6']
zip2 = ['Latesh','Ruchi','Vaneesa','Kishor','Sangita','Latesh']
zip_output = dict(zip(zip1,zip2))
print(zip_output)

o/p:
{'1': 'Latesh', '2': 'Ruchi', '3': 'Vaneesa', '4': 'Kishor', '5': 'Sangita', '6': 'Latesh'}

#For loop on zip function to merge 2 list.
zip1 = ['1','2','3','4','5','6']
zip2 = ['Latesh','Ruchi','Vaneesa','Kishor','Sangita','Latesh']
zip_output = zip(zip1,zip2)

for (i,j) in zip_output:
    print(i,j)
    
o/p:
1 Latesh
2 Ruchi
3 Vaneesa
4 Kishor
5 Sangita
6 Latesh

# use of the json.load ( convert file or json string in the form of the python dictionary)
import json
json_string = '{"name": "Alice", "age": 30, "is_student": false}'
# Use json.loads() to convert the JSON string to a Python dictionary
python_object = json.loads(json_string)
print(python_object)
# Output: {'name': 'Alice', 'age': 30, 'is_student': False}
print(type(python_object))
# Output: <class 'dict'>
# You can then access elements like a standard Python object
print(python_object["name"])
# Output: Alice


File name : data.json
{
  "name": "Francis",
  "age": 25,
  "city": "New York"
}

import json
# Open the JSON file and load its content
try:
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)        
    # Now 'data' is a Python dictionary
    print(data)
    print(f"Data type: {type(data)}")
    print(f"Name: {data['name']}")

except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError:
    print("Error: Could not decode JSON from the file. Check for invalid JSON syntax.")
    

Sockets:
1) TCP : Connection protocal
2) UDP : Connection less protocal

#TCP -> Transmission control protocal
#UDP -> User Datagram Protocal

#Range of the port number 0->65535
#Dont use the below 1000 ,as they were occupied with Windows and Linux servers.   

#Server and client communication.

file 1 :  server.py

import socket

# step1
s= socket.socket()
print('Server Socket Created')

# step2
s.bind(('localhost',9999))

# step3
s.listen(3)
print('Waiting for the connection')

# step4 : infinet loop to accept the connection 24*7.
while True:
    con , address = s.accept()
    i = con.recv(2000).decode()
    print("Connection with" , con , "address with " , address )
    print("Name is ", i)
    con.send(bytes("Welcome to Server","utf-8"))
    con.close()


file 2 : client.py

import socket

# step1
c= socket.socket()
print('Client Socket Created')

# step2
c.connect(('localhost',9999))

#step3
#print(c.recv(2000).decode())
#print(c.recv(2000))

#step4
i = input('Enter your name to send server : ')
c.send(bytes(i,'utf-8'))
print(c.recv(2000).decode())


First run the server.py
promopt :

Server Socket Created
Waiting for the connection

Second run the client.py
prompt:   input "Latesh" given

Client Socket Created
Enter your name to send server : Latesh
**Hit Enter key and look at server side output**

Output:

server.py

Server Socket Created
Waiting for the connection
Connection with <socket.socket fd=552, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 9999), raddr=('127.0.0.1', 51942)> address with  ('127.0.0.1', 51942)
Name is  Latesh                   # message came from the client


client.py

Client Socket Created
Enter your name to send server : Latesh
Welcome to Server  # message came from the server




#Email sending your python
https://www.youtube.com/watch?v=BsVQ_cBmEwg

import smtplib

print('email task start')
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()  # start tsl transport layer security
server.login('sangani.vaneesa@gmail.com','xxxxxxxxx')   # sender login and password
server.sendmail('sangani.vaneesa@gmail.com','latesh.sangani@gmail.com','Papa Vaneesa Loves you!!!!')   # sender , receiver , body
print('email task over')

Output:
email task start
email task over

email will come to latesh.sangani@gmail.com and below is the content

Papa Vaneesa Loves you!!!!


# split string into words

txt = 'hello, my name is latesh , I am 35 yrs old'
x = txt.split(',')
print(x)

o/p: ['hello', ' my name is latesh ', ' I am 35 yrs old']


# Command to display image  , It will work with Jupyter notbook, pycharm will not dispaly the image.
from IPython.display import Image
Image(filename = r'C:\Users\Lenovo\OneDrive\Technology\Python\PyCharm_Project\Latesh.JPG')



#Convert the XML file into CSV file into plain python.
youtube.com/watch?v=NVES_jL9bnw

import csv
import xml.etree.ElementTree as ET

def xml_to_csv(file_path,csv_name) -> None:
    tree = ET.parse(file_path)
    root = tree.getroot()

    with open(csv_name,'w') as csv_file:
        writer = csv.writer(csv_file)
        headers = (child.tag for child in root[0])
        writer.writerow(headers)
        num_records = len(root)

        for record in range(num_records):
            rec = (child.text for child in root[record])
            writer.writerow(rec)

if __name__ == '__main__':
    import sys
    import pathlib

    try:
        file_path = r"C:\Users\latesh.sangani\OneDrive - Accenture\Technology\Python\PyCharm_Project\employees.xml"
        csv_name = "employees.csv"

    except IndexError:
        sys.exit('Two parameters required: 1 XML file path name and 1 CSV file')

    with pathlib.Path(file_path) as xml_file:
        if xml_file.is_file():
            xml_to_csv(file_path,csv_name)

        else:
            sys.exit(f'File Not Found {file_path}')
            
            
# file splitting multiple CSV file or any file            
            
import os
import pandas as pd
import uuid

class FileSettings(object):
    def __init__(self, file_name, row_size=100):
        self.file_name = file_name
        self.row_size = row_size

class FileSplitter(object):
    def __init__(self,file_settings):
        self.file_settings = file_settings

        if type(self.file_settings).__name__ != "FileSettings":
            raise Exception("Please pass correct instance ")

        self.df = pd.read_csv(self.file_settings.file_name,chunksize=self.file_settings.row_size)

    def run(self,directory="temp"):
        try:
            os.mkdir(directory)
        except Exception as e:pass
        counter = 0
        while True:
            try:
                file_name = "{}/{}_{}_row_{}_{}_csv".format(
                    directory,self.file_settings.file_name.split(".")[0],counter,self.file_settings.row_size,uuid.uuid4().__str__()
                )
                df = next(self.df).to_csv(file_name)
                counter = counter + 1
            except StopIteration:
                break
#            except Exception as e:
        return True

def main():
    helper = FileSplitter(FileSettings(file_name='sample11.csv',row_size=10))
    helper.run()

main()
