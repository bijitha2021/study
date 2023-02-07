lst_num = [2,5,1,3,7,9]
n = 3
lst_result = []


for i in range(n):
    lst_result.append(lst_num[i])
    lst_result.append(lst_num[i+n])


print(lst_result)
