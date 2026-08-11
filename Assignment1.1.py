# write a program to calculate the percentage of student based on marks of any 5 subjects

num1 =int(input("Enter your English marks :"))
num2 =int(input("Enter your Mathmatics marks :"))
num3 =int(input("Enter your Science marks :"))
num4 =int(input("Enter your History marks :"))
num5 =int(input("Enter your physics marks :"))

total=num1+num2+num3+num4+num5
percentage=(total/500)*100

print(f"Student percentage is:{percentage}%")


