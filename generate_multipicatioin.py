import random

result = set()
table_space = 5
for i in range (1, 10):
    for j in range (1,10):
        result.add(f"{i:<3}X {j:<3} = ")
        result.add(f"{j:<3}X {i:<3} = ")
        result.add(f"{i*j:<3}/ {i:<3} = ")
        result.add(f"{i * j:<3}/ {j:<3} = ")
        result.add(f"{i * j:<3} /    ={i:<3} ")
        result.add(f"{i * j:<3} /    ={j:<3} ")

result_list = list(result)
random.shuffle(result_list)
for line in range(int((len(result_list)-1)/3)):
    print (f"{result_list[line]:<25}{result_list[line+1]:<25}{result_list[line+2]}")
