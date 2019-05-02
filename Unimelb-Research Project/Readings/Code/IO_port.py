from interpolative_code import *
from numpy import *
from gen_ran_nums import random_numbers
#a = loadtxt('test.txt')
#L = list(map(int,a))
#start = L[0]
#end = L[-1]
random_numbers(2000000,1700000)  
with open("sample.txt","r") as r:
        input_file = r.readlines()
temp = loadtxt('sample.txt')
S = list(map(int,temp))
#print(S)
#print("orginal list:",L)
#str1 = interpolative_code(L,start,end)
str1 = interpolative_code(S,S[0],S[-1])
with open("encode_str.txt","w", encoding = "UTF-8") as f:
          f.write(str1)
print("minimun input value:",S[0])
print("largest input value:",S[-1])
print("Number of values:",len(S))
print("total bits:",len(str1))
decode = exp_golomb_decode(str1)
interpolative_decode(decode,len(S),S[0],S[-1])
#print("result:",sorted(new_list))
print(S == sorted(new_list))
