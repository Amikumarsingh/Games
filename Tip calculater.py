print(" Welcome to tip calculator!")
a= float(input("What was the total  input? $"))
b= float(input("What percentage tip would you like to give? 10 , 12 and 15?"))
c= float(input("How many people would you like to split?" ))
# CALCULATIONS
d= b/100*a
e= d+a
f= e/c
final_ammount=round(f,3)
#step to round of the number after decimal point
final_ammount="{:.3f}".format(final_ammount)
print(f"Each person should pay $ {final_ammount} ammount")
print("THANK YOU FOR USING TIP CALCULATOR")

