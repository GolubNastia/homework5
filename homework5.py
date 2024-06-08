immutable_var = 555, 'Привет', True
print(immutable_var)
immutable_var[-1]= False
# Приводит к ошибке, т.к кортежи неизменяемы
print(immutable_var)
mutable_list = ([555, 666], 777, 'Привет', True)
print(mutable_list)
mutable_list[0][1]=888
print(mutable_list)