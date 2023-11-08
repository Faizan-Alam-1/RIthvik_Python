# Map( fun ,  iterrable)

# num = [1,2,3,4,5,6] # [1 ,4, 9, 16,25,36]


# def fun(x):
#     return x*x


# squared_num = list(map(fun, num))

# print(squared_num)




# num = [1,2,3,4,5,6] # [1 ,4, 9, 16,25,36]



# squared_num =   tuple(map(lambda a: a*a, num))

# print(squared_num)



# filter( fun ,  iterrable)



# num = [1,2,3,4,5,6,7,8,9]


# even_list_from_num = list(filter(lambda x : x % 2 ==0  , num))
# print(even_list_from_num )


# reduce(fun ,  iterable) 

# from functools import reduce


# num = [1,2,3,4 , 5]


# ans = reduce(lambda x, y : x*y , num)
# print(ans)


# Python Datetime Module 




from datetime import datetime


# 
# print(ans)


# ans = datetime(2023, 11 , 8)
# print(ans)


ans  = datetime.now()   

formated_data_and_time =  ans.strftime('%y-%m-%d'+ " "  +'%H:%M:%S') 
print(formated_data_and_time )








