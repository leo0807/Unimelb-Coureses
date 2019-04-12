def unary_single_encode(n):
      if n < 0 or type(n) != int:
            return "input num must be positive integer"
      elif n == 0:
            return "0"
      else:
            return n*"1"+"0"
def unary_encode(n):
      new_list =[]
      if type(n) == list or type(n) == tuple:
            for num in n:
                  new_list.append(unary_single_encode(num))
            return new_list
      else:
            return unary_single_encode(n)
#for single input
def unary_single_decode(n):
      result = n.count("1")
      if result == 0:
            return 0
      else:
            return result
# for list or tuple
def unary_decode(n):
      if type(n) == list or type(n) == tuple or type(n) == str:
            new = []
            for i in n:
                new.append(unary_single_decode(i))
            return new
      elif type(n) != str:
            try:
                n = str(n)
            except TypeError:
                 print("TypeError")
            else:
                return unary_single_decode(n)
      else:
          return unary_single_decode(n)

def gammaCode_encode(n):
    if type(n) == list or type(n) == tuple:
        result = []
        for num in n:
            binary = bin(num)[3:]
            new = unary_encode(len(binary))+binary
            result.append(new)
    else:
        binary = bin(n)[3:]
        return unary_encode(len(binary))+binary
    return result

def gammaCode_decode(n):
    result_list = []
    if type(n) == list or type(n) == tuple or type(n) == str:
        while len(n) != 0:
            new = n.split("0",1)
            una_len = len(str(new[0]))
            binary = "1" + n[una_len+1:2*una_len + 1]
            result_list.append(int(binary, 2))
            n = n[2 * una_len+1:]
    else:
        n = str(n)
        new = n.split("0",1)
        return int("1" + new[1], 2)
    return result_list
