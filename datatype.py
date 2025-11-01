#NUMERIC TYPE (int, float, complex)
a=10        #int
b=67.89     #float
c=3+5j      #complex
print (a, type(a))      # type() gets the type of the varible
print (b, type(b))      
print (c, type(c))
print ("real=",c.real, "imaginary=", c.imag)        # .real gets the real part and .imag gets the imaginary part


# TEXT TYPE (string)
s="hello world"

print(s.upper())                    #all uppercase
print(s.lower())                    #all small case
print(s.capitalize())               #first letter capitalize
print(s[0])                         #acessing index 
print(s[1:4])                       #slicing (includes first,excludes last)
print(s.replace("hello","heyo"))      #replaces word with some other word

#BOOLEAN TYPE (bool)
x = True
y = False

print("x and y:", x and y)   # False
print("x or y:", x or y)     # True
print("not x:", not x)       # False


# LIST
fruits=["cherry","grape","apple"]
vegs=["potato","carrot","cabbage"]
val="cherry"

print(fruits[1])        #acess as an index
print(fruits[0:2])      #slicing

fruits.append("banana") #adds an item
print(fruits)

fruits.remove("cherry")
print(fruits)

fruits.reverse()
print(fruits)
print(fruits+vegs)  #CONCATENATION of sequences 
print(3*vegs)       # adding variables in itself for k no of times (k*s)
print(val in s)     #containment check
print(val not in s) #non-containment check

# TUPLE
t=(1,2,3,4,5)

print(t[3])         #index ke through acess
print(t[0:4])       #slicing 
print(len(t))       #length of the tuple


# RANGE
R=range(1,10,3)     #follows (start, stop, step)
for i in R:
    print(i)
    
    
# SET (similar to maths waley set)
    
s={3,5,3,1,2,4} 
print(s)    #automatically removes duplicate and arranges them(unordered:does not follow the given order) 
s.add(0)    #adds an item 
print(s)
s.remove(3) #removes an item
print(s)



#FROZENSET

fs=frozenset([1,2,3,2])     #automatically removes duplicates and arranges the set
print(fs)                   #immutable hai cannot use add and remove waley functions



#DICTIONARY (dict)

aadmi={"name":"aam","age":24}   #created a dictionary

print("name:",aadmi["name"])    #is tarhan directly print karskty hain
print("age:",aadmi["age"])

aadmi["age"]=25                #updated one key

aadmi["city"]="karachi"         #new key added --> d[key]=value

print(aadmi.keys())            #prints the keys
print(aadmi.values())          #prints the values of the keys
print(aadmi.items())           #prints keys and their values as tuple
print(aadmi)                   #prints full dictionary
del aadmi["name"]               #deletes a key in dict--> del d[key]
print(aadmi)


                 #bonus
print(list(aadmi.items())[0])       #dict ke items ko list banaya hai takey usko as an index acess kar sakon
print(list(aadmi.keys())[0])        #same kaam but sirf dic tki keys ko list banaya hai
print(list(aadmi.values())[0])      #same kaam but sirf dic ki values ko list banaya hai  


#BINARY TYPES (bytes,bytearray,memoryview)
c=bytes([65, 66, 67])   #byte (immutable)
print(c)        #b is for indicating that it is a literal byte class           





ba=bytearray([65, 66, 67])  #bytearray (mutable)
ba[0]=88
print(ba)

mv=memoryview(ba)   #memoryview kinda shows what is actually stored in th array
print(mv[1])










