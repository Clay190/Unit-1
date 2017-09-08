#Clay Kynor
#9/8/17
#isItATriangle.py - finding wether or not three sides could create a triangle

sideA = int(input("Enter side A: ",))
sideB = int(input("Enter side B: ",))
sideC = int(input("Enter side C: ",))
maximum = max(sideA,sideB,sideC)
minimum = min(sideA,sideB,sideC)
middle = (sideA+sideB+sideC)-maximum-minimum
print(maximum < (middle+minimum))