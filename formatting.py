name="John"
age=21
#print("Привет, %s!\n Тебе уже %d" % (name, age))
# %s плейсхолдер строки
# %d плейсхолдер числа
# %f плейсхолдер дроби
print("Привет, {}!\nТебе уже {} год".format(name,age))
input_str="Jessy"
print("Hello, {0:*^11}!".format(input_str))
#Jessy*** >
#***Jessy < 
#***Jessy*** ^