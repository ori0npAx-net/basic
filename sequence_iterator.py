class SequenceIterator:             # made this class to check ke internally iteration ka mechanism kis tarhan work/implement hota hai and custom objects ko manually kis tarhan iterate  karty hain
    def __init__(self,seq):        #first try mein aik underscore missing tha so the terminal gave TypeError which usually comes when init constructor theek na ho ya usmein koi chota bara error ho 
        self._seq=seq
        self._k=-1
        
    def __next__(self):
        self._k+=1                 #we'll write this line here cuz pehley add hona hai then check hona hai is tarhan agar add karney pr 3 ata hai tou woh 3<3 dekhae ga and else execute hjaga 
        if self._k < len(self._seq):
            #self._k+=1             #can't write this here cuz Index out of range ja raha hai. trace karke dekhlo
            return self._k,self._seq[self._k]       #gives index in the element at that index
        else:
            raise StopIteration()
    
    def __iter__(self):
        return self
        
        
if __name__=="__main__":
    series=[10,20,30]
    it=SequenceIterator(series)
    
    for val in it:
        print(val)
    