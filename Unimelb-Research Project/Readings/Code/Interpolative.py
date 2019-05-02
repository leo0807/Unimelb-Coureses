import gamma_code
from exp_golomb_code import exp_golomb_encode, exp_golomb_decode
from math import ceil,floor,log
def binary_code(L,lo,hi):
    rang = hi - lo + 1
    if rang == 0:
        return ""
    else:   
      scope = list(range(lo,hi+1))
      if type(L) ==list:
            L = L[0]
      A = L
      position = scope.index(A)
     # print("f:",position,"lo:",lo,"hi:",hi)
     # print("exp_golomb_encode:",exp_golomb_encode(position))
     # print("decode:",exp_golomb_decode(exp_golomb_encode(position)))
      return exp_golomb_encode(position)
            
           
def interpolative_code(L, start, end):
    if type(L) == int:
        length = 0
    else:
        length = len(L)
    if length == 0:
        return ""
    elif length == 1:
        return binary_code(L,start,end)
    else:
        mid_term = int(floor(length / 2))
        increase = mid_term
        decrease = length - mid_term - 1
        L1 = L[:mid_term]
        L2 = L[mid_term+1:]
    return  (binary_code(L[mid_term],start + increase, end - decrease)
             + interpolative_code(L1,start,L[mid_term]-1)
             + interpolative_code(L2,L[mid_term]+1,end) )    
def former_three(L):
    length = len(L)
    start = L[0]
    end = L[-1]
    result_list = ( exp_golomb_encode(length) +
                    exp_golomb_encode(start) +
                    exp_golomb_encode(end) )
new_list = []  
def interpolative_decode(L,length,start,end):
    if length == 0:
        #print(L,"length == 0",start,end)
        return 
    elif length == 1:
        try:
            if end+1 <= L[0]:
                print(L[0],L,start,end,"lenvt")
            new_list.append(start + L[0])
            #new_list.append(range(start,end+1)[L[0]])
        except:
            print(L[0],L,start,end,"lenvt")
        return
    else:
        if L == 0:
            print("hhhhsah",length,start,end)
            new_list.append(start)
            new_list.append(end)
            return
        mid_term = int(floor(length / 2))
        increase = mid_term
        decrease = length - mid_term - 1
        #print(start + increase, end - decrease + 1,L[0])
        split = start + increase + L[0]
        #split = range(start + increase, end - decrease + 1)[L[0]]
        new_list.append(split)
        
        #print(start + increase, end -decrease + 1,L[0],L)
        #L1, L2 = [], []
        L1 = L[1:mid_term+1]
        L2 = L[mid_term+1:]
        # if length = 2, then L1 will be L[1:2],that`s wrong, it should be L[1]
        # L[0] for append ,L[1] for L1, then what for L2
        '''
        if length == 2:
        
        '''
        
        if length == 2:
            L2 = []
            #print(L,start,end)
            #print("L1",L1,increase,start,split - 1,L)
            #print("L2",L2,decrease,split+1,end,L2 == [])
    
        if L1 != []:    
            interpolative_decode(L1,increase,start,split-1)
        if L2 != []:
            interpolative_decode(L2,decrease,split+1,end)
    
    

