import random

result = set()
table_space = 5
for i in range (1, 10):
    for j in range (1,10):
        result.add(f"{i:<8}X {j:<8} = ")
        result.add(f"{j:<8}X {i:<8} = ")
        result.add(f"{i*j:<8}/ {i:<8} = ")
        result.add(f"{i * j:<8}/ {j:<8} = ")
        result.add(f"{i * j:<8}/         ={i:<8} ")
        result.add(f"{i * j:<8}/         ={j:<8} ")

result_list = list(result)
random.shuffle(result_list)
space = 45
for line in range(int((len(result_list)-1)/3)):
    print (f"{result_list[line]:<45}{result_list[line+1]:<45}{result_list[line+2]}")
    print ("")
