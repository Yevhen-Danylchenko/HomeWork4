
def My_Func_Max (my_list) :
    num = my_list[0]
    for index in my_list :
        if num <= index :
            num = index

    return num

my_list = [1,4,-5,3,7,9,-12,0,8]

print(My_Func_Max (my_list))

My_Func_Max (my_list)
