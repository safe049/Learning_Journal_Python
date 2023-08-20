print("You should read this in your VScode for education use.")

# Print int(i will call nums.) 666,float 1.0,and string.

print(666)

print(1.0)

print("Pretty,lost after input")

"""
 Test,Make Program stop.
 LOL a test
"""
#YOU FINISHED THE CODING OF FLOAT,NUMBER,STRING PRINT.
input()

# Test of  variable
# This simulate a cash variable

cash = 80.5 #float

# Print "cash" variable out

print(cash)
# or
print("Hello.Your cash left:",cash) # You must enter the ","before you input the variable

# Simulate you have cost 31$ to buy something.
cash = cash - 31.0
# Then print the cash amount after buying sth.
print("You have cost 31$ buying sth.Now you got",cash,"To let your wife beat you.")
# A test,cost 10 every hours.
print("Automatic cost activated.")
print("It is 1 o'clock.You got:",cash)
cash = cash - 10
input()
print("It is 2 o'clock.You got:",cash)
cash = cash - 10
input()
print("It is 3 o'clock.You got:",cash)
cash = cash - 10
input()
print("It is 4 o'clock.You got:",cash)
cash = cash - 10
input()
print("Over.")

# Caculation test.
amount = 0
print(amount)
input()
# + caculation
amount = amount + 7
print(amount)
input()
# - caculation
amount = amount - 1
print(amount)
input()
# * caculation
amount = amount * 2
print(amount)
input()
# / caculation
amount = amount / 2
print(amount)
input()

# This is a full test

money = 50
print("You got",money)
money = money - 10
print("You bought a 10 dollar thing,you got:",money)
money = money - 20
print("You bought a 20 dollar thing,you got:",money)
print("Finished,you got",money,"now.")
input()

# Episode 3:THE type() CODE,it checks the TYPE of a data
# 1.Print data type.
print(type(114514))  # This should be a INT
print(type(3.1415926)) # This should be a FLOAT
print(type("嗯哼哼啊啊啊啊(ahhhhhhhhh)")) # This should be a STRING(str).
input()
# 2.Type variable
STR_VAR = type("hello im a str")
print(STR_VAR)
INT_VAR = type(114514)
print(INT_VAR)
FLOAT_VAR = type(3.1415926)
print(FLOAT_VAR)
input()
# 3.You may set the type(a variable),example:
cash_type = type(cash)
print(cash_type)
input()

# 4.FULL TEST
print(type(114514)) # 1
input()
var = type(1) # 2
print(var)
input()
vartype =type("var")# 3
print(vartype)
input()

# EPISODE 4:CONVERT OF DATA TYPE
# example: int(x) convert x to a int, float(x) convert x to a float, str(x) convert x to a str.
# 1.use a variable to store converted
var_num2str = str(11)
print (var_num2str)
input()
# Check did it complete the convert
var_n2stype = type(var_num2str)
print (var_n2stype)
# it output it is a str,int to str complete.
# of course you can use this too
print(type(var_num2str),var_num2str)
input()
# float to str
var_fl2str = str(1.23)
print(type(var_fl2str),var_fl2str)
input()
# str to float
var_str2fl =  float("1.3") # IT CANT NOT BE FLOAT("A WORD")
print(type(var_str2fl),var_str2fl)
input()
# or
var_st2fl = float("1.5")
print (var_st2fl)
input()
# Check did it complete the convert
var_s2ft = type(var_st2fl)
print (var_s2ft)
#str to int
num = int("114514")
print(type(num),num)
#int to float
numfl = float(31)
print(type(numfl),numfl)
input()
#you may convert a float to a int,but after a test,you will found out the float num's float number will be gone,example:10.443 to int,it will become 10.

#EPISODE 5:How to name sth?
#example naming a variety or other nameable stuffs,1.you cannot use a number as a start,like 1_abc will be a problem,2.limit:you can only use chinese character,english character,_,and numbers to name.3.some python restricted words are false,like else,Continue or sth.
#these restricted words all got its own use in python.just name something you dont really think it will be functional in python.

#Print CACULATIONS
#EPISODE 4.5
print("1 + 1 =", 1 + 1)
print("1 * 1 =", 1 * 1)
print("1 - 1 =", 1 - 1)
print("1 / 1 =", 1 / 1)
#The "" is only for telling you what is it caculating,you may remove it. same number / the same number will make the same number a float.
#% Take the remainder // Take the integer ** exponent

#EVEN EXTRA CACULATION
nums = 1
nums += 1 #This is same as 1+1,cuz num =1 ,it just like num +1 and the num was one,one plus one equals 2.
print(nums)
#others is as same.

#EPISODE 6:DEFINE AND OTHER
"""YOU MAY DEFINE A VARIABLE DATA TYPE AS MULTIPLY WAY.
   There is:'string' "string" and three" string. """

#example.
testone = 'test'
print(type(testone),testone)
test2 = "test"
print(type(test2),test2)
test3 = """test"""
print(type(test3),test3)
# theee """ data  can be multiply lines as the multiply hint.
test4 = """hello
                hi"""
print(type(test4),test4)
input()

#What if u want to get something like you want to contain a ' "" inside the (),but you cannot,now how do you do it?
#1.include "'" 2.include '""' 3.use \ , this was a symbol can remove functional of "" or '' or sth
# example: name = "\"dave\""
name = "\"dave\""
#let we see what will happens
print(type(name),name)
input()
#str type."dave",correct.

#COMPILE STRINGS
#use a + to compile two string.
teldave = "1145141919"
cash2 = "3999999"
#you cannot use a int or float to compile with +,you must convert it by str"num" or input as a string with "".
print("hi,im dave."+"i got "+cash2+".im rich.my tel num is "+teldave)
input()

"""
FORMAT STRING
you can compile easier.
use this:
name8 = "me"
msg1 = "hi %s" % name8
print(msg1)
the % stand for taking a place.
the s stand for turning a variety into a string and
place it in the place % has taken.
if you want to use a lots of variety,use msg1 = "hi %s" % (name8 , name9)
"""

name8 = "me"
msg1 = "hi %s" % name8
print(msg1)
input()

#it presents as hi me
#more: %s = turn anything to a string %d = turn anything to a int %f turn anything to a float.
#EVEN BETTER WAY:{}THE DATA. ADD A f BEFORE THE STRING

name9 = "lol"
age = 19
cashes = 11.4514
print(f"hi,im {name9} ,my age is {age} ,i got {cashes}.") #add spaces to make it more elegance.
input()

#EVEN ELEGANCE:EXPRESSION IS STH LIKE "1 + 1"in name = 1 + 1
#FORMAT A EXPRESSION IS JUST LIKE FORMAT A STRING.
print(f"1+1 equals: {1 + 1}")
input()

#FULL TEST:CACULATE COMPANY STOCK PRICE
comp = "COMPANY7"
stock_price = 17.1
stock_code = 114514
grow_day = 7.5
grow_days = 7

print(f"Hi,this is {comp}. stock price now:{stock_price}.stock code:{stock_code}. growth every day:{grow_day},growed {grow_days}. now stock price:{17.1 + 7.5 * 7 }")
input()

#EPISODE 6:INPUT() 
#USERNAME SIMULATION
print("please.tell me who the fuc are u")
username = input()  #receive the user input and write it into a variety
print(f"got it,you are {username}.")
input()
#BETTER ELEGANCE WAY
user = input("who are you?") #straight put the content print should output to input()
print(f"got it,you are {user} ")
input()
#CHECK NUMBER TYPE
code = input("tell me your credit card number ")
code = int(code)
print("your credit card num type is:",type(code))
input()
#SAME,YOU CAN CHECK FLOAT OR STR TOO.
#LITTLE TEST:LOGIN SYSTEM
name2 = input("please input your username ")
print(f"Welcome,Your name is {name2},What is your user type? ")
type5 = input("please input your type. ")
print(f"Welcome,user {name2},You are a {type5} user.")
input("Enter to close.")

#CHAPTER 1 FINISHED.
