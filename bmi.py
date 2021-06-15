#BMI and Body Mass Percentage
#BFP Body Fat Percentage
#Based on the smartbmicalculator webpage 
#MenBFP=(1.20 * BMI)+(0.23*age)-10.8-5.4
#WomenBFP=(1.20 * BMI)+(0.23*age)-5.4

Age=int(input("What is your age?"))
Gender=(input("What is your Gender?"))
Weight=int(input("what is your weight?"))t
Height=int(input("What is your height in inches?"))
BMI=(Weight*703)/(Height)**2
BFP = 0

print("My BMI is", BMI)#outputs the person's BMI

if Gender=="woman"or"female": # You can alter code to get it to work for capitalizations
    BFP = (1.20 * BMI)+(0.23*Age)-5.4 
else:
    BFP = (1.20 * BMI) + (0.23 * Age) - 10.8 - 5.4 

print("My BFP is", BFP)
