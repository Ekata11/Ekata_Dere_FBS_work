#####Numeric

#1. int
x = 10

#2. float
x = 3.14

#3. complex
x = 3+5j


#####Text

#1.str
x='Firstbit Solution'
x="This is demo"
x='''This is first line. This is second line. This is third line.'''
x="""This is first line.
This is next line"""


####Sequentials

#1.List
x =[1,2,'abc', 3.14]

#2.Tuple
x =(1,2,'abc', 3.14)

#3.Range
x=range(1,11)


####Settype

#1.set
x ={1,2,'abc', 3.14}

#2.frozenset
x =frozenset({1,2,'abc', 3.14})


####Mapping

#1.dict
x = {'Name':'Ekata Dere', 'Dept':'Training'}


####Boolean type

#1. True
x = True

#2. False
x= False

####None type
x = None


####Binary

#1.bytes
data=b"hello"

#2.bytearray
arr=bytearray([6,9,7])
#print(arr)
#print(type(arr))
arr[1]=45
#print(arr)

#3.memoryview
data=bytes("python", "utf-8")
mv = memoryview(data)
print(mv[1])
print(bytes(mv[0:3]))
