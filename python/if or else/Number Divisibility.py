#Number Divisibility

num=int(input("Enter the number : "))

if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both")

elif num % 3 == 0 :
    print (" only Divisible by 3")

elif num % 5 == 0:
    print ("only Divisible by 5")

else:
    print("Not Divisible by both")   