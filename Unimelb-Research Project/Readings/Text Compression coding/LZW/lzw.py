from io import StringIO
def encode(inputs):
    compressed = ""
    compressed_dictionary = {chr(i): i for i in range(256)}

    w ,dict_size= "",256
    result =[]
    for term in inputs:
        combination = w + term
        if combination in compressed_dictionary:
            w = combination
        else:
            result.append(compressed_dictionary[w])
            compressed_dictionary[combination] = dict_size
            dict_size += 1
            w = term

    if w:
        result.append(compressed_dictionary[w])
    return result

def decode(inputs):
    dict_size = 256
    dictionary = {i: chr(i) for i in range(dict_size)}

    result = StringIO()
    w = chr(inputs.pop(0))
    result.write(w)
    for k in inputs:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.write(entry)

        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry
    return result.getvalue()



if __name__ == '__main__':
    inputs = ""
    with open("/home/leo/orgin.txt","r") as f:
        lines = f.readlines()
        for line in lines:
            inputs += line
    a = encode(inputs)
    with open("/home/leo/lzw_encode.txt","wb") as o:
        for i in a:
            o.write(bytes(str(i),encoding = "utf-8"))
           #o.write(" ")
    b = decode(a)
    with open("/home/leo/lzw_decode.txt","w") as d:
        d.write(b)

