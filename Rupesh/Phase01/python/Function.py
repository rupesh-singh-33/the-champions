#this is my first program
#output fuction
print("Hello World")

#input fuction
name = input("what is your name : ")
print(name)

# type convertion
old_age= input("Enter your age : ")
new_age= int(old_age) +2
print(new_age)

#addition
print("Additon of two number")
first= input ("Enter first number : ")
second= input ("enter second number")
sum= float(first) + float(second)
print(sum)

#strings & operations
name = "Rupesh singh manjhi"
print(name.upper())
print(name.lower())
print(name.find('m'))
print(name.replace("Rupesh singh manjhi", "Satyam"))
print(name.replace("manjhi", "------"))

#search
print("Rupesh" in name)