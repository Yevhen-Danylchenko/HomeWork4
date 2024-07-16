num = int(input('Задайте ціле число: \t'))

def My_Func_Factorial (num) :
    num1 = 1
    num2 = 2
    if num == 1 :
        return 1
    else :
        num *= My_Func_Factorial (num - 1)
        return num

print(My_Func_Factorial(num))



My_Func_Factorial(num)

