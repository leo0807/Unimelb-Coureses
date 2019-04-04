from math import ceil,floor,log
import re

global symbol,decode
symbol, decode = False, False
global total
total = 0

def Binary_Code(x,lo,hi):
    print(x)
    global total
    results = hi-lo+1
    if results <= 0:
        print("math error")
    else:
        temp = ceil(log(results,2))
        print(str(lo)+"<----"+str(x)+"---->"+str(hi)+" :"+str(temp)+'bits')
    #total += temp
    #print('Totally consumed'+str(total)+'bits')

def dgaps(L):
    global symbol
    if symbol:
        pass
    else:
        for index in range(len(L)):
            if index > 0:
                L[index] += int(L[index-1])                
            else:
                L[index] = int(L[index])
        symbol = True
#print(L)
    return L


def Binary_Interpolative_Code(L,lo,hi):
# L = dgaps(L)
# print(L,lo,hi,"input")
    if type(L) != int:
        f = len(L)
    else:
        f = 1
 
#print(str(f)+"times")
    if f == 0:
        return 0
    elif f == 1:
        return Binary_Code(L,lo,hi)
    else:
        h = (f + 1) / 2 
        f1 = h - 1
        f2 = f - h
        
        L1_indice = int(floor(h-2))
        L2_indice = int(ceil(h))

#print("L1",L1_indice,"L2",L2_indice)
        L1 = L[:L1_indice]
        L2 = L[L2_indice:]
#In the case like a[2:2], will return []
        if L1 == []:
            L1 = L[0]
#due to the limitation of list, it may happen a[-1：]，a[:0]
        if L1_indice <= 0:
            L1 = L[0]
            
        if L2 == []:
            L2 = L[-1]
        if L2_indice <= 0:
            L2 = L
            
        indice = int(ceil(h-1))
# print(indice,"this is indice")
# print(L[indice],lo+f1,hi-f2)

        Binary_Code(L[indice],int(ceil(lo+f1)),int(floor(hi-f2)))
        Binary_Interpolative_Code(L1,lo,L[indice]-1)
        Binary_Interpolative_Code(L2,L[indice]+1,hi)
        return

#while True:         
start_docid = int(input("Please input the starting ponit of docs: "))
lo = start_docid 
end_docid = int(input("Please input the end ponit of docs:"))
hi = end_docid
input_list = input("Plesae input the IDs of docs: ")
range_list = []


    
if input_list == '':
    print("Please not input empty")
else:
    input_list = ''.join(input_list.split())
    L = list(map(int,input_list))
    Decode_L = dgaps(L)
Binary_Interpolative_Code(Decode_L,lo,hi)
print("total bits cost is: ")

'''
file = input("Please Input the address location of test txt file: ")
if file == "":
    print("empty input i")
try:
   file_open = open(file,'r')
   print(file_open.read())
finally:
    if file_open:
        file_open.close()
def encode(doc_id):
    new_id = sorted(doc_id)
    result_list = []
    for index in range(len(new_id)):
        if index == 0:
            result_list.append(new_id[index])
        else :
            result_list.append(new_id[index]-new_id[index-1])
    return result_list
'''
