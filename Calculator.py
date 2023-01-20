# Напишите программу вычисления арифметического выражения заданного строкой.
#  Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

strMath = '3+3*2-20'
strMath = strMath.replace('+', " + ").replace('-', " - ").replace('*', " * ").replace('/', " / ")
strMath = strMath.split(' ')
print(strMath)
if strMath[1] in '-':
    strMath.pop(0)
    strMath.pop(0)
    strMath[0] = int(strMath[0]) * (-1)
    

def math (a,b,operation):
    result = 0
    if operation == '+': result = int(a) + int(b)
    if operation == '-': result = int(a) - int(b)
    if operation == '*': result = int(a) * int(b)
    if operation == '/': result = int(a) / int(b)
    return result
def answer (strMath):
    counter = 0
    while(counter<len(strMath)):
        ind = 0
        #Для умножения деления
        for i in range(len(strMath)):
            if str(strMath[i]) in "*/":
                strMath[i-1] = (math(strMath[i-1],strMath[i+1],strMath[i]))
                ind = i
                break
        if ind != 0:    
            strMath.pop(ind)
            strMath.pop(ind)
        
        
        #Для сложения, вычитания
           
        for i in range(len(strMath)):
            if str(strMath[i]) in "-+":
                    strMath[i-1] = (math(strMath[i-1],strMath[i+1],strMath[i]))
                    ind = i
                    break
        if ind != 0:    
                strMath.pop(ind)
                strMath.pop(ind)
        counter+=1
    return strMath

print(answer(strMath))

  





