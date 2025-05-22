a = 5
print(a)

#strings
name = "Alex"
print(name)

message = "Hello Sibangi!!"
print(message)
print(type(message))
print(message.upper())
print(message.lower())
print(message.capitalize())
print(message.title())
print(message.count("l"))
print(message.replace("l", "L"))
print("sibangi" in message) #Python is a case-sensitive language
print("sibangi" not in message)

greeting1 = "Hello"
greeting2 = "hello"
if greeting1 == greeting2:
    print("Equal")
else:
    print("Not Equal")

her_name = "Sibangi"
print("Hello " + her_name)
print("Hello" , her_name)
print("Hello {}. How are you?".format(her_name))

#Type Conversion
age_str = "25"
age_num = int(age_str)
print(type(age_str))
print(type(age_num))
