x="global"

def myfunc():
    #global x (to change th global variable inside the function)
    x="new global" 
    print(x)
    
myfunc()
print(x)