#Clay Kynor
#9/1/17
#slope.py Calculate the slope

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
slope = (y2-y1)/(x2-x1)
print('Your slope is', slope)
print("Your equation is y=", slope,"x+", y1-(slope*x1))
