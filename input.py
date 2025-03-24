name = input("What is your name ")
age = input ("How old are you? ")
print ("Hello ", name)
print (f"{name}, you are {age} old")


# casting
length = float(input("Enter the length "))
width = float(input("Enter the width "))
area = length * width
print (f"The area is {area} cm")   

# shopping cart
item = input ("What do you want to buy? ")
price = float(input("What is the price? "))
quality = int(input("How many items? "))
total = price * quality

print (f"You have bought {quality} {item} at ${price}")
print (f"The total cost is: ${total}")


