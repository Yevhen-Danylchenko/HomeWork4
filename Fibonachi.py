num = int(input('Задайте ціле число: \t'))

def my_func_fib (num) :
    if num <= 0 :
        return 0
    if num == 1 :
        return 1
    else :
        num += my_func_fib (num-1)
        return num

print(my_func_fib (num))

my_func_fib (num)