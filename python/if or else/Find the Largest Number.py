#Find the Largest Number

x=int(input("Enter the number: "))
y=int(input("Enter the number: "))
z=int(input("Enter the number: "))

if x > y and x > z:
    print(x,"greater than",y ,z)

elif y > x and y > z:
    print(y,"greater than",x, z)

else:
    print(z,"greatet than" ,x,z)