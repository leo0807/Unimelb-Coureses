from collections import Counter
from ex_gol import *

def text_encode(text):
    count = 0
    result = ""
    #print(Counter(text))
    for k,v in dict(Counter(text)).items():
        result += exp_golomb_encode(ord(k)) + exp_golomb_encode(v)
    print(result)
    return result        

def text_decode(text):
    text = exp_golomb_decode(text)
    result = ""
    for i in range(0,len(text),2):
        result += chr(text[i]) * text[i + 1]
    print(result)
    return result 
    
def image_encode(filename):
    return

if __name__ == '__main__':
    text = "aaaaaaaaaaabbbbbbbbbssssssggggggggfffffff"
    a = text_encode(text)
    b = text_decode(a)
    print(text == b)
