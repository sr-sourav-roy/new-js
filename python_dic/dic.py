#Dictionary questions:

# #write a python script to merge two python dictionaries
# p_1 = {1:10,2:200,3:30,4:400}
# p_2 = {6:600,7:00,8:800,9:90}
# for i in p_2:
#     p_1[i] = p_2[i] #p_1 er bhitore b_2 er sob value thakbe❤️
# print(p_1)
# #or simple system
# # sp = p_1|p_2
# # print(sp)



# #write a python program to sum all the values in a dictionary
# dic = {6:600,7:700,8:800,9:90}
# sum = 0
# for i in dic:
#     sum +=dic[i] #dic er valu print korte |dic[i]| function uses
# print(sum)



# #count the frequency of each elements in list
# fre = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,6]
# dic ={}
# for i in fre:
#     if i in dic.keys():
#         dic [i] +=1
#     else:
#         dic[i] = 1
#
# print(dic)



#write a python program to combine two dictionary by adding values for common keys
p_1 = {1:10,2:200,3:30,4:400}
p_2 = {4:600,7:00,8:800,9:90}

for i in p_2:
    if i in p_1.keys():
        p_1[i] = p_1[i] + p_2[i]

    else:
        p_1[i] = p_2[i]

print(p_1)










