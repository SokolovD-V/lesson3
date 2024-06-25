immutable_var= 4,"Мир",False
print(immutable_var)
# immutable_var[0]=9  # tuple this is an immuteble list
# print(immutable_var) # The output will display and error
mutable_list = ([56,"Приватный",True])
mutable_list[::2] = "Строковый","Непроходимый"
mutable_list.append(47)
print(mutable_list)