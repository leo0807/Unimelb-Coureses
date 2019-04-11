def vbyte_encode(num):

    # out_bytes stores a list of output bytes encoding the number
    out_bytes = []
    x=num
    while x>=128:
        out_bytes.append((x % 128).to_bytes(1,byteorder="little"))
        x = x//128
    x=x+128
    out_bytes.append(x.to_bytes(1,byteorder="little"))
    return out_bytes


def vbyte_decode(input_bytes, idx):
    
    # x stores the decoded number
    x = 0
    # consumed stores the number of bytes consumed to decode the number
    consumed = 0
    s=0
    cur_pos=idx
    y=int.from_bytes(input_bytes[cur_pos],byteorder="little")
    print(y)
    while y<128:
        x=x^(y<<s)
        s=s+7
        consumed+=1
        cur_pos+=1
        y=int.from_bytes(input_bytes[cur_pos],byteorder="little")
        print(y)
    x=x^((y-128)<<s)
    consumed+=1
    return x, consumed
