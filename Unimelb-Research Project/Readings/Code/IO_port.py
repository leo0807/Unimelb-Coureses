from interpolative_code import *
from numpy import *
from gen_ran_nums import random_numbers
import time
import filecmp

#a = loadtxt('test.txt')
#L = list(map(int,a))
#start = L[0]
#end = L[-1]
random_numbers(200000,170000)  
with open("sample.txt","rb") as r:
        input_file = r.readlines()
temp = loadtxt('sample.txt')
S = list(map(int,temp))
#print(S)
#print("orginal list:",L)
#str1 = interpolative_code(L,start,end)
start_time = time.time()
str1 = interpolative_code(S,S[0],S[-1])
end_time = time.time()
print("encoding time:", end_time - start_time)
with open("encode_str.txt","wb") as f:
          f.write(bytes(str1,encoding = "utf-8"))
print("minimun input value:",S[0])
print("largest input value:",S[-1])
print("Number of values:",len(S))
print("total bits:",len(str1))
decode = exp_golomb_decode(str1)
interpolative_decode(decode,len(S),S[0],S[-1])
with open("decode_str.txt","w") as w:
        #a = map(str,new)
        for i in new_list:
                w.write(str(i))
                w.write(' ')
      #  w.write(new_list)
#print("result:",sorted(new_list))
print(filecmp.cmp("sample.txt","decode_str.txt"))
print(S == sorted(new_list))
