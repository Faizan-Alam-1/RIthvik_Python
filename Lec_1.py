# function 

# def hello():
#     print("Hello , world")



# def sum(a,b):
#     ans = a+b
#     return ans



# def sum(a,b):
#     return a+b



# Return_val = sum(2,5)
# print(Return_val)


# step1 = create two pointer 


# low = 0
# high = len(lists)-1

# while(low<=high):
#     temp = lists[low]
#     lists[low] = lists[high]
#     lists[high] = temp
#     low +=1
#     high -=1


# print(lists)





# def reverse_list(lists):
#    low = 0
#    high = len(lists) -1

#    while(low <= high):
#       temp = lists[low]
#       lists[low] = lists[high]
#       lists[high] = temp
#       low +=1
#       high -=1

#    return lists   
   


# lists = [1,2,3,4,5,6,7,8,9]


# reverse_list_new = reverse_list(lists)
# print(reverse_list_new)





lists = [1,2,2,1,4,5,3,1]  # [1,2,3,4,5]





# def remove_num(lists):
#     lists2 =[]
#     for i in lists:
#         if i not in lists2:
#          lists2.append(i)
#     return lists2     
     

# new_list = remove_num(lists)     

# print(new_list)






# def car(cost , *feature , **new_feature):
#     print(f"The cost of the car {cost}")
#     print(f"The cost of the car {feature}")
#     print(f"the new fearure of car {new_feature}" )
    


# car(4000, "black" ,"ev" , 300, 4.0 , time = 3 ,  days = "monday" , tips = True)




# x = 1

# def text():
#     print(x)


# print(x) # 2
# text()    





def muit( num , sum ):
    ans = sum(2,5)  # 7*3
    return num * ans

    

sum = lambda a , b : a+b





print(muit( 3 ,sum))



