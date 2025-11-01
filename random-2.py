"""
_______________________________________

    TESTING/CHECKING EXAM ANSWERS
_______________________________________
"""
a=[1,2,3]
b=a
print(a==b,a is b)
print (id(a),id(b))
nums=[1,2,3]
sq=[n**2 for n in  nums]
print(sq)


sum=([x*x for x in range(10)])
sum2=(x*x for x in range(10))
print(sum)
print(next(sum2))
print(next(sum2))
print(list(sum2)) #generator remembers what was the last state so the list continues when from where it left off (resumes)
print(type(sum2))
#print(list(next(sum2))) #gives type error



class Num:
    def __init__(self, value):
        self.value=value
        value=value+1
    def is_even(self)->bool:
        return (self.value & 1) == 0
    def show(self):
        print (self.value)
if __name__=="__main__":
    obj=Num(6)
    print (obj.value)
    f=obj.is_even
    print(f()) 
    obj.show()
    b=obj
    value=10
    print(b.value)

class Seq:
    def __init__(self,data):
        self.data=list(data)
        
if __name__=="__main__":
    nums=[1,2,3]
    obj=Seq(nums)
    nums.append(4)
    print(id(obj.data))
    print(id(nums))