s="this is a string"

s.lower().startswith('y')
print(s.upper().startswith('T')) #checks whether the str is starting with T or not then gives a bool value 
print (s)
w=s.replace('this','what')

print(s)
print(w)
#the syntax response.lower( ).startswith( y ) first evaluates the method call, response.lower( ), which itself returns a new string instance, and then the startswith('y') method is called on that intermediate string.


pairs=[ ('ge','irsih'),('de','german')]
s=dict(pairs)

print(s)


a='the'
b='he'
print(a != b)