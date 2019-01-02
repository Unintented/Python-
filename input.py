# input中的参数提示给用户，并将用户的输入解读为字符串
message = input("Tell me something:")
print(message + '\n')

height = input("How tall are you, in inches?")
height = int(height)
if height >= 36:
    print("You are tall enough to ride!")
else:
    print("Sorry, you'll be able to ride when you are older!")
