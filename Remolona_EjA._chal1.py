
constant = int(77)
name = input("Enter your name.")
age = input("Enter your age.")
age= int(age)
c_year = input("Enter current year.")
c_year= int(c_year)

f_leap1 = (77 - age)
f_result = (77 - age + c_year)


print("Hi " + name + " " + "you will turn 77 years old in the year",f_result, "you will die in" ,f_leap1*365 ,"days")