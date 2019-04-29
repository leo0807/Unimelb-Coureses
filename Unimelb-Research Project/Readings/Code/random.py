from random import sample

def random_numbers(scope,num = 10):
    if type(scope) != int and type(num) != int:
        return "Input must be Integers"        
    if num <= 0 or scope <= 0:
        return "Input must bigger than 0"
    elif scope < num:
        return "Scope must bigger than the randonly generated numbers"
    result = sorted(sample(range(scope),num))
    with open("C:\\Users\\unimelb\\Desktop\\sample.txt","w", encoding ='UTF-8') as f:
        for num in result:
            f.write(str(num)+" ")
