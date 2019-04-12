def unray_single_encode(n):
      if n < 0 or type(n) != int:
            return "input num must be positive integer"
      elif n == 1:
            return 0
      else:
            return(n-1)*"1"+"0"
def unray_encode(n):
      new_list =[]
      if type(n) == list or type(n) == tuple:
            for num in n:
                  new_list.append((num-1)*"1"+"0")
            return new_list
      else:
            return unray_single_encode(n)
#for single input
def unary_single_decode(n):
      result = n.count("1")
      if result == 0:
            return "1"
      else:
            return result+1
# for list or tuple
def unray_decode(n):
      if type(n) == list or type(n) == tuple or type(n) == str:
            new = []
            temp = 0
            for i in n:
                  if i == "1":
                        temp += 1
                  else:
                        temp += 1
                        new.append(temp)
                        temp = 0
                  
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
