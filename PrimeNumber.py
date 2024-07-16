num = int(input('Введіть ціле число: \t'))

def My_Func_Prime (num) :

    for index in range(2,num) :
        if num % index != 0 :
            return True
        else: return False

print(My_Func_Prime (num))

My_Func_Prime (num)