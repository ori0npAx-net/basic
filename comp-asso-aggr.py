class Sq_sum:
    def __init__(self,n):
        n=abs(n)
        self._n=n           
        
    def calculate(self):    
        return sum(i**2 for i in range(1,self._n))      #init should return NOne, not int (compiler gives TypeError) 
     
    def set_n(self,k):
        self.n=abs(k)   
        
    def get_n(self):
        return self._n
  
    def __str__(self):
        return str(self._n)
    
class Result:
    def __init__(self,data):
        self._data=data
        
    def display(self):
        print (self._data)
    
if __name__=="__main__":
    
    # composition
    sq_obj=Sq_sum(10)
    sq=sq_obj.calculate()
    
    re_obj=Result(sq)
    re_obj.display()
    
    
    #association (independent classes/temporaray link)
    obj2=Sq_sum(10)
    re_obj=Result(obj2.calculate())     #result apney argument mein direct object le rha (amooman function apny argument mein dosri class ka obj call kar raha hai)
    re_obj.display()
    
    
    #aggregation 
    #obj3=Sq_sum(10)     
    #Result class ke paas ek reference hai Sq_sum object ka, jo usay bahar se diya gaya hai.Matlab Result class us object ko own nahi karti, sirf use karti hai.
    obj3=Sq_sum(10)  
    re_obj=Result(obj3)
    re_obj.display()  
    