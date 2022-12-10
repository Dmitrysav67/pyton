#Дан список, вывести отдельно буквы и цифры, пользуясь filter.
#[12,'sadf',5643] ---> ['sadf'] ,[12,5643]
data = [12,'sadf',5643]
res = list(filter(lambda x: type(x) == int , data))
res2 = list(filter(lambda x: type(x) == str , data))
print(res)
print(res2)