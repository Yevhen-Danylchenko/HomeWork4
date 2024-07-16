num = int(input('Задайте ціле число: \t'))

def My_Func_Factorial (num) :
    num1 = 1
    for index in range(num) :
        index += 1
        num1 *= index

    return num1

print(My_Func_Factorial (num))

My_Func_Factorial (num)

