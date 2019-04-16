def unsigned_golomb_encode(x):
      bin_x = bin(x+1)[2:]
      return (len(bin_x)-1) * '0'+bin_x
#one input
def unsigned_golomb_decode(x):
      if type(x) != str:
            return "Invalid Type (must binary input)"
      else:
            N,result_list = 0, []
            while len(x)!=0:
                  for index in range(len(x)):
                        if x[index] == '0':
                              continue
                        else:
                              N = index
                              break
                  new = int(x[N:2*N+1],2)-1      
                  result_list.append(new)
                  x = x[2*N+1:]
            if len(result_list) == 1:
                  return result_list[0]
            else:
                  return result_list

def signed_golomb_encode(x):

      if x >= 0:
            bin_x = bin(x)[2:] + '0'
      else:
            bin_x = bin(x)[3:] + '1'
      M = (len(bin_x)-1)* '0'
      return M + bin_x
def signed_golomb_decode(x):
      if type(x) != str:
            return "Invalid Type (must binary input)"
      else:
            N,result_list = 0, []
            while len(x)!=0:
                  for index in range(len(x)):
                        if x[index] == '0':
                              continue
                        else:
                              N = index
                              break
                  if x[2*N] == '1':
                        new = (-1) * int(x[N:2*N],2)
                  else:
                        new = int(x[N:2*N],2)      
                  result_list.append(new)
                  x = x[2*N+1:]
            if len(result_list) == 1:
                  return result_list[0]
            else:
                  return result_list
