ck_num =int(input("tell me how many cookies you want"))

if ck_num <3:
    print("you dont have many cookies")
elif ck_num<10:
    print("you have a good amount")
elif ck_num>10:
    print("you have a lot of cookies")

#------
force_allign = input("are you a Jedi or a Sith?")
if force_allign == "Jedi":
    print("you get a green lightsaber")
elif force_allign == "Sith":
    print("you get a red lightsaber")
else:
    print("you get a breadstick")

#-------
for x in range(4,40,2):
    print(x)
num = 100
#------
while num >=50:
    print(num)
    num -=10
#------ 
str_val :str
while str_val !="orange":
    print("knock knock, who's there? banana")
    str_val = input()
else:
    print("Orange you glad I didn't say banana?!")
#-----

x = lambda arg1, arg2, arg3 :  (arg1 *arg2 *arg3)  
print("{} - is the value".format(x(10,20,30)) )
#----
b = lambda arg1 : ([print("{} bottles of root beer on the wall".format(f)) for f in range(arg1)])
b(10)